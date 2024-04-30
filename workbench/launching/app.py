import json
import os
from pathlib import Path
from loguru import logger
import subprocess
from dp.launching.app import App
import re
from dp.launching.app.app import PaymentInfo
from utils.token_helper import get_user_key
from utils.bohrium import get_default_project
from utils.tracer import trace_time

retro_synthesis_app: App = App(
    "retro-synthesis", os.environ.get("LAUNCHING_APPLICATION_TOKEN")
)
retro_synthesis_default_version = os.environ.get("LAUNCHING_APPLICATION_VERSION")

# TODO get user payment info
payment_info: PaymentInfo = PaymentInfo(
    os.environ.get("BOHRIUM_PAID_ACCOUNT"), os.environ.get("BOHRIUM_PAID_PROJECT_ID")
)


@trace_time
def submit_job(
    params: dict,
    root_dir: str,
    job_name: str = "wb-job",
    # payment_info: PaymentInfo = payment_info,

):

    logger.info(json.dumps(params))
    json.dump(params, open(os.path.join(root_dir,"app_param.json"), "w"))

    lbj_json_dict={
        "job_name": job_name,
        "command": "python /root/launching_entry/gen_score_screen.py score_screen --json-config  %s "%(os.path.join(root_dir,"app_param.json")),
        "platform": "ali",
        "disk_size": 200,
        "machine_type": "c8_m31_1 * NVIDIA T4",
        "image_name": "registry.dp.tech/dptech/prod-11729/sub:0312",
        "program_id": 14480
    }
    json.dump(lbj_json_dict, open(os.path.join(root_dir, "lbg.json"), "w"))

    logger.info("lbg job submit -i %s -p  %s"%(os.path.join(root_dir,"lbg.json"),root_dir))
    os.system("lbg job submit -i %s -p  %s >%s"%(os.path.join(root_dir,"lbg.json"),root_dir,os.path.join(root_dir,"log")))
    # result = subprocess.run(["lbg","job","submit","-i",os.path.join(root_dir,"lbg.json"),"-p",root_dir])
    # logger.info(result.stdout)
    # 使用正则表达式匹配 JOB ID 后面的数字
    fp=open(os.path.join(root_dir,"log"))
    logger.info(fp.read())
    match = re.search(r'JOB ID: (\d+)',fp.read())

    if match:
        job_id = match.group(1)
        logger.info(f"submit_job {job_name} finish job_id {job_id}")
        return job_id
    else:
        logger.info("Job ID not found.")
        raise Exception("Job ID not found.")


#
# def submit_job(
#     token,
#     params: dict,
#     files: dict = {},
#     job_name: str = "wb-job",
#     # payment_info: PaymentInfo = payment_info,
#     version: str = retro_synthesis_default_version,
#     bohrium_project_id: int = 0,
# ):
#     # TODO performance optimization: submit_job took 2.9323599338531494 seconds
#     user_key = get_user_key(token)
#     if not bohrium_project_id:
#         project_id = get_default_project(token)
#     else:
#         project_id = bohrium_project_id
#     payment = PaymentInfo(user_key, project_id)
#     if os.environ.get("DRY_RUN_MODE") == "True":
#         logger.info("fake submit job due to DRY_RUN_MODE: wb-job-ffcd1aca")
#         return "wb-job-ffcd1aca"
#
#     submit_params = {}
#     if params.get("debug", False):
#         # machine_type c2_m2_cpu if debug
#         submit_params = {
#             "bohrium_job_type": "container",
#             "bohrium_machine_type": "c2_m2_cpu",
#             "bohrium_platform": "ali",
#         }
#
#     logger.info(f"submit_job {job_name} start")
#     if not params:
#         # for debug
#         params = {
#             "input_ligand": "CCO",
#             "max_iteration": 20,
#             "first_step_constrain": "",
#             "origin_output": "",
#             "debug": True,
#             "reaction_type": "ai+expert+database",
#             "route_diversity": "normal",
#         }
#     params["output_dir"] = "__INTERNAL_PLACEHOLDER__{{output_directory}}"
#     job_id = retro_synthesis_app.submit_job(
#         payment, job_name, files, params, version=version, submit_params=submit_params
#     )
#     logger.info(f"submit_job {job_name} finish job_id {job_id}")
#     return job_id


def get_job_status(
    job_id: str,
):
    return retro_synthesis_app.get_job_status(None, job_id)


def get_job_root():
    path = Path(os.environ.get("LAUNCHING_ROOT")) / "jobs"
    return path


def get_job_output_path(job_id: str):
    path = get_job_root() / job_id / "outputs"
    return path


def get_job_result(
    job_id: str,
):
    output_path = Path(
        os.environ.get("SAMPLE_OUTPUT_DIR") or get_job_output_path(job_id)
    )
    sample_path = output_path / "sample.json"
    if sample_path.exists():
        result_path = sample_path
    else:
        result_path = output_path / "result.json"
    if not result_path.exists():
        return None
    with open(result_path, "r") as f:
        try:
            data = json.load(f)
            return data
        except Exception as e:
            logger.error(e)
            return None
