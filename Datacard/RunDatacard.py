import sys, os
import glob

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--years", help = "which years to consider", type=str, default = "2017")
parser.add_argument("--inputWSDir", help = "directories with input ws", type=str, default = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_Hut_YEAR_prod_v2.1_2-March-2020/")
parser.add_argument("--signal_model_dir", help = "dir with sigfits", type=str, default="../Signal/outdir_fcnc")
parser.add_argument("--bkg_model_dir", help = "dir with background model", type=str, default="../Background")
parser.add_argument("--cats", help = "cats", type=str, default="FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCLeptonicTag_0,FCNCLeptonicTag_1")
args = parser.parse_args()

years = args.years.split(",")
for year in years:
    os.system("mkdir -p %s_workspaces_%s" % (args.tag, year))
    os.system("ln -s %s/*.root %s_workspaces_%s/" % (args.inputWSDir.replace("YEAR", year), args.tag, year))

    os.system("mkdir -p Models/signal_%s" % year)
    os.system("ln -s %s_%s/*.root Models/signal_%s/" % (args.signal_model_dir, year, year))

os.system("mkdir -p Models/background_merged")
os.system("ln -s %s/CMS-HGG_mva_13TeV_multipdf.root Models/background_merged/" % args.bkg_model_dir)

os.system("python makeDatacard.py --procs 'tth,ggh,vbf,wh,zh,bbh,thq,thw' --inputWSDir %s --cats %s --prune --years %s --mergeYears --removeNoTag --doSystematics" % (args.tag + "_workspaces", args.cats, args.years)) 
