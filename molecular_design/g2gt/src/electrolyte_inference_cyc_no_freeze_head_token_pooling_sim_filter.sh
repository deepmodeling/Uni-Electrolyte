# bing energy

if [[ $1 = "be" ]]; then
    python /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py  --predicted_target be   \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path $2  \
    --predict_output_csv_file_path $3 \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -5  --sigmoid_sup 1   


elif [[ $1 = "HOMO" ]]; then
    python /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py  --predicted_target HOMO  \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path $2  \
    --predict_output_csv_file_path $3 \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -18  --sigmoid_sup 3  


elif [[ $1 = "LUMO" ]]; then
    python /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py  --predicted_target LUMO  \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path $2  \
    --predict_output_csv_file_path $3 \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -8  --sigmoid_sup 13   
 
elif [[ $1 = "log_dcs" ]]; then
    python /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py  --predicted_target log_dcs  \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path $2  \
    --predict_output_csv_file_path $3 \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -0.5  --sigmoid_sup 2.5 

elif [[ $1 = "log_vs" ]]; then
    python /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py  --predicted_target log_vs   \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path $2  \
    --predict_output_csv_file_path $3 \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -4  --sigmoid_sup 3 


fi
