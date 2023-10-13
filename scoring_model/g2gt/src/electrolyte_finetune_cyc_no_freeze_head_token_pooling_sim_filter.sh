# bing energy

if [[ $1 = "be" ]]; then
    python rem4electrolyte_data.py  --predicted_target be  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
     --dataset_name  rem_electrolyte_train_1_CHO_47371_uninf_20230706  \
    --input_filename  1_CHO_47371_uninf_20230706_all_train.csv \
    --iid_test_dataset_name rem_electrolyte_iid_1_CHO_47371_uninf_20230706  \
    --iid_test_input_filename 1_CHO_47371_uninf_20230706_iid_test.csv  \
    --ood_test_dataset_name rem_electrolyte_ood_1_CHO_47371_uninf_20230706  \
    --ood_test_input_filename 1_CHO_47371_uninf_20230706_ood_test.csv  \
    --log_name_prefix  rem_electrolyte_train_1_CHO_47371_uninf_20230706 \
    --sigmoid_inf -5  --sigmoid_sup 1   


elif [[ $1 = "HOMO" ]]; then
    python rem4electrolyte_data.py  --predicted_target HOMO  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
    --dataset_name  rem_electrolyte_train_1_CHO_47371_uninf_20230706  \
    --input_filename  1_CHO_47371_uninf_20230706_all_train.csv \
    --iid_test_dataset_name rem_electrolyte_iid_1_CHO_47371_uninf_20230706  \
    --iid_test_input_filename 1_CHO_47371_uninf_20230706_iid_test.csv  \
    --ood_test_dataset_name rem_electrolyte_ood_1_CHO_47371_uninf_20230706  \
    --ood_test_input_filename 1_CHO_47371_uninf_20230706_ood_test.csv  \
    --log_name_prefix  rem_electrolyte_train_1_CHO_47371_uninf_20230706 \
    --sigmoid_inf -18  --sigmoid_sup 3  


elif [[ $1 = "LUMO" ]]; then
    python rem4electrolyte_data.py  --predicted_target LUMO  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
    --dataset_name  rem_electrolyte_train_1_CHO_47371_uninf_20230706  \
    --input_filename  1_CHO_47371_uninf_20230706_all_train.csv \
    --iid_test_dataset_name rem_electrolyte_iid_1_CHO_47371_uninf_20230706  \
    --iid_test_input_filename 1_CHO_47371_uninf_20230706_iid_test.csv  \
    --ood_test_dataset_name rem_electrolyte_ood_1_CHO_47371_uninf_20230706  \
    --ood_test_input_filename 1_CHO_47371_uninf_20230706_ood_test.csv  \
    --log_name_prefix  rem_electrolyte_train_1_CHO_47371_uninf_20230706 \
  --sigmoid_inf -8  --sigmoid_sup 13   
 
elif [[ $1 = "log_dcs" ]]; then
    python rem4electrolyte_data.py  --predicted_target log_dcs  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
    --dataset_name  rem_electrolyte_train_1_CHO_47371_uninf_20230706  \
    --input_filename  1_CHO_47371_uninf_20230706_all_train.csv \
    --iid_test_dataset_name rem_electrolyte_iid_1_CHO_47371_uninf_20230706  \
    --iid_test_input_filename 1_CHO_47371_uninf_20230706_iid_test.csv  \
    --ood_test_dataset_name rem_electrolyte_ood_1_CHO_47371_uninf_20230706  \
    --ood_test_input_filename 1_CHO_47371_uninf_20230706_ood_test.csv  \
    --log_name_prefix  rem_electrolyte_train_1_CHO_47371_uninf_20230706 \
  --sigmoid_inf -0.5  --sigmoid_sup 2.5 

elif [[ $1 = "log_vs" ]]; then
    python rem4electrolyte_data.py  --predicted_target log_vs  --loaded_target_list be,log_dcs,log_vs,HOMO,LUMO \
    --dataset_name  rem_electrolyte_train_1_CHO_47371_uninf_20230706  \
    --input_filename  1_CHO_47371_uninf_20230706_all_train.csv \
    --iid_test_dataset_name rem_electrolyte_iid_1_CHO_47371_uninf_20230706  \
    --iid_test_input_filename 1_CHO_47371_uninf_20230706_iid_test.csv  \
    --ood_test_dataset_name rem_electrolyte_ood_1_CHO_47371_uninf_20230706  \
    --ood_test_input_filename 1_CHO_47371_uninf_20230706_ood_test.csv  \
    --log_name_prefix  rem_electrolyte_train_1_CHO_47371_uninf_20230706 \
  --sigmoid_inf -4  --sigmoid_sup 3 


fi