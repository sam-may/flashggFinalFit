import sys, os
import glob

sys.path.append("../Signal/python")
import parallel_utils

lumi = {'2016':'35.9', '2017':'41.5', '2018':'59.8'}

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--datacard", help = "path to datacard", type=str, default="../Datacard/Datacard_COUPLING_TAG_mod.txt")
parser.add_argument("--tag", help = "tag", type=str, default = "fcnc")
parser.add_argument("--cats", help = "subcategories to also run limits for", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2")
parser.add_argument("--couplings", help = "fcnc coupling", type=str, default="Hut,Hct")
args = parser.parse_args()


cats = args.cats.split(",")
if args.cats == "":
    cats = []
couplings = args.couplings.split(",")

for coupling in couplings:
    os.system("cp %s %s" % (((args.datacard.replace("COUPLING", coupling)).replace("TAG", args.tag)).replace(".txt", "*"), "../Plots/FinalResults/"))

command_list = []

for coupling in couplings:
    datacard = (args.datacard.split("/")[-1].replace("COUPLING", coupling)).replace("TAG", args.tag)
    datacard_dir = "../../Datacard/" 
    print datacard_dir, datacard

    datacard_ws = "Datacard_%s_FCNC.root" % (args.tag + "_" + coupling.lower())
    command = "text2workspace.py %s -o %s -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 higgsMassRange=122,128" % (datacard_dir + datacard, datacard_ws)
    #command = "text2workspace.py %s -o %s -m 125 " % (datacard, datacard_ws)
    command += ' --PO "map=.*/fcnc.*:r_fcnc_%s[0,-2,2]" ' % coupling.lower()
    for proc in ["tth", "ggh", "wh", "zh", "thq", "thw", "vbf"]:
        command += ' --PO "map=.*/%s.*:1" ' % (proc) 
    command_list.append(command)

    for cat in cats:
        datacard = args.datacard.split("/")[-1].replace("COUPLING", coupling).replace("TAG", args.tag).replace("Datacard_%s" % coupling, "Datacard_%s_%s" % (coupling, cat))
        datacard_ws = "Datacard_%s_%s_FCNC.root" % (args.tag + "_" + coupling.lower(), cat)
        command = "text2workspace.py %s -o %s -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 higgsMassRange=122,128" % (datacard_dir + datacard, datacard_ws)
        #command = "text2workspace.py %s -o %s -m 125 " % (datacard, datacard_ws)
        command += ' --PO "map=.*/fcnc.*:r_fcnc_%s[0,-2,2]" ' % coupling.lower()
        for proc in ["tth", "ggh", "wh", "zh", "thq", "thw", "vbf"]:
            command += ' --PO "map=.*/%s.*:1" ' % (proc)
        command_list.append(command)

os.chdir("../Plots/FinalResults/")
parallel_utils.submit_jobs(command_list, 12)
command_list = []

cats_full = cats
cats_full.append("")
for coupling in couplings:
    for cat in cats_full:
        cat_string = "" if cat == "" else "_" + cat
        print "cat_string", cat_string
        command = "combine -M AsymptoticLimits -m 125 --run blind Datacard_%s_%s%s_FCNC.root -n %s" % (args.tag, coupling.lower(), cat_string, "limit" + cat_string)
        command_statonly = command + " --freezeParameters allConstrainedNuisances"

        command += " > limits_%s_%s%s.txt" % (args.tag, coupling.lower(), cat_string)
        command_statonly += " > limits_%s_%s%s_statonly.txt" % (args.tag, coupling.lower(), cat_string)

        command_list.append(command)
        command_list.append(command_statonly)

parallel_utils.submit_jobs(command_list, 12)
