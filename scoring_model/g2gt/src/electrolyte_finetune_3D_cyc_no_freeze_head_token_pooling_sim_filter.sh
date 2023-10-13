# bing energy

if [[ $1 = "be" ]]; then
    python rem4electrolyte_data.py  --predicted_target be  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  3D_20230706_vacuum_train  \
    --input_filename  train.sdf \
    --iid_test_dataset_name 3D_20230706_vacuum_iid  \
    --iid_test_input_filename iid_test.sdf  \
    --ood_test_dataset_name 3D_20230706_vacuum_ood  \
    --ood_test_input_filename  ood_test.sdf  \
    --log_name_prefix  3D_20230706_vacuum \
    --sigmoid_inf -5  --sigmoid_sup 1   

elif [[ $1 = "HOMO" ]]; then
    python rem4electrolyte_data.py  --predicted_target HOMO  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  3D_20230706_vacuum_train  \
    --input_filename  train.sdf \
    --iid_test_dataset_name 3D_20230706_vacuum_iid  \
    --iid_test_input_filename iid_test.sdf  \
    --ood_test_dataset_name 3D_20230706_vacuum_ood  \
    --ood_test_input_filename  ood_test.sdf  \
    --log_name_prefix  3D_20230706_vacuum \
    --sigmoid_inf -18  --sigmoid_sup 3  


elif [[ $1 = "LUMO" ]]; then
    python rem4electrolyte_data.py  --predicted_target LUMO  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  3D_20230706_vacuum_train  \
    --input_filename  train.sdf \
    --iid_test_dataset_name 3D_20230706_vacuum_iid  \
    --iid_test_input_filename iid_test.sdf  \
    --ood_test_dataset_name 3D_20230706_vacuum_ood  \
    --ood_test_input_filename  ood_test.sdf  \
    --log_name_prefix  3D_20230706_vacuum \
  --sigmoid_inf -8  --sigmoid_sup 13   
 
elif [[ $1 = "log_dcs" ]]; then
    python rem4electrolyte_data.py  --predicted_target log_dcs  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  3D_20230706_vacuum_train  \
    --input_filename  train.sdf \
    --iid_test_dataset_name 3D_20230706_vacuum_iid  \
    --iid_test_input_filename iid_test.sdf  \
    --ood_test_dataset_name 3D_20230706_vacuum_ood  \
    --ood_test_input_filename  ood_test.sdf  \
    --log_name_prefix  3D_20230706_vacuum \
  --sigmoid_inf -0.5  --sigmoid_sup 2.5 

elif [[ $1 = "log_vs" ]]; then
    python rem4electrolyte_data.py  --predicted_target log_vs  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  3D_20230706_vacuum_train  \
    --input_filename  train.sdf \
    --iid_test_dataset_name 3D_20230706_vacuum_iid  \
    --iid_test_input_filename iid_test.sdf  \
    --ood_test_dataset_name 3D_20230706_vacuum_ood  \
    --ood_test_input_filename  ood_test.sdf  \
    --log_name_prefix  3D_20230706_vacuum \
  --sigmoid_inf -4  --sigmoid_sup 3 


fi
