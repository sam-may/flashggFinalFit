#!/bin/bash

cd /vols/build/cms/jl2117/hgg/FinalFits/legacy/March20_prep/CMSSW_10_2_13/src/flashggFinalFit/Datacard

eval `scramv1 runtime -sh`

python makeDatacard.py --mergeYears --tagSplit --prune --doSystematics --doScaleCorrelationScheme --years 2016,2017,2018 --cats RECO_0J_PTH_0_10_Tag0,RECO_0J_PTH_0_10_Tag1,RECO_0J_PTH_0_10_Tag2,RECO_0J_PTH_GT10_Tag0,RECO_0J_PTH_GT10_Tag1,RECO_0J_PTH_GT10_Tag2,RECO_1J_PTH_0_60_Tag0,RECO_1J_PTH_0_60_Tag1,RECO_1J_PTH_0_60_Tag2,RECO_1J_PTH_60_120_Tag0,RECO_1J_PTH_60_120_Tag1,RECO_1J_PTH_60_120_Tag2,RECO_1J_PTH_120_200_Tag0,RECO_1J_PTH_120_200_Tag1,RECO_1J_PTH_120_200_Tag2,RECO_GE2J_PTH_0_60_Tag0,RECO_GE2J_PTH_0_60_Tag1,RECO_GE2J_PTH_0_60_Tag2,RECO_GE2J_PTH_60_120_Tag0,RECO_GE2J_PTH_60_120_Tag1,RECO_GE2J_PTH_60_120_Tag2,RECO_GE2J_PTH_120_200_Tag0,RECO_GE2J_PTH_120_200_Tag1,RECO_GE2J_PTH_120_200_Tag2,RECO_PTH_200_300_Tag0,RECO_PTH_200_300_Tag1,RECO_PTH_300_450_Tag0,RECO_PTH_300_450_Tag1,RECO_PTH_450_650_Tag0,RECO_PTH_450_650_Tag1,RECO_PTH_GT650_Tag0,RECO_PTH_GT650_Tag1,RECO_VBFTOPO_VHHAD_Tag0,RECO_VBFTOPO_VHHAD_Tag1,RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0,RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1,RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0,RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1,RECO_VBFTOPO_JET3_LOWMJJ_Tag0,RECO_VBFTOPO_JET3_LOWMJJ_Tag1,RECO_VBFTOPO_JET3_HIGHMJJ_Tag0,RECO_VBFTOPO_JET3_HIGHMJJ_Tag1,RECO_VBFTOPO_BSM_Tag0,RECO_VBFTOPO_BSM_Tag1,RECO_VBFLIKEGGH_Tag0,RECO_VBFLIKEGGH_Tag1,RECO_TTH_HAD_LOW_Tag0,RECO_TTH_HAD_LOW_Tag1,RECO_TTH_HAD_LOW_Tag2,RECO_TTH_HAD_LOW_Tag3,RECO_TTH_HAD_HIGH_Tag0,RECO_TTH_HAD_HIGH_Tag1,RECO_TTH_HAD_HIGH_Tag2,RECO_TTH_HAD_HIGH_Tag3,RECO_WH_LEP_LOW_Tag0,RECO_WH_LEP_LOW_Tag1,RECO_WH_LEP_LOW_Tag2,RECO_WH_LEP_HIGH_Tag0,RECO_WH_LEP_HIGH_Tag1,RECO_WH_LEP_HIGH_Tag2,RECO_ZH_LEP_Tag0,RECO_ZH_LEP_Tag1,RECO_TTH_LEP_LOW_Tag0,RECO_TTH_LEP_LOW_Tag1,RECO_TTH_LEP_LOW_Tag2,RECO_TTH_LEP_LOW_Tag3,RECO_TTH_LEP_HIGH_Tag0,RECO_TTH_LEP_HIGH_Tag1,RECO_TTH_LEP_HIGH_Tag2,RECO_TTH_LEP_HIGH_Tag3,RECO_THQ_LEP --inputWSDir /vols/cms/jl2117/hgg/ws/Feb20_unblinding/stage1_2 --saveDataFrame all_systematics --output Datacard_all_systematics.txt
