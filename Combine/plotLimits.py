import os, sys
import ROOT
import json

import tdrStyle
tdrStyle.setTDRStyle()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag", type=str, default = "test")
parser.add_argument("--cats", help = "subcategories to also run limits for", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCLeptonicTag_0,FCNCLeptonicTag_1")
parser.add_argument("--couplings", help = "fcnc coupling", type=str, default="Hut,Hct")
args = parser.parse_args()

cats = args.cats.split(",")
cats_full = cats
cats_full.append("All_Categories")
couplings = args.couplings.split(",")

results = {}
for coupling in couplings:
    results[coupling] = {}
    for cat in cats_full:
        results[coupling][cat] = {}
        cat_string = "" if cat == "All_Categories" else "_%s" % cat
        results[coupling][cat]["input"] = "../Plots/FinalResults/limits_%s_%s%s.txt" % (args.tag, coupling.lower(), cat_string)
        with open (results[coupling][cat]["input"], "r") as f_in:
            lines = f_in.readlines()
            for line in lines:
                if not "Expected" in line:
                    continue
                else:
                    if "2.5" in line: results[coupling][cat]["-2sigma"] = line.split()[-1]
                    if "16.0" in line: results[coupling][cat]["-1sigma"] = line.split()[-1]
                    if "50.0" in line: results[coupling][cat]["exp"] = line.split()[-1]
                    if "84.0" in line: results[coupling][cat]["+1sigma"] = line.split()[-1]
                    if "97.5" in line: results[coupling][cat]["+2sigma"] = line.split()[-1]

with open("plot_results_%s.json" % args.tag, "w") as f_out:
    json.dump(results, f_out, sort_keys=True, indent=4)

#for coupling in couplings:
#    c1 = ROOT.TCanvas("c1", "c1", 800, 800)
#    h = ROOT.TH1F("h", "h", 5, 1, 5)
