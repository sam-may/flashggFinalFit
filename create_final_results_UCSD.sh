SIGFITLEP=CMS-HGG_sigfit_tth_TTHLeptonicTag.root
SIGFITHAD=CMS-HGG_sigfit_tth_TTHHadronicTag.root
BKGFIT=CMS-HGG_multipdf_tth.root
DATACARD=DATACARD_13TeV_tth.txt

cd Plots/FinalResults

cp $SIGFITLEP CMS-HGG_13TeV_sigfit_mva_tth_TTHLeptonicTag.root 
cp $SIGFITLEP CMS-HGG_sigfit_mva_tth_TTHLeptonicTag.root # readme says file should be named a la previous line, but some parts of script try to access file with this name
cp $SIGFITHAD CMS-HGG_13TeV_sigfit_mva_tth_TTHHadronicTag.root
cp $SIGFITHAD CMS-HGG_sigfit_mva_tth_TTHHadronicTag.root # readme says file should be named a la previous line, but some parts of script try to access file with this name
cp $BKGFIT CMS-HGG_mva_13TeV_multipdf.root
cp $DATACARD CMS-HGG_mva_13TeV_datacard.txt

EXT=tth

#./combineHarvester.py -d combineHarvesterOptions13TeV_"$EXT".dat --runLocal --parallel
./combineHarvester.py --hadd combineJobs13TeV_$EXT
./makeCombinePlots.py -d combinePlotsOptions_"$EXT".dat
