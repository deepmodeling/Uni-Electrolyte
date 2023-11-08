import os

from dpdispatcher import Machine, Resources, Task, Submission


def leftnet_dpdispatcher(machine_info, cmdline):
    os.environ['BOHR_TICKET'] = machine_info['ticket']
    machine_dict = {
        "batch_type": "Bohrium",
        "context_type": "Bohrium",
        'local_root': "./",

        'remote_root': './test_dpdispatcher',
        'remote_profile': {
            "email": machine_info['email'],
            "password": '',
            "project_id": machine_info['project_id'],
            "input_data": {
                "job_type": "container",
                "log_file": "log",
                "job_name": "Uni_electrolyte_property_prediction",
                "disk_size": 200,
                "scass_type": machine_info['hardware'],
                "platform": machine_info['platform'],
                "image_name": "registry.dp.tech/dptech/prod-11729/uni-electrolyte-app:uni-electrolyte-app-bootstrap"
            }
        }
    }
    resource_dict = {
        'number_node': 1,
        'cpu_per_node': 4,
        'gpu_per_node': 1,
        'queue_name': "GPU",
        'group_size': 4,
        "envs": {
            "PYTHONUNBUFFERED": "true",
            "BOHR_TICKET": machine_info['ticket'],
        },
    }
    machine = Machine.load_from_dict(machine_dict=machine_dict)
    resources = Resources.load_from_dict(resource_dict)
    local_files = os.listdir('./')
    task1 = Task(
        command=cmdline,
        task_work_path='./',
        forward_files=local_files,
        backward_files=['output/*', 'out.txt'], outlog='out.txt')
    task_list = [task1]
    submission = Submission(work_base='./',
                            machine=machine,
                            resources=resources,
                            task_list=task_list,
                            forward_common_files=[],
                            backward_common_files=[]
                            )
    submission.run_submission(check_interval=10, clean=True)

