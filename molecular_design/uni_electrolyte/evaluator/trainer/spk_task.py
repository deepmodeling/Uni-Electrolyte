# A schnetpack task to properly incorporate Thu-ChenXiang electrolyte database.
# Part of this code are borrowed from schnetpack,
# see https://github.com/atomistic-machine-learning/schnetpack
import os
import warnings
from typing import Optional, Dict, List, Type, Any

import pytorch_lightning as pl
import torch
from torch import nn as nn
from torchmetrics import Metric
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

from schnetpack.model.base import AtomisticModel
from ..inference.visualize import *


class ModelOutput(nn.Module):
    """
    Defines an output of a model, including mappings to a loss function and weight for training
    and metrics to be logged.
    """

    def __init__(
            self,
            name: str,
            loss_fn: Optional[nn.Module] = None,
            loss_weight: float = 1.0,
            metrics: Optional[Dict[str, Metric]] = None,
            constraints: Optional[List[torch.nn.Module]] = None,
            target_property: Optional[str] = None,
    ):
        """
        Args:
            name: name of output in results dict
            target_property: Name of target in training batch. Only required for supervised training.
                If not given, the output name is assumed to also be the target name.
            loss_fn: function to compute the loss
            loss_weight: loss weight in the composite loss: $l = w_1 l_1 + \dots + w_n l_n$
            metrics: dictionary of metrics with names as keys
            constraints:
                constraint class for specifying the usage of model output in the loss function and logged metrics,
                while not changing the model output itself. Essentially, constraints represent postprocessing transforms
                that do not affect the model output but only change the loss value. For example, constraints can be used
                to neglect or weight some atomic forces in the loss function. This may be useful when training on
                systems, where only some forces are crucial for its dynamics.
        """
        super().__init__()
        self.name = name
        self.target_property = target_property or name
        self.loss_fn = loss_fn
        self.loss_weight = loss_weight
        self.train_metrics = nn.ModuleDict(metrics)
        self.val_metrics = nn.ModuleDict({k: v.clone() for k, v in metrics.items()})
        self.test_metrics = nn.ModuleDict({k: v.clone() for k, v in metrics.items()})
        self.metrics = {
            "train": self.train_metrics,
            "val": self.val_metrics,
            "test": self.test_metrics,
        }
        self.constraints = constraints or []

    def calculate_loss(self, pred, target):
        if self.loss_weight == 0 or self.loss_fn is None:
            return 0.0

        loss = self.loss_weight * self.loss_fn(
            pred[self.name], target[self.target_property]
        )
        return loss

    def update_metrics(self, pred, target, subset):
        for metric in self.metrics[subset].values():
            metric(pred[self.name], target[self.target_property])


class UnsupervisedModelOutput(ModelOutput):
    """
    Defines an unsupervised output of a model, i.e. an unsupervised loss or a regularizer
    that do not depend on label data. It includes mappings to the loss function,
    a weight for training and metrics to be logged.
    """

    def calculate_loss(self, pred, target=None):
        if self.loss_weight == 0 or self.loss_fn is None:
            return 0.0
        loss = self.loss_weight * self.loss_fn(pred[self.name])
        return loss

    def update_metrics(self, pred, target, subset):
        for metric in self.metrics[subset].values():
            metric(pred[self.name])


