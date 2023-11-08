import os
import shutil

from dpdispatcher import Machine, Resources, Task, Submission


def postgres_interaction(postgres_handler, workbase):
    cwd_2 = os.getcwd()
    os.chdir(workbase)
    if postgres_handler == 'insert':
        shutil.copy(src=r'/root/postgres_scripts/insert_test.py',
                    dst='insert_test.py')
    else:
        os.chdir(cwd_2)
        return

    cmdline = 'su postgres -c "/home/postgres/anaconda3/bin/python insert_test.py"'

    machine_dict = {
        "batch_type": "Shell",
        "context_type": "SSHContext",
        'local_root': "./",
        'remote_root': '/home/postgres/test_dpdispatcher',
        'remote_profile': {
            "hostname": 'qghi1060629.bohrium.tech',
            "password": 'XTfVrLPVPwCMOz80',
            "username": 'root',
            "port": 22,
        },
    }

    resource_dict = {
        'number_node': 1,
        'cpu_per_node': 4,
        'gpu_per_node': 1,
        'queue_name': "CPU",
        'group_size': 4,
    }

    machine = Machine.load_from_dict(machine_dict=machine_dict)

    resources = Resources.load_from_dict(resource_dict)

    local_files = os.listdir('./')

    task1 = Task(
        command=cmdline,
        task_work_path='./',
        forward_files=local_files,
        backward_files=[])

    task_list = [task1]

    submission = Submission(work_base='./',
                            machine=machine,
                            resources=resources,
                            task_list=task_list,
                            forward_common_files=[],
                            backward_common_files=[]
                            )

    submission.run_submission(check_interval=10, clean=True)
    os.chdir(cwd_2)
