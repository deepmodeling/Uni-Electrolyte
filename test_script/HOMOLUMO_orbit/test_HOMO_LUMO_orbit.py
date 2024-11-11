import json
import os
import sys
#
# {
#             "output_directory": "./output",
#             "gen_mode": {
#                 "type": "Binding_Energy_and_Formular",
#                 "formular": params["Binding_Enegry_And_Formular_Formular"],
#                 "targeted_binding_e": params["Binding_Enegry"],
#                 "n_molecules": int(params["N_Molecules_Input"])
#             }
#         }
def test_HOMO_LUMO_orbit_task():
    launching_json_dict= {
                "output_directory": "./output",
                "n_grids": 75,
                "smiles_name": "smiles",
                "csv_file_path": "input_4.csv",
            }
    json.dump(launching_json_dict, open("./input/test_HOMO_LUMO_orbit_task_launching.json", "w"), indent=2)
    command="python /root/launching_entry/gen_score_screen.py HOMO_LUMO_orbit --json-config  ./test_HOMO_LUMO_orbit_task_launching.json"
    print(command)
    # os.system(command)
    # return

    json.dump(launching_json_dict, open("./input/test_HOMO_LUMO_orbit_task_launching.json", "w"), indent=2)
    lbj_json_dict = {
        "job_name": "test_HOMO_LUMO_orbit_task",
        "command": command,
        "platform": "ali",
        "disk_size": 200,
        "machine_type": "c12_m92_1 * NVIDIA V100" ,
        # c12_m92_1 * NVIDIA V100  c8_m31_1 * NVIDIA T4
        "image_name": image_name,
        "program_id": 14480,
        "input": "input",
        "result": "bohrium_output",
    }
    print(lbj_json_dict)
    json.dump(lbj_json_dict, open("test_HOMO_LUMO_orbit_task_launching_lbg.json", "w"))
    shell_str = f"lbg job submit -i test_HOMO_LUMO_orbit_task_launching_lbg.json"
    os.system(shell_str)
    print(shell_str)

def test_gen_task():
    launching_json_dict= {
        "output_directory": "./output",
        "gen_mode": {"type": "Structure_FingerPrint", "smiles": "CCOC(=O)OCC", "n_molecules": 100},
        "n_grids":75,
    }
    json.dump(launching_json_dict, open("./test_gen_task_launching.json", "w"), indent=2)
    command="python /root/launching_entry/gen_score_screen.py gen_with_score --json-config  test_gen_task_launching.json"
    print(command)
    # os.system(command)
    # return
    json.dump(launching_json_dict, open("./input/test_gen_task_launching.json", "w"), indent=2)
    lbj_json_dict = {
        "job_name": "test_gen_task",
        "command": command,
        "platform": "ali",
        "disk_size": 200,
        "machine_type": "c12_m92_1 * NVIDIA V100" ,
        # c12_m92_1 * NVIDIA V100  c8_m31_1 * NVIDIA T4
        "image_name": image_name,
        "program_id": 14480,
        "result": "bohrium_output",

    }
    json.dump(lbj_json_dict, open("test_gen_task_lbg.json", "w"))
    shell_str = f"lbg job submit -i test_gen_task_lbg.json"
    print(shell_str)
    os.system(shell_str)

def test_score_task():
    launching_json_dict={"output_directory": "./output",
                         "Screen_Switch": {"type": "predict_property_only", "input_file_path": "smiles",
                                            "target": ["Binding_Energy", "Dielectric_Constant", "Viscosity","HOMO", "LUMO"]},
                         "n_grids": 75,
                         }
    json.dump(launching_json_dict, open("./test_score_task_launching.json", "w"), indent=2)

    command="python /root/launching_entry/gen_score_screen.py score_screen --json-config test_score_task_launching.json"
    print(command)
    # os.system(command)
    # return
    json.dump(launching_json_dict, open("./input/test_gen_task_launching.json", "w"), indent=2)
    lbj_json_dict = {
        "job_name": "test_score_task",
        "command": command,
        "platform": "ali",
        "disk_size": 200,
        "machine_type": "c12_m92_1 * NVIDIA V100" ,
        # c12_m92_1 * NVIDIA V100  c8_m31_1 * NVIDIA T4
        "image_name": image_name,
        "program_id": 14480,
        "result": "bohrium_output",

    }
    json.dump(lbj_json_dict, open("test_score_task_lbg.json", "w"))
    shell_str = f"lbg job submit -i test_score_task_lbg.json"
    print(shell_str)
    os.system(shell_str)


if __name__ == "__main__":
    image_name="registry.dp.tech/dptech/prod-17396/sub:1111"
    #test_score_task()
    #test_HOMO_LUMO_orbit_task()
    #test_gen_task()