class AtomisticTask(pl.LightningModule):
    """
    The basic learning task in SchNetPack, which ties model, loss and optimizer together.

    """

    def __init__(
            self,
            model: AtomisticModel,
            outputs: List[ModelOutput],
            optimizer_cls: Type[torch.optim.Optimizer] = torch.optim.Adam,
            optimizer_args: Optional[Dict[str, Any]] = None,
            scheduler_cls: Optional[Type] = None,
            scheduler_args: Optional[Dict[str, Any]] = None,
            scheduler_monitor: Optional[str] = None,
            warmup_steps: int = 0,
    ):
        """
        Args:
            model: the neural network model
            outputs: list of outputs an optional loss functions
            optimizer_cls: type of torch optimizer,e.g. torch.optim.Adam
            optimizer_args: dict of optimizer keyword arguments
            scheduler_cls: type of torch learning rate scheduler
            scheduler_args: dict of scheduler keyword arguments
            scheduler_monitor: name of metric to be observed for ReduceLROnPlateau
            warmup_steps: number of steps used to increase the learning rate from zero
              linearly to the target learning rate at the beginning of training
        """
        super().__init__()
        self.model = model
        self.optimizer_cls = optimizer_cls
        self.optimizer_kwargs = optimizer_args
        self.scheduler_cls = scheduler_cls
        self.scheduler_kwargs = scheduler_args
        self.schedule_monitor = scheduler_monitor
        self.outputs = nn.ModuleList(outputs)

        self.grad_enabled = len(self.model.required_derivatives) > 0
        self.lr = optimizer_args["lr"]
        self.warmup_steps = warmup_steps
        self.save_hyperparameters()

    def setup(self, stage=None):
        if stage == "fit":
            self.model.initialize_transforms(self.trainer.datamodule)

    def forward(self, inputs: Dict[str, torch.Tensor]):
        results = self.model(inputs)
        return results

    def loss_fn(self, pred, batch):
        loss = 0.0
        for output in self.outputs:
            loss += output.calculate_loss(pred, batch)
        return loss

    def log_metrics(self, pred, targets, subset):
        for output in self.outputs:
            output.update_metrics(pred, targets, subset)
            for metric_name, metric in output.metrics[subset].items():
                self.log(
                    f"{subset}_{output.name}_{metric_name}",
                    metric,
                    on_step=(subset == "train"),
                    on_epoch=(subset != "train"),
                    prog_bar=False,
                )

    def apply_constraints(self, pred, targets):
        for output in self.outputs:
            for constraint in output.constraints:
                pred, targets = constraint(pred, targets, output)
        return pred, targets

    def training_step(self, batch, batch_idx):

        targets = {
            output.target_property: batch[output.target_property]
            for output in self.outputs
            if not isinstance(output, UnsupervisedModelOutput)
        }
        try:
            targets["considered_atoms"] = batch["considered_atoms"]
        except:
            pass

        pred = self.predict_without_postprocessing(batch)
        pred, targets = self.apply_constraints(pred, targets)

        loss = self.loss_fn(pred, targets)

        self.log("lr", self.optimizer.state_dict()['param_groups'][0]['lr'], on_epoch=True)
        self.log("train_loss", loss, on_epoch=True, prog_bar=False)
        return loss

    def validation_step(self, batch, batch_idx):
        pass

    def test_step(self, batch, batch_idx):
        pass

    def predict_without_postprocessing(self, batch):
        pp = self.model.do_postprocessing
        self.model.do_postprocessing = False
        pred = self(batch)
        self.model.do_postprocessing = pp
        return pred

    def configure_optimizers(self):
        self.optimizer = self.optimizer_cls(
            params=self.parameters(), **self.optimizer_kwargs
        )
        return {
            "optimizer": self.optimizer,
            "lr_scheduler": {
                "scheduler": torch.optim.lr_scheduler.CyclicLR(
                    self.optimizer,
                    base_lr=1e-5,
                    max_lr=1e-3,
                    step_size_up=10,
                    step_size_down=40,
                    cycle_momentum=False,
                    mode="exp_range"
                ),
            }
        }

    def optimizer_step(
            self,
            epoch: int = None,
            batch_idx: int = None,
            optimizer=None,
            optimizer_closure=None,
    ):
        if self.global_step < self.warmup_steps:
            lr_scale = min(1.0, float(self.trainer.global_step + 1) / self.warmup_steps)
            for pg in optimizer.param_groups:
                pg["lr"] = lr_scale * self.lr

        # update params
        optimizer.step(closure=optimizer_closure)

    def save_model(self, path: str, do_postprocessing: Optional[bool] = None):
        if self.global_rank == 0:
            pp_status = self.model.do_postprocessing
            if do_postprocessing is not None:
                self.model.do_postprocessing = do_postprocessing

            torch.save(self.model, path)

            self.model.do_postprocessing = pp_status


