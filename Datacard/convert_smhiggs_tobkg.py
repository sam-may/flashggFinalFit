import os, sys
import json


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "input ws to modify", type=str)
parser.add_argument('--fcnc_unc', default='theory_uncertainties/fcnc_individual_uncs.json', type=str, help="json with per-year, per-category uncertainties for fcnc normalization")
args = parser.parse_args()

with open(args.fcnc_unc, "r") as f_in:
    fcnc_unc = json.load(f_in)

if "Tag" in args.input:
    cats = [args.input.split("_")[2] + "_" +  args.input.split("_")[3]]
else:
    #cats = ["all"]
    cats = ["FCNCHadronicTag_0","FCNCHadronicTag_1","FCNCHadronicTag_2","FCNCHadronicTag_3","FCNCLeptonicTag_0","FCNCLeptonicTag_1","FCNCLeptonicTag_2"]

if "Hut" in args.input:
    coupling = "Hut"
elif "Hct" in args.input:
    coupling = "Hct"

years = ["2016", "2017", "2018"]
#procs = ['tth','ggh','wh','zh','thq','thw','fcnc_%s' % coupling.lower()]

with open(args.input, "r") as f_in:
    lines = f_in.readlines()
    idx = []
    for i in range(len(lines)):
        line = lines[i]
        if not "process" in line:
            continue
        else:
            procs = line.split()
            for i in range(len(procs)):
                proc = procs[i]
                if proc == "process" or "fcnc" in proc or "bkg_mass" in proc or "data" in proc:
                    continue
                else:
                    idx.append(i)
            break

    for i in range(len(lines)):
        line = lines[i]
        if not "process" in line:
            continue
        if "hgg" in line:
            continue
        old_idx = line.split()
        lines[i] = ""
        for j in range(len(old_idx)):
            if j in idx:
                if float(old_idx[j]) == 0:
                    lines[i] += "999"
                else:
                    lines[i] += old_idx[j].replace("-","")
            else:
                lines[i] += old_idx[j]
            lines[i] += "    "
        lines[i] += "\n"

    procs = sorted(set(procs), key = procs.index)
    print procs

    for i in range(len(lines)):
        line = lines[i]

        if "norm_fcnc" not in line:
            continue
        if coupling.lower() not in line:
            continue

        lines[i] = "norm_fcnc_%s                                       lnN   " % coupling.lower()
        for cat in cats:
            #for year in years:
            for proc in procs:
                if proc == "process":
                    continue
                if proc == "bkg_mass":
                    lines[i] += "-"
                    lines[i] += "    "
                    continue
                year = proc.split("_")[1]
                if "fcnc" in proc:
                    year = proc.split("_")[2]
                    #print cat, year, proc, fcnc_unc[coupling][year][cat]
                    #lines[i] += "%.3f" % (1.085)
                    lines[i] += "%.3f" % fcnc_unc[coupling][year][cat] 
                else:
                    print cat, year, proc
                    lines[i] += "-"
                lines[i] += "    "
        lines[i] += "\n"


with open(args.input.replace(".txt", "_mod.txt"), "w") as f_out:
    for line in lines:
        f_out.write(line)

