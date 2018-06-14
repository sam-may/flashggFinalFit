#!/bin/bash

#DATA="/afs/cern.ch/work/j/jolangfo/public/FinalFits/ForSam/ws_ttHOnlyTest/allData.root"

#DATA="/afs/cern.ch/work/s/smay/public/CMSSW_8_0_28/src/flashgg/Systematics/test/data_jobs_916/allData.root"
#DATA="/afs/cern.ch/work/s/smay/public/allData.root"
#DATA="/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/ws_flashgg_std/allData.root"
DIR="ws_ttHOnlyTest_v1"
DATA="/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/$DIR/allData.root"

EXT="ttHOnly"
echo "Ext is $EXT"
PROCS="GG2H,VBF,TTH,QQ2HLL,QQ2HLNU,WH2HQQ,ZH2HQQ,testBBH,testTHQ,testTHW"
echo "Procs are $PROCS"
CATS="TTHHadronicTag,TTHLeptonicTag"
echo "Cats are $CATS"
INTLUMI=35.9
echo "Intlumi is $INTLUMI"
BATCH="LSF"
echo "Batch is $BATCH"
QUEUE="1nh"
echo "Batch is $QUEUE"

#SIGFILE="/vols/build/cms/jl2117/ttHOnlyTest/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_${EXT}/CMS-HGG_sigfit_${EXT}.root"
#SIGFILE="/afs/cern.ch/work/s/smay/public/ttH_only_flashggFinalFit/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_${EXT}/CMS-HGG_sigfit_${EXT}.root"
SIGFILE="/home/users/sjmay/ttH/FinalFits/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_${EXT}/CMS-HGG_sigfit_${EXT}.root"

echo "./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --unblind"
./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --unblind
#echo "./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --fTestOnly"
#./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --fTestOnly
#echo "./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --bkgPlotsOnly --unblind"
#./runBackgroundScripts.sh -i $DATA -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --sigFile $SIGFILE --isData --bkgPlotsOnly --unblind