class ConsiderOnlySelectedAtoms(nn.Module):
    """
    Constraint that allows to neglect some atomic targets (e.g. forces of some specified atoms) for model optimization,
    while not affecting the actual model output. The indices of the atoms, which targets to consider in the loss
    function, must be provided in the dataset for each sample in form of a torch tensor of type boolean
    (True: considered, False: neglected).
    """

    def __init__(self, selection_name):
        """
        Args:
            selection_name: string associated with the list of considered atoms in the dataset
        """
        super().__init__()
        self.selection_name = selection_name

    def forward(self, pred, targets, output_module):
        """
        A torch tensor is loaded from the dataset, which specifies the considered atoms. Only the
        predictions of those atoms are considered for training, validation, and testing.

        :param pred: python dictionary containing model outputs
        :param targets: python dictionary containing targets
        :param output_module: torch.nn.Module class of a particular property (e.g. forces)
        :return: model outputs and targets of considered atoms only
        """

        considered_atoms = targets[self.selection_name].nonzero()[:, 0]

        # drop neglected atoms
        pred[output_module.name] = pred[output_module.name][considered_atoms]
        targets[output_module.target_property] = targets[output_module.target_property][
            considered_atoms
        ]

        return pred, targets

class SinglePropertyClrTask(AtomisticTask):
    def __init__(
            self,
            model: AtomisticModel,
            outputs: List[ModelOutput],
            optimizer_cls: Type[torch.optim.Optimizer] = torch.optim.Adam,
            optimizer_args: Optional[Dict[str, Any]] = None,
            scheduler_cls: Optional[Type] = None,
            scheduler_args: Optional[Dict[str, Any]] = None,
            scheduler_monitor: Optional[str] = None,
            warmup_steps: int = 0,
            predict_property: str = 'binding_e',
            dump_info_path: str = None,
    ):
        """
        Args:
            model: the neural network model
            outputs: list of outputs an optional loss functions
            optimizer_cls: type of torch optimizer,e.g. torch.optim.Adam
            optimizer_args: dict of optimizer keyword arguments
            scheduler_cls: type of torch learning rate scheduler
            scheduler_args: dict of scheduler keyword arguments
            scheduler_monitor: name of metric to be observed for ReduceLROnPlateau
            warmup_steps: number of steps used to increase the learning rate from zero
              linearly to the target learning rate at the beginning of training
        """
        super(SinglePropertyClrTask, self).__init__(
            model=model,
            outputs=outputs,
            optimizer_cls=optimizer_cls,
            optimizer_args=optimizer_args,
            scheduler_cls=scheduler_cls,
            scheduler_args=scheduler_args,
            scheduler_monitor=scheduler_monitor,
            warmup_steps=warmup_steps
        )
        self.model = model
        self.optimizer_cls = optimizer_cls
        self.optimizer_kwargs = optimizer_args
        self.scheduler_cls = scheduler_cls
        self.scheduler_kwargs = scheduler_args
        self.schedule_monitor = scheduler_monitor
        self.outputs = nn.ModuleList(outputs)

        self.grad_enabled = len(self.model.required_derivatives) > 0
        self.lr = optimizer_args["lr"]
        self.warmup_steps = warmup_steps
        self.save_hyperparameters()
        self.predict_property = predict_property
        self.info_file_flag = None
        self.dump_info_path = os.path.abspath(dump_info_path)
        os.makedirs(self.dump_info_path, exist_ok=True)

    def validation_step(self, batch, batch_idx):
        torch.set_grad_enabled(self.grad_enabled)

        targets = {
            output.target_property: batch[output.target_property]
            for output in self.outputs
            if not isinstance(output, UnsupervisedModelOutput)
        }
        try:
            targets["considered_atoms"] = batch["considered_atoms"]
        except:
            pass

        pred = self.predict_without_postprocessing(batch)
        pred, targets = self.apply_constraints(pred, targets)

        flatten_pred = torch.flatten(pred[self.predict_property]).detach().cpu().numpy()
        flatten_targets = torch.flatten(targets[self.predict_property]).detach().cpu().numpy()
        loss = np.mean(np.abs(flatten_targets - flatten_pred))

        self.log("val_loss", loss, on_step=False, on_epoch=True, prog_bar=True)

        return {"val_loss": loss}

    def test_step(self, batch, batch_idx):
        cwd_ = os.getcwd()
        os.makedirs(self.dump_info_path, exist_ok=True)
        os.chdir(self.dump_info_path)
        torch.set_grad_enabled(self.grad_enabled)

        targets = {
            output.target_property: batch[output.target_property]
            for output in self.outputs
            if not isinstance(output, UnsupervisedModelOutput)
        }
        try:
            targets["considered_atoms"] = batch["considered_atoms"]
        except:
            pass

        pred = self.predict_without_postprocessing(batch)
        pred, targets = self.apply_constraints(pred, targets)

        flatten_pred = torch.flatten(pred[self.predict_property]).detach().cpu().numpy()
        if self.predict_property in ['dielectric_constant', 'viscosity']:
            flatten_pred = pow(10, flatten_pred)

        flatten_targets = torch.flatten(targets[self.predict_property]).detach().cpu().numpy()

        with open("pred", "a") as pred:
            pred.writelines(list(map(lambda x: str(x) + "\n", flatten_pred)))
        with open("target", "a") as target:
            target.writelines(list(map(lambda x: str(x) + "\n", flatten_targets)))

        os.chdir(cwd_)

        loss = np.mean(np.abs(flatten_targets - flatten_pred))
        self.log("test_loss", loss, on_step=False, on_epoch=True, prog_bar=True)
        return {"test_loss": loss}

    def predict_step(self, batch, batch_idx):
        cwd_ = os.getcwd()
        os.chdir(self.dump_info_path)
        torch.set_grad_enabled(self.grad_enabled)

        pred = self.predict_without_postprocessing(batch)
        flatten_pred = torch.flatten(pred[self.predict_property]).detach().cpu().numpy()

        if self.predict_property in ['dielectric_constant', 'viscosity']:
            flatten_pred = pow(10, flatten_pred)
        with open("pred", "a") as pred:
            pred.writelines(list(map(lambda x: str(x) + "\n", flatten_pred)))
        os.chdir(cwd_)

    def configure_optimizers(self):
        self.optimizer = self.optimizer_cls(
            params=self.parameters(), **self.optimizer_kwargs
        )
        return {
            "optimizer": self.optimizer,
            "lr_scheduler": {
                "scheduler": torch.optim.lr_scheduler.CyclicLR(
                    self.optimizer,
                    base_lr=self.scheduler_kwargs['base_lr'],
                    max_lr=self.scheduler_kwargs['max_lr'],
                    step_size_up=self.scheduler_kwargs['step_size_up'],
                    step_size_down=self.scheduler_kwargs['step_size_down'],
                    cycle_momentum=False,
                    mode=self.scheduler_kwargs['lr_mode'],
                ),
            }
        }

    # def configure_optimizers(self):
    #     self.optimizer = self.optimizer_cls(
    #         params=self.parameters(), **self.optimizer_kwargs
    #     )
    #     return {
    #         "optimizer": self.optimizer,
    #         "lr_scheduler": {
    #             "scheduler": torch.optim.lr_scheduler.ExponentialLR(
    #                 self.optimizer,
    #                 gamma=self.scheduler_kwargs['gamma'],
    #             ),
    #         }
    #     }

    def parse_test_result(self, info_file_flag, use_r2_score: bool=True):
        cwd_ = os.getcwd()
        os.chdir(self.dump_info_path)
        flatten_targets = file_2_npy('target')
        flatten_pred = file_2_npy('pred')
        if use_r2_score:
            r = r2_score(y_true=flatten_targets, y_pred=flatten_pred)
        else:
            r, _ = stats.pearsonr(flatten_targets, flatten_pred)
        r = round(r, 3)
        mae_e = np.mean(np.abs(flatten_targets - flatten_pred))
        mae_e = round(mae_e, 3)
        print(f'\n{info_file_flag} mae: {str(mae_e)}\n')
        print(f'{info_file_flag} corr: {str(r)}\n')
        plot_rel(label=flatten_targets, prediction=flatten_pred, flag=info_file_flag, mae=mae_e, r2=r)
        plot_heatmap(label=flatten_targets, prediction=flatten_pred, flag=info_file_flag, mae=mae_e, r2=r)
        plot_rank(label=flatten_targets, prediction=flatten_pred, flag=info_file_flag, use_r2_score=use_r2_score)
        rename_file(flag=info_file_flag)
        np.save('pred.npy', flatten_pred)
        np.save('target.npy', flatten_targets)
        os.chdir(cwd_)

