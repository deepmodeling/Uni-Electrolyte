import os
from typing import Any, Dict

import torch
from pytorch_lightning.callbacks import ModelCheckpoint as BaseModelCheckpoint
from schnetpack.task import AtomisticTask

__all__ = ["ModelCheckpoint"]


class ModelCheckpoint(BaseModelCheckpoint):
    """
    Like the PyTorch Lightning ModelCheckpoint callback,
    but also saves the best inference model with activated post-processing
    """

    def __init__(self, valid_best_model_path: str, last_model_path: str, do_postprocessing=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.valid_best_model_path = valid_best_model_path
        self.last_model_path = last_model_path
        self.do_postprocessing = do_postprocessing

    def on_validation_end(self, trainer, pl_module: AtomisticTask) -> None:
        self.trainer = trainer
        self.task = pl_module
        super().on_validation_end(trainer, pl_module)
        checkpoint = {'model_state_dict': self.task.state_dict()}
        torch.save(checkpoint, self.last_model_path)

    def _update_best_and_save(
            self, current: torch.Tensor, trainer, monitor_candidates: Dict[str, Any]
    ):
        # save model checkpoint
        super()._update_best_and_save(current, trainer, monitor_candidates)

        # save best inference model
        if isinstance(current, torch.Tensor) and torch.isnan(current):
            current = torch.tensor(float("inf" if self.mode == "min" else "-inf"))


        if current == self.best_model_score:
            if self.trainer.strategy.local_rank == 0:
                checkpoint = {'model_state_dict': self.task.state_dict()}
                torch.save(checkpoint, self.valid_best_model_path)
