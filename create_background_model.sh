INPUTPATH=/afs/cern.ch/work/s/smay
SIGFILES="$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root"
EXT="background_test_3"
PROC="tth"
TAGS="TTHHadronicTag,TTHLeptonicTag"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"
SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE"
SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward"
SCALESGLOBAL="Geant4"
#SMEARS="HighR9EE,LowR9EE,HighR9EB,LowR9EB" #DRY RUN
#SCALES="HighR9EE,LowR9EE,HighR9EB,LowR9EB"
LUMI=35.9
BATCH="LSF"
DATA=$INPUTPATH/data_jobs_916/allData.root
SIGOUTPUT="/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHHadronicTag.root,/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHLeptonicTag.root"

cd Background
./runBackgroundScripts.sh -p $PROC -f $TAGS --ext $EXT --sigFile $SIGOUTPUT --intLumi $LUMI --unblind --isData -i $DATA --batch $BATCH
