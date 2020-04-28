import sys, os
import glob

sys.path.append("../Signal/python")
import parallel_utils

lumi = {'2016':'35.9', '2017':'41.5', '2018':'59.8'}

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--datacard", help = "path to datacard", type=str, default="../Datacard/Datacard_COUPLING.txt")
parser.add_argument("--tag", help = "tag", type=str, default = "test")
parser.add_argument("--cats", help = "categories to make plots for", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCLeptonicTag_0,FCNCLeptonicTag_1")
parser.add_argument("--couplings", help = "fcnc coupling", type=str, default="Hut,Hct")
args = parser.parse_args()

limits = { "Hut" : 0.4094, "Hct" : 0.4891 }

cats = args.cats.split(",")
if args.cats == "":
    cats = []
couplings = args.couplings.split(",")

command_list = []

for coupling in couplings:
    for cat in cats:
        command = "python makeSplusBModelPlot.py --inputWSFile FinalResults/Datacard_%s_%s_FCNC.root --cat %s --doZeroes --parameterMap r_fcnc_%s:%.6f" % (args.tag, coupling.lower(), cat, coupling.lower(), limits[coupling])
        command_list.append(command)

parallel_utils.submit_jobs(command_list, 12)
