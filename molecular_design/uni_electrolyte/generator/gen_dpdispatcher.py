import json
import os
import shutil

from uni_electrolyte.generator.gen_pipeline_class_2 import BasePipeline
from uni_electrolyte.evaluator.dataset.data_transform import get_props_npy_from_db, merge_all_db, get_total_num_from_json, get_smiles_from_db
from dpdispatcher import Task, Submission, Machine, Resources


class DpdispatcherGenerator:
    def __init__(self, gen_pipeline: BasePipeline, n_jobs: int, machine_info: dict, resrc_info: dict, common_file_list: list):
        self.gen_pipeline = gen_pipeline
        self.machine_info = machine_info
        self.resrc_info = resrc_info
        self.n_jobs = n_jobs
        self.common_file_list = [os.path.abspath(i) for i in common_file_list]

    def create_unit_gen_params(self):
        self.gen_params_path = os.path.abspath("unit_gen_params.json")
        unit_gen_params = self.gen_pipeline.__dict__
        with open("unit_gen_params.json", "w") as file:
            json.dump(unit_gen_params, file, indent=4)

    def clone_common_files(self):
        self.common_file_list.append(self.gen_params_path)
        if 'gen_ckpt_path' in self.gen_pipeline.__dict__:
            self.common_file_list.append(self.gen_pipeline.gen_ckpt_path)
        for a_file in self.common_file_list:
            a_basename = os.path.basename(a_file)
            if os.path.isfile(a_file):
                shutil.copy(src=a_file, dst=a_basename)
            else:
                shutil.copytree(src=a_file, dst=a_basename)
            if a_basename.endswith('.py'):
                self.handler_filename = a_basename

    def prepare_workbase(self):
        self.create_unit_gen_params()
        self.task_list = []
        self.path_raw = os.path.abspath('raw')
        os.makedirs(exist_ok=True, name=self.path_raw)

        for i in range(self.n_jobs):
            os.chdir(self.path_raw)
            os.makedirs(str(i))
            os.chdir(str(i))
            self.clone_common_files()
            a_task = Task(command=fr'unset SLURM_NTASKS && unset SLURM_JOB_NAME && python {self.handler_filename} 2>&1 ',
                          task_work_path=f'{str(i)}/',
                          forward_files=[f'{self.path_raw}/{str(i)}/*'],
                          backward_files=['generated_molecules/*'])
            self.task_list.append(a_task)
            os.makedirs('generated_molecules')
            os.chdir('generated_molecules')
            os.makedirs('leftnet')
        os.chdir(self.gen_pipeline.workbase)

    def run_a_batch(self):
        machine = Machine.load_from_dict(machine_dict=self.machine_info)
        resources = Resources.load_from_dict(resources_dict=self.resrc_info)
        submission = Submission(work_base=f'{self.path_raw}',
                                machine=machine,
                                resources=resources,
                                task_list=self.task_list,
                                forward_common_files=[],
                                backward_common_files=[]
                                )
        submission.run_submission(check_interval=60, clean=True)

    def post_process(self):
        self.path_cooked = os.path.abspath('cooked')
        os.makedirs(exist_ok=True, name=self.path_cooked)
        success_num = get_total_num_from_json(abs_raw_path=self.path_raw, info_line='Successfully generated molecules:', n_jobs=self.n_jobs)
        pass_topo_num = get_total_num_from_json(abs_raw_path=self.path_raw, info_line='Passed topological check molecules:', n_jobs=self.n_jobs)
        non_duplicated_num = merge_all_db(abs_raw_path=self.path_raw, abs_cooked_path=self.path_cooked, db_name=r'de_redundancy.db', n_jobs=self.n_jobs, properties=self.gen_pipeline.infer_target_list)
        new_info = {
            'Successfully generated molecules:': success_num,
            'Passed topological check molecules:': pass_topo_num,
            "Non-duplicated molecules:": non_duplicated_num,
        }
        if self.gen_pipeline.chk_db_path:
            unseen_num = merge_all_db(abs_raw_path=self.path_raw, abs_cooked_path=self.path_cooked,
                                             db_name=r'unseen.db', n_jobs=self.n_jobs, properties=self.gen_pipeline.infer_target_list)

            new_info.update({'Unseen molecules:': unseen_num})
        synthesizable_num = merge_all_db(abs_raw_path=self.path_raw, abs_cooked_path=self.path_cooked, db_name=r'synthesizable.db', n_jobs=self.n_jobs, properties=self.gen_pipeline.infer_target_list)
        new_info.update({"Synthesizable molecules:": synthesizable_num})
        os.chdir(self.path_cooked)
        with open("info.json", "w") as f:
            json.dump(new_info, f, indent=4)
        get_smiles_from_db(db_path=r'synthesizable.db', smile_file_path=r'synthesizable_smiles.txt')
        os.makedirs('leftnet')
        self.gen_pipeline.leftnet_result_dir = os.path.abspath('leftnet')
        get_props_npy_from_db(db_path=r'synthesizable.db', dump_folder_path=self.gen_pipeline.leftnet_result_dir, properties=self.gen_pipeline.infer_target_list)
        self.gen_pipeline.plot_results()
        os.chdir(self.gen_pipeline.workbase)

    def run_with_dpdispatcher(self):
        self.prepare_workbase()
        self.run_a_batch()
        self.post_process()
