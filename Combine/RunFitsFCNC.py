import sys, os
import glob

lumi = {'2016':'35.9', '2017':'41.5', '2018':'59.8'}

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--datacard", help = "path to datacard", type=str, default="../Datacard/Datacard_dummy1.txt")
parser.add_argument("--tag", help = "tag", type=str, default = "test")
args = parser.parse_args()

datacard = args.datacard.split("/")[-1]
datacard_dir = args.datacard.replace(datacard, "")

#os.chdir(datacard_dir)
os.system("cp %s %s" % (args.datacard, "../Plots/FinalResults/"))
os.chdir("../Plots/FinalResults/")

datacard_ws = "Datacard%s_mu_ttH.root" % args.tag

command = "text2workspace.py %s -o %s -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 higgsMassRange=122,128" % (datacard, datacard_ws)
command += ' --PO "map=.*/tth.*:r_ttH[1,0,3]" '

print command
os.system(command)

os.system("cp %s %s" % (datacard_ws, "../../Combine/"))
os.chdir("../../Combine")

command = "python runFits.py --mode 'mu_ttH' --ext %s" % args.tag

print command
os.system(command)

command = "python collectFits.py --mode 'mu_ttH' --ext %s" % args.tag

print command
os.system(command)
