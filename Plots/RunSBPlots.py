import sys, os
import glob

sys.path.append("../Signal/python")
import parallel_utils

lumi = {'2016':'35.9', '2017':'41.5', '2018':'59.8'}

import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("--datacard", help = "path to datacard", type=str, default="../Datacard/Datacard_COUPLING_tth_scale1_unc40.txt")
parser.add_argument("--tag", help = "tag", type=str, default = "test")
parser.add_argument("--cats", help = "categories to make plots for", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2")
parser.add_argument("--mH", help = "value to fix Higgs mass to", type=float, default=125.38)
parser.add_argument("--couplings", help = "fcnc coupling", type=str, default="Hut,Hct")
parser.add_argument("--doBands", help = "add 1/2 sigma error bands", action="store_true")
parser.add_argument("--unblind", help = "unblind data", action="store_true")
args = parser.parse_args()

#limits = { "Hut" : 0.4094, "Hct" : 0.4891 }
#limits = { "Hut" : 0.2617, "Hct" : 0.3328 }
#limits = { "Hut" : 0.2867, "Hct" : 0.3422 } # v5.1_18Sep2020
#limits = { "Hut" : 0.2945, "Hct" : 0.3469 } # v5.2_5Oct2020
#limits = { "Hut" : 0.2656, "Hct" : 0.3234 } # v5.3_26Oct2020_fixtH
#limits = { "Hut" : 0.2336, "Hct" : 0.2781 } # v5.8_7/8Dec2020
#limits = { "Hut" : 0.2266, "Hct" : 0.2742 } # v5.10_27Jan2021
limits = { "Hut" : 0.2236, "Hct" : 0.3662} # unblinded v5.10_9Feb2021_unblind_fixMH

cats = args.cats.split(",")
if args.cats == "":
    cats = []
couplings = args.couplings.split(",")

command_list = []

for coupling in couplings:
    #command = "python makeSplusBModelPlot.py --inputWSFile FinalResults/Datacard_%s_%s_FCNC.root --cat %s --doZeroes --parameterMap r_fcnc_%s:%.6f --mass %.6f %s" % (args.tag, coupling.lower(), "all", coupling.lower(), limits[coupling], args.mH, "--unblind" if args.unblind else "")
    command = "python makeSplusBModelPlot.py --inputWSFile FinalResults/Datacard_fcnc_%s%s_FCNC.root --cat %s --doZeroes --parameterMap r_fcnc_%s:%.6f --mass %.6f %s %s" % (coupling.lower(), args.tag, "all", coupling.lower(), limits[coupling], args.mH, "--unblind" if args.unblind else "", "--doBands" if args.doBands else "")
    command_list.append(command)

parallel_utils.submit_jobs(command_list, 12)
