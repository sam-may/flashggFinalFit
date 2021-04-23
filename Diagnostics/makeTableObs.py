import os, sys
import glob
import json

import ROOT

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--years", help = "which years to consider", type=str, default = "2016,2017,2018")
parser.add_argument("--couplings", help = "which couplings to run for", type=str, default = "Hut,Hct")
parser.add_argument("--procs", help = "which processes to consider", type=str, default = "fcnc_COUPLING,tth,ggh,vbf,wh,zh,thq,thw,bbh")
parser.add_argument("--cats", help = "which categories to consider", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2")
parser.add_argument("--limits", help = "json with exp limits", type=str, default = "../Combine/plot_results_fcncv5.10_9Feb2021_unblind_fixMH.json")
args = parser.parse_args()

signal_ws_dir = "../Signal/outdir_fcnc_COUPLING_YEAR/"
signal_ws_name = "CMS-HGG_sigfit_fcnc_COUPLING_YEAR_PROC_CAT.root"
signal_ws = signal_ws_dir + signal_ws_name

datacard_ws = "../Plots/FinalResults/Datacard_fcnc_COUPLINGTAG_CAT_FCNC.root"

couplings = args.couplings.split(",")
years = args.years.split(",")
procs = args.procs.split(",")
cats = args.cats.split(",")

#limit = { "Hut" : 0.4094, "Hct" : 0.4891 }
#limit = { "Hut" : 0.2617, "Hct" : 0.3328 } 
#limit = { "Hut" : 0.2867, "Hct" : 0.3422 } # v5.1_18Sep2020
#limit = { "Hut" : 0.2945, "Hct" : 0.3469 } # v5.2_5Oct2020
#limit = { "Hut" : 0.2656, "Hct" : 0.3234 } # v5.3_26Oct2020_fixtH
#limit = { "Hut" : 0.2625, "Hct" : 0.3234 } # fcncv5.3_13Nov2020_mH125p38
#limit = { "Hut" : 0.2336, "Hct" : 0.2781 } # v5.8_7/8Dec2020
limit = { "Hut" : 0.2266, "Hct" : 0.2742 } # v5.10_27Jan2021

with open(args.limits, "r") as f_in:
    exp_lim = json.load(f_in)

yields = {}
for coupling in couplings:
    yields[coupling] = {}
    for cat in cats:
        yields[coupling][cat] = {}
        for p in procs:
            proc = p.replace("COUPLING", coupling.lower())
            yields[coupling][cat][proc] = { "yield" : 0 }
            for year in years:
                yields[coupling][cat][proc][year] = 0
        yields[coupling][cat]["smhiggs"] = { "yield" : 0 }
        for year in years:
            yields[coupling][cat]["smhiggs"][year] = 0
        yields[coupling][cat]["non_resonant_bkg"] = { "yield" : 0 }
        yields[coupling][cat]["total_bkg"] = { "yield" : 0 }
        yields[coupling][cat]["obs_data"] = { "yield" : 0 }

for coupling in couplings:
    for cat in cats:
        for p in procs:
            proc = p.replace("COUPLING", coupling.lower())
            proc_yield = 0
            for year in years:
                ws_file = ROOT.TFile.Open(signal_ws.replace("COUPLING", coupling).replace("YEAR", year).replace("PROC", proc).replace("CAT", cat))
                ws = ws_file.Get("wsig_13TeV")
                y = ws.data("sig_%s_mass_m125_%s" % (proc, cat)).sumEntries()
                #n_entry = ws.data("sig_%s_mass_m125_%s" % (proc, cat)).numEntries()
                #if n_entry <= 0:
                #    n_entry = 1

                #yerr_low_bound = y * (float(n_entry))**(-0.5)
                

                pdf = ws.pdf("")

                if "fcnc" in proc:
                    y *= limit[coupling]

                yields[coupling][cat][proc]["yield"] += y
                yields[coupling][cat][proc][year] += y

                #print coupling, cat, p, y, "+/-", yerr_low_bound, "(%.2f percent error)" % (yerr_low_bound*100./y)

                if not "fcnc" in proc:
                    yields[coupling][cat]["smhiggs"]["yield"] += y
                    yields[coupling][cat]["smhiggs"][year] += y
                    yields[coupling][cat]["total_bkg"]["yield"] += y

def get_bkg_yield(file, m_low, m_high):
    bkg_yield = 0
    with open(file, "r") as f_in:
        lines = f_in.readlines()
        for line in lines:
            if not "[INFO] mgg:" in line:
                continue
            mass = float(line.split()[2])
            if mass >= m_low and mass < m_high:
                bkg_yield += float(line.split()[4])
    return bkg_yield

bkg_ws = "../Background/CMS-HGG_multipdf_fcnc_COUPLING.root"
bkg_txt = "../Background/bkg_yield_COUPLING_CAT.txt"
for coupling in couplings:
    for cat in cats:
        #ws_file = ROOT.TFile.Open(bkg_ws.replace("COUPLING", coupling))
        #ws = ws_file.Get("multipdf")
        #y = ws.data("roohist_data_mass_%s" % cat).sumEntries()
        y = get_bkg_yield(bkg_txt.replace("COUPLING", coupling.lower()).replace("CAT",cat), 122, 128)
        yields[coupling][cat]["non_resonant_bkg"]["yield"] += y
        yields[coupling][cat]["total_bkg"]["yield"] += y

for coupling in couplings:
    for cat in cats:
        ws_name = datacard_ws.replace("COUPLING", coupling.lower()).replace("TAG", "v5.10_9Feb2021_unblind").replace("CAT", cat)
        ws_file = ROOT.TFile.Open(ws_name)
        ws = ws_file.Get("w")
        dataset = ws.data("data_obs")
        print dataset.sumEntries()
        xvar = ws.var("CMS_hgg_mass")
        xvar_arglist, xvar_argset = ROOT.RooArgList(xvar), ROOT.RooArgSet(xvar)
        h_data = xvar.createHistogram("h_data_%s" % cat, ROOT.RooFit.Binning(80))
        h_data.SetBinErrorOption(ROOT.TH1.kPoisson)
        dataset.fillHistogram(h_data, xvar_arglist)
        for i in range(1, h_data.GetNbinsX() + 1):
            bin_center = h_data.GetBinCenter(i)
            if bin_center < 122. or bin_center > 128:
                continue
            yields[coupling][cat]["obs_data"]["yield"] += h_data.GetBinContent(i)

import json
with open("yields.json", "w") as f_out:
    json.dump(yields, f_out, sort_keys=True, indent=4)

# Make table
for coupling in couplings:
    table = ""
    table += "\\begin{center} \\Fontvi \n"
    table += "\\begin{tabular}{ l r r r r } \\hline \\hline \n"
    table += " & Exp. Lim. & Obs. Lim. & Exp. Yield & Obs. Yield \\\\ \\hline \n"
    for cat in cats:
        table += cat.replace("_", " ") + "&"
        table += " %.3f & " % exp_lim[coupling][cat]["exp"]
        table += " %.3f & " % exp_lim[coupling][cat]["obs"]
        total_bkg = yields[coupling][cat]["total_bkg"]["yield"]
        table += " %.2f &" % total_bkg
        obs_data = yields[coupling][cat]["obs_data"]["yield"]
        table += " %.2f \\\\ \n" % obs_data
    table += " \\hline \\hline \n"
    table += "\\end{tabular} \n"
    table += "\\end{center}\n"
    print coupling, table

