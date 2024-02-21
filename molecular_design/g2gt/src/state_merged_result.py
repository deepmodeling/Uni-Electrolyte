import pandas as pd
import torch
import torch.nn as nn

def show_mae(path="./rem_test_iid_log_vs.csv"):
    import pandas as pd
    import torch
    import torch.nn as nn
    mae_loss_fn = nn.L1Loss(reduction="mean")
    test_output_df_tmp = pd.read_csv(path)
    y_pred = torch.tensor(test_output_df_tmp["y_pred"])
    y_true = torch.tensor(test_output_df_tmp["y_true"])
    mae = mae_loss_fn(y_pred, y_true)
    de_log_mae = mae_loss_fn(torch.pow(10, y_pred), torch.pow(10, y_true))
    de_log_ratio = torch.mean(torch.abs(torch.pow(10, y_pred) / torch.pow(10, y_true) - 1))
    print('mae %s' % (mae))
    print("de_log_mae %s" % ( de_log_mae))
    print("de_log_ratio %s" % (de_log_ratio))

def output_process_merge_csv(test_outputs_csv_path_list,tag):
    mae_loss_fn = nn.L1Loss(reduction="mean")

    for fold in range(len(test_outputs_csv_path_list)):
        test_output_df_tmp = pd.read_csv(test_outputs_csv_path_list[fold])
        y_pred = torch.tensor(test_output_df_tmp["y_pred"])
        y_true = torch.tensor(test_output_df_tmp["y_true"])
        mae = mae_loss_fn(y_pred, y_true)
        de_log_mae = mae_loss_fn(torch.pow(10, y_pred), torch.pow(10, y_true))
        de_log_ratio = torch.mean(torch.abs(torch.pow(10, y_pred) / torch.pow(10, y_true) - 1))

        print('fold:%s,%s:mae %s' % (fold,tag, mae))
        print("fold:%s,%s:de_log_mae %s" % (fold,tag, de_log_mae))
        print("fold:%s,%s:de_log_ratio %s" % (fold,tag, de_log_ratio))


    test_output_df = pd.read_csv(test_outputs_csv_path_list[0])
    for fold in range(len(test_outputs_csv_path_list)):
        if fold == 0:
            continue
        test_output_df_tmp = pd.read_csv(test_outputs_csv_path_list[fold])
        test_output_df_tmp = test_output_df_tmp.rename(columns={'y_pred': 'y_pred2'})[["ID", "y_pred2"]]
        test_output_df = pd.merge(test_output_df, test_output_df_tmp, on="ID")
        test_output_df["y_pred"] = test_output_df["y_pred2"] + test_output_df["y_pred"]
        del test_output_df["y_pred2"]
    test_output_df["y_pred"] /= len(test_outputs_csv_path_list)
    test_output_df.to_csv("./merged_test_result_%s.csv" % (tag))



    y_pred = torch.tensor(test_output_df["y_pred"])
    y_true = torch.tensor(test_output_df["y_true"])
    mae = mae_loss_fn(y_pred, y_true)
    de_log_mae = mae_loss_fn(torch.pow(10, y_pred), torch.pow(10, y_true))
    de_log_ratio = torch.mean(torch.abs(torch.pow(10, y_pred) / torch.pow(10, y_true) - 1))

    print('%s:mae %s'% (tag,mae))
    print("%s:de_log_mae %s"%(tag, de_log_mae))
    print("%s:de_log_ratio %s"%(tag, de_log_ratio))

    # with open("./merging_%s.log" % (tag), "w") as fp:
    #     print('%s:mae %s'%(tag, mae), file=fp)
    #     print("%s:de_log_mae %s"%(tag, de_log_mae), file=fp)
    #     print("%s:de_log_ratio %s"%( tag,de_log_ratio), file=fp)



if __name__=="__main__":


    for tag in ["iid","ood"]:
        log_path_tmp_list = [
            "rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20240207235033/test_output_%s_1.csv" % tag,
            "rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20240208000744/test_output_%s_7.csv" % tag,
            "rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20240208000532/test_output_%s_3.csv" % tag,
            "rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20240208000912/test_output_%s_9.csv" % tag,
            "rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20240208000720/test_output_%s_5.csv" % tag
        ]
        test_outputs_iid_csv_path_list = []
        for fold in range(5):
            test_outputs_iid_csv_path_list.append("/personal/Bohrium_task_g2g_result/lightning_logs/%s"%(log_path_tmp_list[fold]))
        output_process_merge_csv(test_outputs_iid_csv_path_list, tag)
