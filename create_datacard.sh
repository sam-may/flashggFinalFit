INPUTPATH=/afs/cern.ch/work/s/smay
EXT="datacard_test_3"
PROC="tth"
TAGS="TTHHadronicTag,TTHLeptonicTag"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"
SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE"
SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward"
SCALESGLOBAL="Geant4"
LUMI=35.9
MASSLIST="120,123,124,125,126,127,130"
BATCH="LSF"
SIGOUTPUT="/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHHadronicTag.root,/afs/cern.ch/user/s/smay/public/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_signal_test_3/CMS-HGG_sigfit_signal_test_3_tth_TTHLeptonicTag.root"
DATACARD="DATACARD_13TeV_test_3.txt"
SIGPATH=/eos/cms/store/group/phys_higgs/cmshgg/analyzed/ichep2016/flashgg-workspaces
SIGFILES=$SIGPATH/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root 

cd Datacard
./makeParametricModelDatacardFLASHgg.py -i $SIGFILES -o $DATACARD -p $PROC -c $TAGS --photonCatScales $SCALES --photonCatSmears $SMEARS --isMultiPdf --mass 125 --intLumi $LUMI
