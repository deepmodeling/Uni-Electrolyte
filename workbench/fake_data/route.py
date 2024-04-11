
DRY_RUN_DATA = [
    {
        "route_name": "rank1",
        "properties": {
            "step": 3,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank2",
        "properties": {
            "step": 3,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank3",
        "properties": {
            "step": 3,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank4",
        "properties": {
            "step": 3,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank5",
        "properties": {
            "step": 3,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "O=C(O)c1ccccc1-n1nccn1",
                        "label": "O=C(O)c1ccccc1-n1nccn1",
                        "commercial": True,
                        "price": "72.6\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank6",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.45783132314682007,
                        "probability": -0.12672464549541473
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12515997886657715
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12129520624876022
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c([N+](=O)[O-])ccc(Cl)c2C)c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37931036949157715,
                        "probability": -0.11201301962137222
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.36263734102249146,
                        "probability": -0.10135453194379807
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(C)cccc2N)c1.O=C1CCC(=O)N1Cl>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.09891011565923691,
                        "probability": -0.09512269496917725
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank7",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank8",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "CC1(C(=O)O)CCCN1",
                        "label": "CC1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "1200.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 1.0,
                        "probability": -0.11688432842493057
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09177286177873611
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCCC2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.08002990484237671
                    },
                    {
                        "smiles": "CCOC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.10784441232681274
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)Cl)c1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.1758606731891632
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.11670933663845062,
                        "probability": -0.08249300718307495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1195879653096199,
                        "probability": -0.0741521492600441
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.12664812803268433,
                        "probability": -0.0846867561340332
                    },
                    {
                        "smiles": "COC(=O)C1(C)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.13236339390277863,
                        "probability": -0.19519323110580444
                    },
                    {
                        "smiles": "CI.COC(=O)C1CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -5.289507865905762,
                        "probability": -0.1870400458574295
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank9",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "O=C(Cl)C(=O)Cl",
                        "label": "O=C(Cl)C(=O)Cl",
                        "commercial": True,
                        "price": "1.28\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "12",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "13",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-12",
                    "source": "10",
                    "target": "12",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "11-12",
                    "source": "11",
                    "target": "12",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "12-13",
                    "source": "12",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "13",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)Cl)c1": [
                    {
                        "smiles": "O=C(Cl)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7567567527294159,
                        "probability": -0.1729452908039093
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.O=C(Cl)C(=O)Cl>CN(C)C=O.ClCCl>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6578947305679321,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.O=S(Cl)Cl>ClCCl.c1ccncc1>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6578947305679321,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.ClCCl>>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.846356153488159,
                        "probability": -0.12647520005702972
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.O=C(Cl)Cl>>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -5.754045009613037,
                        "probability": -0.11052636057138443
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.ClC(Cl)Cl>>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -5.763882637023926,
                        "probability": -0.1348246932029724
                    },
                    {
                        "smiles": "CC(C)=C(Cl)N(C)C.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)Cl)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.777243614196777,
                        "probability": -0.11636319011449814
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank10",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-8",
                    "source": "7",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "8",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "8-10",
                    "source": "8",
                    "target": "10",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "target": "10",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.O=C(Cl)C(=O)Cl>CN(C)C=O.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.40322577953338623,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1>ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.40322577953338623,
                        "probability": -0.12819017469882965
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank11",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.45783132314682007,
                        "probability": -0.12672464549541473
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12515997886657715
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12129520624876022
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c([N+](=O)[O-])ccc(Cl)c2C)c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37931036949157715,
                        "probability": -0.11201301962137222
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.36263734102249146,
                        "probability": -0.10135453194379807
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(C)cccc2N)c1.O=C1CCC(=O)N1Cl>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.09891011565923691,
                        "probability": -0.09512269496917725
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank12",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.45783132314682007,
                        "probability": -0.12672464549541473
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12515997886657715
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12129520624876022
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c([N+](=O)[O-])ccc(Cl)c2C)c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37931036949157715,
                        "probability": -0.11201301962137222
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.36263734102249146,
                        "probability": -0.10135453194379807
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(C)cccc2N)c1.O=C1CCC(=O)N1Cl>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.09891011565923691,
                        "probability": -0.09512269496917725
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank13",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.45783132314682007,
                        "probability": -0.12672464549541473
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12515997886657715
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12129520624876022
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c([N+](=O)[O-])ccc(Cl)c2C)c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37931036949157715,
                        "probability": -0.11201301962137222
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.36263734102249146,
                        "probability": -0.10135453194379807
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(C)cccc2N)c1.O=C1CCC(=O)N1Cl>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.09891011565923691,
                        "probability": -0.09512269496917725
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank14",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "O=C(O)c1ccccc1-n1nccn1",
                        "label": "O=C(O)c1ccccc1-n1nccn1",
                        "commercial": True,
                        "price": "72.6\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "expert_system",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.45783132314682007,
                        "probability": -0.12672464549541473
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12515997886657715
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4307692050933838,
                        "probability": -0.12129520624876022
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c([N+](=O)[O-])ccc(Cl)c2C)c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37931036949157715,
                        "probability": -0.11201301962137222
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1NC(=O)[C@]1(C)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.36263734102249146,
                        "probability": -0.10135453194379807
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(C)cccc2N)c1.O=C1CCC(=O)N1Cl>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.09891011565923691,
                        "probability": -0.09512269496917725
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank15",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank16",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank17",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1c[nH]nn1",
                        "label": "c1c[nH]nn1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank18",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "O=C(O)c1ccccc1-n1nccn1",
                        "label": "O=C(O)c1ccccc1-n1nccn1",
                        "commercial": True,
                        "price": "72.6\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "C[C@@]1(C(=O)O)CCCN1",
                        "label": "C[C@@]1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "99.2\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.1068539023399353
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09788434952497482
                    },
                    {
                        "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.09341540932655334
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.43421053886413574,
                        "probability": 0.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.20377855002880096
                    },
                    {
                        "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.07035081088542938,
                        "probability": -0.09458772093057632
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1351894736289978,
                        "probability": -0.11803625524044037
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.14947395026683807,
                        "probability": -0.09298502653837204
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.15171797573566437,
                        "probability": -0.08790042251348495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -3.8154542446136475,
                        "probability": -0.16713565587997437
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank19",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(I)c(C(=O)O)c1",
                        "label": "COc1ccc(I)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "19.89\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "CC1(C(=O)O)CCCN1",
                        "label": "CC1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "1200.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "database",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 1.0,
                        "probability": -0.11688432842493057
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09177286177873611
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCCC2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.08002990484237671
                    },
                    {
                        "smiles": "CCOC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.10784441232681274
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)Cl)c1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.1758606731891632
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.11670933663845062,
                        "probability": -0.08249300718307495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1195879653096199,
                        "probability": -0.0741521492600441
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.12664812803268433,
                        "probability": -0.0846867561340332
                    },
                    {
                        "smiles": "COC(=O)C1(C)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.13236339390277863,
                        "probability": -0.19519323110580444
                    },
                    {
                        "smiles": "CI.COC(=O)C1CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -5.289507865905762,
                        "probability": -0.1870400458574295
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    },
    {
        "route_name": "rank20",
        "properties": {
            "step": 4,
            "complete": True
        },
        "workflow": {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc(Br)c(C(=O)O)c1",
                        "label": "COc1ccc(Br)c(C(=O)O)c1",
                        "commercial": True,
                        "price": "0.84\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "c1cn[nH]n1",
                        "label": "c1cn[nH]n1",
                        "commercial": True,
                        "price": "1.494\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "CC1(C(=O)O)CCCN1",
                        "label": "CC1(C(=O)O)CCCN1",
                        "commercial": True,
                        "price": "1200.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "Cc1c(Cl)ccc(N)c1N",
                        "label": "Cc1c(Cl)ccc(N)c1N",
                        "commercial": True,
                        "price": "281.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-3",
                    "source": "1",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "2-3",
                    "source": "2",
                    "target": "3",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "label": "similarity",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "4",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "4-6",
                    "source": "4",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "5-6",
                    "source": "5",
                    "target": "6",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "7",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "7-9",
                    "source": "7",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "8-9",
                    "source": "8",
                    "target": "9",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "label": "unimol",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "10",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "transformer_network",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "expert_system",
                        "confidence_score": 0.8,
                        "probability": 0.8
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.42424243688583374,
                        "probability": -0.12521551549434662
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.04267781600356102,
                        "probability": -0.07558560371398926
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.060306668281555176,
                        "probability": -0.06755616515874863
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -6.134176731109619,
                        "probability": -0.12802264094352722
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1": [
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N.Cl>CCN(CC)CC.O=C(Cl)C(=O)Cl.CN(C)C=O.ClCCl.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(On1nnc2cccnc21)=[N+](C)C.CCN(C(C)C)C(C)C.F[P-](F)(F)(F)(F)F.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5694444477558136,
                        "probability": -0.07393409311771393
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10367210954427719
                    },
                    {
                        "smiles": "Cc1c(Cl)ccc(NC(=O)[C@]2(C)CCCN2C(=O)c2cc(F)ccc2-n2nccn2)c1N>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.41791045665740967,
                        "probability": -0.10514769703149796
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2[N+](=O)[O-])c1>Cl[Sn](Cl)(Cl)Cl.C1CCOC1.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.37078648805618286,
                        "probability": -0.08496806770563126
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc([NH])c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1305147409439087,
                        "probability": -0.08275733143091202
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -0.4180683195590973,
                        "probability": -0.14613541960716248
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1": [
                    {
                        "smiles": "COC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 1.0,
                        "probability": -0.11688432842493057
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.09177286177873611
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)N2CCCC2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.5800000131130219,
                        "probability": -0.08002990484237671
                    },
                    {
                        "smiles": "CCOC(=O)C1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4363636374473572,
                        "probability": -0.10784441232681274
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)Cl)c1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.4285714030265808,
                        "probability": -0.1758606731891632
                    },
                    {
                        "smiles": "CC1(C(=O)O)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.11670933663845062,
                        "probability": -0.08249300718307495
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.1195879653096199,
                        "probability": -0.0741521492600441
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.12664812803268433,
                        "probability": -0.0846867561340332
                    },
                    {
                        "smiles": "COC(=O)C1(C)CCCN1.COc1ccc(-n2nccn2)c(C(=O)O)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "transformer_network",
                        "confidence_score": -0.13236339390277863,
                        "probability": -0.19519323110580444
                    },
                    {
                        "smiles": "CI.COC(=O)C1CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -5.289507865905762,
                        "probability": -0.1870400458574295
                    }
                ],
                "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
                    {
                        "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "database",
                        "confidence_score": 1.0,
                        "probability": 1.0
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.7777777761220932,
                        "probability": -0.11192844063043594
                    },
                    {
                        "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11164479702711105
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.11898676306009293
                    },
                    {
                        "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "similarity",
                        "confidence_score": 0.6486486494541168,
                        "probability": -0.13990871608257294
                    },
                    {
                        "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -2.821465015411377,
                        "probability": -0.12816283106803894
                    },
                    {
                        "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
                        "reaction_type": "unimol",
                        "confidence_score": -4.799795627593994,
                        "probability": -0.11633466929197311
                    }
                ]
            }
        }
    }
]