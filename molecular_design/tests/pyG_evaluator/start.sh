export PYTHONPATH=$PYTHONPATH:/root/yinshiqiu/Uni-Electrolyte/molecular_design:/root/yinshiqiu/Uni-Electrolyte/molecular_design/uni_electrolyte/evaluator/model/spatial
#cd /root/yinshiqiu/Uni-Electrolyte/molecular_design/tests/pyG_evaluator/
cp ./pyG_train_test.py /root/yinshiqiu/Uni-Electrolyte/molecular_design/tests/pyG_evaluator/pyG_train_test.py #for bohrium task 更灵活
python /root/yinshiqiu/Uni-Electrolyte/molecular_design/tests/pyG_evaluator/pyG_train_test.py $1 $2 $3