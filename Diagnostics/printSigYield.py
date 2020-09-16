import ROOT as r
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input_tag", help = "input_tag", type=str, default="")
args = parser.parse_args()

years = { "2016" : 35900, "2017" : 41500, "2018" : 58000 }

# RooFormulaVar::shapeBkg_tth_2018_hgg_FCNCLeptonicTag_0__norm[ actualVars=(fxs_tth_13TeV,fbr_13TeV,fea_tth_2018_FCNCLeptonicTag_0_13TeV,rate_tth_2018_FCNCLeptonicTag_0_13TeV) formula="@0*@1*@2*@3" ] = 5.03217e-06

results = {}

def printYields(coupling, proc, tag):

    total_yield = 0

    for year, lumi in years.items():
        #file = r.TFile("../Signal/outdir_fcnc_%s_%s/CMS-HGG_sigfit_fcnc_%s_%s_%s.root" % (coupling, year, coupling, year, tag))
        file = r.TFile("../Plots/FinalResults/Datacard_fcnc_%s%s_FCNC.root" % (coupling.lower(), args.input_tag))
        ws = file.Get("w")
        mH = ws.var('MH')
        type = "Sig" if "fcnc" in proc else "Bkg"
        #print 'shape%s_%s_%s_hgg_%s__norm' % (type, proc, year, tag)
        norm = ws.function('shape%s_%s_%s_hgg_%s__norm' % (type, proc, year, tag))

        if not norm:
            evt_yield = 0.

        else:
            evt_yield = norm.getVal() * lumi
        #if "fcnc" in proc: #TODO do we actually need this? pretty sure it is taken care of in datacards...
        #    evt_yield *= 0.01
        #print "nEvts for mH = %.1f is: %.10f" % (m, evt_yield)
            #if m == 125.:
        print "Yield for year %s is: %.10f" % (year, evt_yield)
        total_yield += evt_yield
        results[coupling][tag][proc][year] = evt_yield
        if "fcnc" not in proc:
            results[coupling][tag]["smhiggs"][year] += evt_yield  

    print "Total yield is: %.10f" % total_yield
    results[coupling][tag][proc]["yield"] = total_yield
    if "fcnc" not in proc:
        results[coupling][tag]["smhiggs"]["yield"] += total_yield

tags = ["FCNCHadronicTag_0", "FCNCHadronicTag_1", "FCNCHadronicTag_2", "FCNCHadronicTag_3", "FCNCLeptonicTag_0", "FCNCLeptonicTag_1", "FCNCLeptonicTag_2"]
procs = ["fcnc_COUPLING", "tth","ggh","vbf","wh","zh","thq", "thw"] 
couplings = ["Hut", "Hct"]


redo = False

if redo:
    for coupling in couplings: 
        results[coupling] = {}
        for tag in tags:
            results[coupling][tag] = {}
            results[coupling][tag]["smhiggs"] = { "yield" : 0, "2016" : 0, "2017" : 0, "2018" : 0 }
            for proc in procs:
                proc = proc.replace("COUPLING", coupling.lower())
                results[coupling][tag][proc] = {}
                print coupling, tag, proc
                printYields(coupling, proc, tag)
                print "---"

    with open("yields_from_datacard.json", "w") as f_out:
        json.dump(results, f_out, indent=4, sort_keys = True)

else:
    with open("yields_from_datacard.json", "r") as f_in:
        results = json.load(f_in)

limit = { "Hut" : 0.2617, "Hct" : 0.3328 }

for coupling in couplings:
    table = ""
    table += "\\begin{center} \\Fontvi \n"
    table += "\\begin{tabular}{ l r"
    for i in range(len(procs)+3):
        table += " r "
        if i == 1 or i == 3:
            table += "|"
    table += "}\\hline \\hline \n"
    table += " & Exp. Lim. & \\multicolumn{2}{c|}{Yield} & \\multicolumn{2}{c|}{Bkg Composition} & \\multicolumn{%d}{c}{SM Higgs Composition (\\%%)} \\\\ \n" % (len(procs) -1)
    table += " & & FCNC (%s) & Tot. Bkg & Non-Res. Bkg & SM Higgs & " % coupling

    for p in procs:
        if "COUPLING" in p:
            continue
        proc = p.replace("COUPLING", coupling.lower())
        table += proc.replace("_", " ") + " &"
    table = table[:-1]
    table += " \\\\ \\hline \n"

    fcnc_scale = limit[coupling] 

    for tag in tags:
        table += tag.replace("_", " ") + "&"
        table += " & "
        table += " %.2f & & " % (results[coupling][tag]["fcnc_%s" % coupling.lower()]["yield"] * fcnc_scale)
        table += " & %.2f & " % results[coupling][tag]["smhiggs"]["yield"]
        for p in procs:
            if "fcnc" in p:
                continue
            table += "%.2f &" % (float(results[coupling][tag][p]["yield"] / results[coupling][tag]["smhiggs"]["yield"]) * 100)
        table = table[:-1]
        table += " \\\\ \n"
    table += " \\hline \\hline \n"
    table += "\\end{tabular} \n"
    table += "\\end{center}\n"
    print coupling, table







