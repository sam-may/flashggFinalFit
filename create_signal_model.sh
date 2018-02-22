INPUTPATH=/afs/cern.ch/work/s/smay
SIGFILES="$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8.root,$INPUTPATH/tth_sig_jobs_916/output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root"
EXT="signal_test_3"
PROC="tth"
TAGS="TTHHadronicTag,TTHLeptonicTag"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"
SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE"
SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward"
SCALESGLOBAL="NonLinearity,Geant4,LightYield,Absolute"
LUMI=35.9
MASSLIST="120,123,124,125,126,127,130"
BATCH="LSF"
SIMULATENOUSMASSPOINTFITTING=0
USEDCBP1G=0

cd Signal
./runSignalScripts.sh -i $SIGFILES -p $PROC -f $TAGS --ext $EXT --intLumi $LUMI --smears $SMEARS --scales $SCALES --scalesCorr $SCALESCORR --scalesGlobal $SCALESGLOBAL --massList $MASSLIST --useDCB_1G $USEDCBP1G --useSSF $SIMULATENOUSMASSPOINTFITTING --batch $BATCH
