import json
import glob
import ROOT

target_ws_dir = "/home/users/smay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_v5.10_22Jan20201/" 
source_ws_dir = "/home/users/smay/ttH/FCNC_Workspaces_v2/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_v5.11_21Apr2021/"
#source_ws_dir = "/home/users/smay/ttH/FCNC_FinalFits_v3/CMSSW_10_2_13/src/flashggFinalFit/Signal/outdir_fcnc_COUPLING_YEAR/"
signal_ws_name = "ws_merged_fcnc_COUPLING_tt_st_125_YEAR.root"

target_ws = target_ws_dir + signal_ws_name
source_ws = source_ws_dir + signal_ws_name

couplings = ["Hut", "Hct"]
cats = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2".split(",")
years = ["2016", "2017", "2018"]

corrs = {}

for coupling in couplings:
    corrs[coupling] = {}
    for year in years:
        corrs[coupling][year] = {}
        proc = "fcnc_%s" % coupling.lower()
        target = ROOT.TFile.Open(target_ws.replace("COUPLING", coupling).replace("YEAR", year).replace("PROC", proc))
        t_ws = target.Get("tagsDumper/cms_hgg_13TeV")

        source = ROOT.TFile.Open(source_ws.replace("COUPLING", coupling).replace("YEAR", year).replace("PROC", proc))
        s_ws = source.Get("tagsDumper/cms_hgg_13TeV")
        for cat in cats:
            no_pu_yield = t_ws.data("fcnc_%s_125_13TeV_%s" % (coupling.lower(), cat)).sumEntries()
            yes_pu_yield = s_ws.data("fcnc_%s_125_13TeV_%s" % (coupling.lower(), cat)).sumEntries()

            corrs[coupling][year][cat] = {
                "yield_no_pu" : no_pu_yield,
                "yield_yes_pu" : yes_pu_yield,
                "corr" : yes_pu_yield / no_pu_yield
            }
            print(corrs[coupling][year][cat])

with open("theory_uncertainties/pu_corr.json", "w") as f_out:
    json.dump(corrs, f_out, sort_keys=True, indent=4)
