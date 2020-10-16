import sys, os
import glob

sys.path.append("../Signal/python/")
import parallel_utils

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--years", help = "which years to consider", type=str, default = "2016,2017,2018")
parser.add_argument("--inputWSDir", help = "directories with input ws", type=str, default = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_v5.2_5-Oct-2020/")
parser.add_argument("--signal_model_dir", help = "dir with sigfits", type=str, default="../Signal/outdir_fcnc_COUPLING")
parser.add_argument("--bkg_model_dir", help = "dir with background model", type=str, default="../Background")
parser.add_argument("--cats", help = "cats", type=str, default="FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2")
parser.add_argument("--couplings", help = "which fcnc couplings to consider", type=str, default="Hut,Hct")
parser.add_argument("--update_inputs", help = "copy over workspaces", action="store_true", default=False)
parser.add_argument('--tth_unc', default=0.4, type=float, help='Additional systematic uncertainty to apply on ttH')
parser.add_argument('--tth_scale', default=1.0, type=float, help='factor by which to scale ttH normalization')
parser.add_argument('--fcnc_unc', default='theory_uncertainties/fcnc_individual_uncs.json', type=str, help="json with per-year, per-category uncertainties for fcnc normalization")
args = parser.parse_args()

command_list = []
command_list2 = []
command_list3 = []

years = args.years.split(",")
couplings = args.couplings.split(",")
for coupling in couplings:

    if args.update_inputs:
        for year in years:
            os.system("mkdir -p %s_%s_workspaces_%s" % (args.tag, coupling, year))
            os.system("cp %s/*.root %s_%s_workspaces_%s/" % (args.inputWSDir.replace("YEAR", year).replace("COUPLING", coupling), "fcnc", coupling, year))

            os.system("mkdir -p ../Plots/FinalResults/Models_%s/signal_%s" % (coupling, year))
            files = glob.glob(args.signal_model_dir.replace("COUPLING", coupling) + "_" + year + "/*.root")
            for file in files:
                print file
                os.system("cp %s %s" % (file, "../Plots/FinalResults/Models_" + coupling + "/signal_" + year + "/" + file.split("/")[-1].replace("sigfit_fcnc_%s" % coupling, "sigfit_mva").replace("_" + year, "")))


    os.system("mkdir -p ../Plots/FinalResults/Models_%s/background_merged" % coupling)
    os.system("cp %s/CMS-HGG_multipdf_fcnc_%s.root ../Plots/FinalResults/Models_%s/background_merged/CMS-HGG_mva_13TeV_multipdf.root" % (args.bkg_model_dir, coupling, coupling))

    command_list.append("python makeDatacard.py --fcnc_unc %s --tth_unc %.6f --tth_scale %.6f --procs 'tth,ggh,wh,zh,thq,thw,fcnc_%s' --inputWSDir %s --cats %s --years %s --mergeYears --removeNoTag --doSystematics --modelWSDir %s --output %s" % (args.fcnc_unc, args.tth_unc, args.tth_scale, coupling.lower(), "fcnc" + "_" + coupling + "_workspaces", args.cats, args.years, "Models_" + coupling, 'Datacard_' + coupling + "_" + args.tag + '.txt'))
    command_list2.append("python convert_smhiggs_tobkg.py --input %s --fcnc_unc %s" % ('Datacard_' + coupling + "_" + args.tag + '.txt', args.fcnc_unc))
    command_list3.append("python cleanDatacard.py --datacard %s --removeDoubleSided --verbose" % ('Datacard_' + coupling + "_" + args.tag + '_mod.txt'))
    for cat in args.cats.split(","):
        command_list.append("python makeDatacard.py --fcnc_unc %s --tth_unc %.6f --tth_scale %.6f --procs 'tth,ggh,wh,zh,thq,thw,fcnc_%s' --inputWSDir %s --cats %s --years %s --mergeYears --removeNoTag --doSystematics --modelWSDir %s --output %s" % (args.fcnc_unc, args.tth_unc, args.tth_scale, coupling.lower(), "fcnc" + "_" + coupling + "_workspaces", cat, args.years, "Models_" + coupling, 'Datacard_' + coupling + "_" + cat + "_" + args.tag + '.txt'))
        command_list2.append("python convert_smhiggs_tobkg.py --input %s --fcnc_unc %s" % ('Datacard_' + coupling + "_" + cat + "_" + args.tag + '.txt', args.fcnc_unc))
        command_list3.append("python cleanDatacard.py --datacard %s --removeDoubleSided --verbose" % ('Datacard_' + coupling + "_" + cat + "_" + args.tag + '_mod.txt'))

parallel_utils.submit_jobs(command_list, 6)
parallel_utils.submit_jobs(command_list2, 12)
parallel_utils.submit_jobs(command_list3, 12)
