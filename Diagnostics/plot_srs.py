import os, sys
import glob

import ROOT
ROOT.gROOT.SetBatch(True)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--years", help = "which years to consider", type=str, default = "2016,2017,2018")
parser.add_argument("--couplings", help = "which couplings to run for", type=str, default = "Hut,Hct")
parser.add_argument("--procs", help = "which processes to consider", type=str, default = "tth,ggh,vbf,wh,zh,thq,thw")
parser.add_argument("--mH", help = "value to set Higgs mass to", type=float, default=125.0)
parser.add_argument("--cats", help = "which categories to consider", type=str, default = "FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2")
args = parser.parse_args()

signal_ws_dir = "../Signal/outdir_fcnc_COUPLING_YEAR/"
signal_ws_name = "CMS-HGG_sigfit_fcnc_COUPLING_YEAR_PROC_CAT.root"
signal_ws = signal_ws_dir + signal_ws_name

couplings = args.couplings.split(",")
years = args.years.split(",")
procs = args.procs.split(",")
cats = args.cats.split(",")

#limit = { "Hut" : 0.4094, "Hct" : 0.4891 }
#limit = { "Hut" : 0.3344, "Hct" : 0.4437 }
#limit = { "Hut" : 0.2867, "Hct" : 0.3422 } # v5.1_18Sep2020
limit = { "Hut" : 0.2945, "Hct" : 0.3469 } # v5.2_5Oct2020

def get_bkg_yield(file, m): 
    bkg_yield = 0
    with open(file, "r") as f_in:
        lines = f_in.readlines()
        for line in lines:
            if not "[INFO] mgg:" in line:
                continue
            mass = float(line.split()[2])
            if mass == m: 
                bkg_yield += float(line.split()[4])
    return bkg_yield

for coupling in couplings:
    for cat in cats:
        mgg = ROOT.RooRealVar("CMS_hgg_mass","",100,180)
        frame = mgg.frame()

        pdfs_al = ROOT.RooArgList("pdfs")
        pdfs_bkg_as = ROOT.RooArgSet("pdfs_resBkg")
        fracs_al = ROOT.RooArgList("fracs")
        values = ROOT.RooArgList
        for proc in procs:
            if "fcnc" in proc:
                continue
            for year in years:
                ws_file = ROOT.TFile.Open(signal_ws.replace("COUPLING", coupling).replace("YEAR", year).replace("PROC", proc).replace("CAT", cat))
                ws = ws_file.Get("wsig_13TeV")
                mh = ws.var("CMS_hgg_mass")
                pdf = ws.pdf("extendhggpdfsmrel_%s_13TeV_%s_%s" % (year, proc, cat))
                #pdf
                mh.setVal(args.mH)
                pdfs_al.add(pdf)
                pdfs_bkg_as.add(pdf)
                fracs_al.add(ROOT.RooRealVar("frac_%s_%s_%s_%s" % (coupling, cat, proc, year), "", 1.))
                #print ws.var("hggpdfsmrel_%s_13TeV_%s_%s_norm" % (year, proc, cat)).getVal(mh)
                #print coupling, cat, proc, year, pdf.expectedEvents(mh)

        model = ROOT.RooAddPdf("model","",pdfs_al)
        model.plotOn(frame, ROOT.RooFit.Components(pdfs_bkg_as))
        #model.plotOn(frame, ROOT.RooFit.Components(pdfs_bkg_as), ROOT.RooFit.LineStyle(2), ROOT.RooFit.LineColor(2), ROOT.RooFit.Name("bkg"))
        #model.plotOn(frame, ROOT.RooFit.Components(pdfs_bkg_as, ROOT.RooFit.LineStyle(2), ROOT.RooFit.LineColor(2), ROOT.RooFit.Name("bkg")))
        c = ROOT.TCanvas("c","",800,800)
        frame.GetXaxis().SetTitle("m_{#gamma#gamma}")
        frame.Draw()
        c.SaveAs("sr_%s_%s.pdf" % (coupling, cat))
