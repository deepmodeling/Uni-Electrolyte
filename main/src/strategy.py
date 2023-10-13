
def RECORD_DATASET_func(mol_file,model_property_list,fingerprint_list):
    """
    mol_file:
        CSV file or sdf file，
        the CSV file has 2 columns, "ID" and "smiles".
        In the sdf file, each conformation has "ID" tag and "smiles" tag . Each smiles and ID could only appear once
        and correspond to a unique conformation.

    model_property_map:
    fingerprint_list:
    """
    #1  输入文件格式检查
    # 1 将输入smiles 转换为标准smiles

    #2 如果没有构象输入，则调用构象采样函数,结果保存到本地临时文件

    #3 调用各个性质各个模型打分函数，结果保存到本地临时文件

    # 4 调用各个性质各个模型打分函数，结果保存到本地临时文件

    # 5 调用各个指纹算法，结果保存到本地

    #结果整理成表

    #返回数据库名
    pass

def SCREENING_func(dataset_name,Binding_energy_eV_screening_condition,
                   Dielectric_constant_of_solvents_screening_condition,
                   Viscosity_of_solvents_mPas_screening_condition,
                   LUMO_eV_screening_condition,
                   HOMO_eV_screening_condition):

    #1 检查daset_name 在数据库中是否存在
    #2检查各个筛选条件合法性

    #3 用sql计算数据库中各个模型各个属性预测值，返回topN结果

    pass

def SEARCH_MOL_func(query_mol_file):
    """
    CSV file or sdf file，
        the CSV file has 2 columns, "ID" and "smiles".
    """
    pass

    #1 将输入smiles 转换为标准smiles 建立和ID的映射
    #2 在总表中查询smiles，返回属性预测结果，根据不同模型权重求平均
    #返回查询结果，以及未查询到的smiles list
