import sys, os
import glob

import ROOT

import json
import math

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input_ws_dir", help = "directory with input workspaces", type=str, default="/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_v5.2_5-Oct-2020")
args = parser.parse_args()

tt_unc = 0.034
st_unc = 0.300

def calculate_total_unc(yield_tt, yield_st, verbose=False):
    raw_unc = ((tt_unc*yield_tt)**2 + (st_unc*yield_st)**2)**(0.5)
    unc = raw_unc / (yield_tt + yield_st)
    if verbose:
        print "With a tt yield of %.2f and a st yield of %.2f" % (yield_tt, yield_st)
        print "The total tt unc is %.2f and the total st unc is %.2f" % ((tt_unc*yield_tt)**2, (st_unc*yield_st)**2)
        print "Giving a total unc of %.2f" % raw_unc
        print "And a fractional unc of %.3f" % unc
    return 1 + unc

years = ["2016", "2017", "2018"]
couplings = ["Hut", "Hct"]
cats = ["FCNCLeptonicTag_0", "FCNCLeptonicTag_1", "FCNCLeptonicTag_2", "FCNCHadronicTag_0", "FCNCHadronicTag_1", "FCNCHadronicTag_2", "FCNCHadronicTag_3"]

uncertainties = {}

for coupling in couplings:
    uncertainties[coupling] = {}
    for year in years:
        uncertainties[coupling][year] = {}
        ws_file_tt = ROOT.TFile.Open(args.input_ws_dir.replace("COUPLING", coupling).replace("YEAR", year) + "/ws_merged_fcnc_%s_tt_%s.root" % (coupling, year))
        ws_tt = ws_file_tt.Get("tagsDumper/cms_hgg_13TeV")
        ws_file_st = ROOT.TFile.Open(args.input_ws_dir.replace("COUPLING", coupling).replace("YEAR", year) + "/ws_merged_fcnc_%s_st_%s.root" % (coupling, year))
        ws_st = ws_file_st.Get("tagsDumper/cms_hgg_13TeV") 

        total_yield_tt = 0
        total_yield_st = 0
        for cat in cats:
            yield_tt = ws_tt.data("fcnc_%s_125_13TeV_%s" % (coupling.lower(), cat)).sumEntries()
            yield_st = ws_st.data("fcnc_%s_125_13TeV_%s" % (coupling.lower(), cat)).sumEntries()

            total_yield_tt += yield_tt
            total_yield_st += yield_st

            print "Coupling: %s, Year: %s, Cat: %s, st/tt fraction: %.2f" % (coupling, year, cat, yield_st/yield_tt)
            unc = calculate_total_unc(yield_tt, yield_st, True)
            uncertainties[coupling][year][cat] = unc

        total_unc = calculate_total_unc(total_yield_tt, total_yield_st, True)
        uncertainties[coupling][year]["all"] = total_unc

with open("theory_uncertainties/fcnc_individual_uncs.json", "w") as f_out:
    json.dump(uncertainties, f_out, sort_keys=True, indent=4)

#print "Coupling: %s, Year: %s, Cat: %s, tt fcnc yield: %s" % (coupling, year, cat, y)
