DATACARD="/home/users/sjmay/ttH/FCNC_FinalFits_v2/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/Datacard_fcnc_hct_FCNC.root"

combineTool.py -M Impacts -d $DATACARD -m 125  --doInitialFit --robustFit 1 -t -1 --expectSignal 0 #--setPhysicsModelParameters r_fcnc_hct=0
combineTool.py -M Impacts -d $DATACARD -m 125  --doFits --robustFit 1 -t -1 --expectSignal 0 #--setPhysicsModelParameters r_fcnc_hct=0 --parallel 20
combineTool.py -M Impacts -d $DATACARD -m 125  -o impacts.json
plotImpacts.py -i impacts.json -o impacts_hct --POI r_fcnc_hct

#combineTool.py -M Impacts -d Datacard_test_simple_hut_FCNC.root -m 125  --doInitialFit --robustFit 1 -t -1 --expectSignal 1 --setPhysicsModelParameters pdfindex_TTHHadronicTag_0_13TeV=2,pdfindex_TTHHadronicTag_1_13TeV=1,pdfindex_TTHHadronicTag_2_13TeV=2,pdfindex_TTHHadronicTag_3_13TeV=2,pdfindex_TTHLeptonicTag_0_13TeV=1,pdfindex_TTHLeptonicTag_1_13TeV=3,pdfindex_TTHLeptonicTag_2_13TeV=3,pdfindex_TTHLeptonicTag_3_13TeV=3
#combineTool.py -M Impacts -d Datacard_test_simple_hut_FCNC.root -m 125  --doFits --robustFit 1 -t -1 --expectSignal 1 --setPhysicsModelParameters pdfindex_TTHHadronicTag_0_13TeV=2,pdfindex_TTHHadronicTag_1_13TeV=1,pdfindex_TTHHadronicTag_2_13TeV=2,pdfindex_TTHHadronicTag_3_13TeV=2,pdfindex_TTHLeptonicTag_0_13TeV=1,pdfindex_TTHLeptonicTag_1_13TeV=3,pdfindex_TTHLeptonicTag_2_13TeV=3,pdfindex_TTHLeptonicTag_3_13TeV=3 --parallel 20
#combineTool.py -M Impacts -d Datacard_test_simple_hut_FCNC.root -m 125  -o impacts.json
#plotImpacts.py -i impacts.json -o impacts_mutth --POI mu_tth
