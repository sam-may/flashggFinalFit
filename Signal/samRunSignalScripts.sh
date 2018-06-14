#!/bin/bash

DIR="ws_ttHOnlyTest_v1"
FILE="/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_TTH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/testBBH.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/testTHQ.root,/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/testTHW.root"

EXT="ttHOnly"
echo "Ext is $EXT"
PROCS="GG2H,VBF,TTH,QQ2HLL,QQ2HLNU,WH2HQQ,ZH2HQQ,testBBH,testTHQ,testTHW"
echo "Procs are $PROCS"
#CATS="UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,VBFTag_0,VBFTag_1,VBFTag_2,TTHHadronicTag,TTHLeptonicTag,ZHLeptonicTag,WHLeptonicTag,VHLeptonicLooseTag,VHHadronicTag,VHMetTag"
##ttH Only categories
CATS="TTHHadronicTag,TTHLeptonicTag"
echo "Cats are $CATS"
INTLUMI=35.9
echo "Intlumi is $INTLUMI"
BATCH=""
echo "Batch is $BATCH"
QUEUE="1nh"
echo "Batch is $QUEUE"
BSWIDTH=3.400000
echo "Bswidth is $BSWIDTH"
NBINS=320
echo "Nbins is $NBINS"

SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"
SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"
SCALESGLOBAL="NonLinearity:UntaggedTag_0:2,Geant4"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"

MASSLIST="120,123,124,125,126,127,130"
#MASSLIST="120,125,130"
MLOW=120
MHIGH=130
echo "Masslist is $MASSLIST"

echo "cp ../newConfig_ttHOnly.dat dat/"
cp ../newConfig_ttHOnly.dat dat/
echo "cp ../newConfig_ttHOnly.dat outdir_$EXT/"
cp ../newConfig_ttHOnly.dat outdir_$EXT/

#cd /vols/build/cms/es811/FreshStart/Pass6/CMSSW_7_4_7/src/flashggFinalFit/Signal
#eval `scramv1 runtime -sh`
#./runSignalScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --massList $MASSLIST --bs $BSWIDTH \
#                        --smears $SMEARS --scales $SCALES --scalesCorr $SCALESCORR --scalesGlobal $SCALESGLOBAL --useSSF 1 --useDCB_1G 0 --calcPhoSystOnly
./runSignalScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --massList $MASSLIST --bs $BSWIDTH \
                        --smears $SMEARS --scales $SCALES --scalesCorr $SCALESCORR --scalesGlobal $SCALESGLOBAL --useSSF 1 --useDCB_1G 0
