SIGFITLEP=/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHLeptonicTag.root
SIGFITHAD=/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHHadronicTag.root
BKGFIT=/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Background/CMS-HGG_multipdf_background_test_3.root
DATACARD=/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Datacard/DATACARD_13TeV_test_3.txt

cd Plots/FinalResults

cp $SIGFITLEP CMS-HGG_13TeV_sigfit_mva_tth_TTHLeptonicTag.root 
cp $SIGFITHAD CMS-HGG_13TeV_sigfit_mva_tth_TTHHadronicTag.root 
cp $BKGFIT CMS-HGG_mva_13TeV_multipdf.root
cp $DATACARD CMS-HGG_mva_13TeV_datacard.txt

EXT=tth

./combineHarvester.py -d combineHarvesterOptions13TeV_"$EXT".dat -q 1nh --batch LSF
./combineHarvester.py --hadd combineJobs13TeV_$EXT
./makeCombinePlots.py -d combinePlotsOptions_"$EXT".dat


