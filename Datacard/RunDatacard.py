import sys, os
import glob

sys.path.append("../Signal/python/")
import parallel_utils

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--years", help = "which years to consider", type=str, default = "2016,2017,2018")
parser.add_argument("--inputWSDir", help = "directories with input ws", type=str, default = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_prod_v2.1_2-March-2020/")
parser.add_argument("--signal_model_dir", help = "dir with sigfits", type=str, default="../Signal/outdir_fcnc_COUPLING")
parser.add_argument("--bkg_model_dir", help = "dir with background model", type=str, default="../Background")
parser.add_argument("--cats", help = "cats", type=str, default="FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCLeptonicTag_0,FCNCLeptonicTag_1")
parser.add_argument("--couplings", help = "which fcnc couplings to consider", type=str, default="Hut,Hct")
args = parser.parse_args()

command_list = []

years = args.years.split(",")
couplings = args.couplings.split(",")
for coupling in couplings:
    for year in years:
        os.system("mkdir -p %s_%s_workspaces_%s" % (args.tag, coupling, year))
        os.system("cp %s/*.root %s_%s_workspaces_%s/" % (args.inputWSDir.replace("YEAR", year).replace("COUPLING", coupling), args.tag, coupling, year))

        os.system("mkdir -p ../Plots/FinalResults/Models_%s/signal_%s" % (coupling, year))
        files = glob.glob(args.signal_model_dir.replace("COUPLING", coupling) + "_" + year + "/*.root")
        for file in files:
            print file
            os.system("cp %s %s" % (file, "../Plots/FinalResults/Models_" + coupling + "/signal_" + year + "/" + file.split("/")[-1].replace("sigfit_fcnc_%s" % coupling, "sigfit_mva").replace("_" + year, "")))

    #os.system("mkdir -p Models/background_merged")
    #os.system("cp %s/CMS-HGG_mva_13TeV_multipdf.root Models/background_merged/" % args.bkg_model_dir)


    os.system("mkdir -p ../Plots/FinalResults/Models_%s/background_merged" % coupling)
    os.system("cp %s/CMS-HGG_multipdf_fcnc_%s.root ../Plots/FinalResults/Models_%s/background_merged/CMS-HGG_mva_13TeV_multipdf.root" % (args.bkg_model_dir, coupling, coupling))

    command_list.append("python makeDatacard.py --procs 'tth,ggh,wh,zh,thq,thw,bbh,fcnc_%s' --inputWSDir %s --cats %s --years %s --mergeYears --removeNoTag --doSystematics --modelWSDir %s --output %s" % (coupling.lower(), args.tag + "_" + coupling + "_workspaces", args.cats, args.years, "Models_" + coupling, 'Datacard_' + coupling + '.txt'))
    for cat in args.cats.split(","):
        command_list.append("python makeDatacard.py --procs 'tth,ggh,wh,zh,thq,thw,bbh,fcnc_%s' --inputWSDir %s --cats %s --years %s --mergeYears --removeNoTag --doSystematics --modelWSDir %s --output %s" % (coupling.lower(), args.tag + "_" + coupling + "_workspaces", cat, args.years, "Models_" + coupling, 'Datacard_' + coupling + "_" + cat + '.txt'))

parallel_utils.submit_jobs(command_list, 12)

