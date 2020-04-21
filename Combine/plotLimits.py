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

assumed_br = 0.1441

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
                    if "2.5" in line: results[coupling][cat]["-2sigma"] = float(line.split()[-1]) * assumed_br
                    if "16.0" in line: results[coupling][cat]["-1sigma"] = float(line.split()[-1]) * assumed_br
                    if "50.0" in line: results[coupling][cat]["exp"] = float(line.split()[-1]) * assumed_br
                    if "84.0" in line: results[coupling][cat]["+1sigma"] = float(line.split()[-1]) * assumed_br
                    if "97.5" in line: results[coupling][cat]["+2sigma"] = float(line.split()[-1]) * assumed_br

with open("plot_results_%s.json" % args.tag, "w") as f_out:
    json.dump(results, f_out, sort_keys=True, indent=4)

ylabel = { "Hut" : "BF (t #rightarrow Hu)", "Hct" : "BF (t #rightarrow Hc)" }

for coupling in couplings:
    c1 = ROOT.TCanvas("c1", "c1", 800, 800)

    nBins = len(cats_full)
    h_exp = ROOT.TH1F("h_exp", "h_exp", nBins, 0, nBins)
    h_plus1sigma = ROOT.TH1F("h_plus1sigma", "h_plus1sigma", nBins, 0, nBins)
    h_plus2sigma = ROOT.TH1F("h_plus2sigma", "h_plus2sigma", nBins, 0, nBins)
    h_minus1sigma = ROOT.TH1F("h_minus1sigma", "h_minus1sigma", nBins, 0, nBins)
    h_minus2sigma = ROOT.TH1F("h_minus2sigma", "h_minus2sigma", nBins, 0, nBins)

    h_exp.SetLineColor(1)
    h_exp.SetFillColor(0)
    h_exp.SetLineStyle(2)
    h_exp.SetLineWidth(2)

    h_plus1sigma.SetLineColor(3)
    h_minus1sigma.SetLineColor(3)
    h_plus1sigma.SetFillColor(3)
    h_minus1sigma.SetFillColor(3)

    h_plus2sigma.SetLineColor(5)
    h_minus2sigma.SetLineColor(5)
    h_plus2sigma.SetFillColor(5)
    h_minus2sigma.SetFillColor(5)

    y_max = -1
    y_min = 99999

    idx = 1
    for cat in cats_full:
        h_exp.SetBinContent(idx, results[coupling][cat]["exp"])
        h_exp.SetBinError(idx, 0.000000001)
        h_exp.GetXaxis().SetBinLabel(idx, cat.replace("All_Categories", "Combined"))

        diff_plus1sigma = abs(results[coupling][cat]["+1sigma"] - results[coupling][cat]["exp"])/2
        h_plus1sigma.SetBinContent(idx, results[coupling][cat]["exp"] + diff_plus1sigma) 
        h_plus1sigma.SetBinError(idx, diff_plus1sigma) 

        diff_plus2sigma = abs(results[coupling][cat]["+2sigma"] - results[coupling][cat]["exp"])/2
        h_plus2sigma.SetBinContent(idx, results[coupling][cat]["exp"] + diff_plus2sigma)
        h_plus2sigma.SetBinError(idx, diff_plus2sigma)

        if (results[coupling][cat]["exp"] + (2*diff_plus2sigma)) > y_max:
            y_max = results[coupling][cat]["exp"] + (2*diff_plus2sigma)

        diff_minus1sigma = abs(results[coupling][cat]["-1sigma"] - results[coupling][cat]["exp"])/2
        h_minus1sigma.SetBinContent(idx, results[coupling][cat]["exp"] - diff_minus1sigma)
        h_minus1sigma.SetBinError(idx, diff_minus1sigma)
                        
        diff_minus2sigma = abs(results[coupling][cat]["-2sigma"] - results[coupling][cat]["exp"])/2
        h_minus2sigma.SetBinContent(idx, results[coupling][cat]["exp"] - diff_minus2sigma)
        h_minus2sigma.SetBinError(idx, diff_minus2sigma)

        if (results[coupling][cat]["exp"] - (2*diff_minus2sigma)) > y_min:
            y_min = results[coupling][cat]["exp"] - (2*diff_minus2sigma)

        idx += 1

    h_exp.Draw("E")
    for hist in [h_plus2sigma, h_minus2sigma, h_plus1sigma, h_minus1sigma]:
        hist.SetMarkerColor(0)
        hist.SetMarkerSize(0)
        hist.Draw("E2,SAME")
   
    h_exp.Draw("SAME,E")
    h_exp.SetMinimum(y_min * 0.9)
    h_exp.SetMaximum(y_max * 1.1 * 0.5)

    h_exp.GetYaxis().SetTitle(ylabel[coupling])
    h_exp.GetYaxis().SetTitleOffset(1.23)
    ROOT.gPad.RedrawAxis()

    legend = ROOT.TLegend(0.16, 0.77, 0.46, 0.87)
    legend.AddEntry(h_exp, "Median Expected", "l")
    legend.AddEntry(h_plus1sigma, "#pm 1#sigma", "f")
    legend.AddEntry(h_plus2sigma, "#pm 2#sigma", "f")
    legend.SetBorderSize(0)
    legend.Draw("SAME")

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.4*c1.GetTopMargin())
    latex.SetTextFont(42)
    latex.SetTextAlign(11)
    latex.SetTextColor(1)
    latex.DrawLatex(0.17, 0.88, "95% CL Upper Limits: #bf{" + coupling + "}")

    latex.SetTextSize(0.6*c1.GetTopMargin())
    latex.DrawLatex(0.12, 0.935, "#bf{CMS}")

    latex.SetTextSize(0.6*c1.GetTopMargin())
    latex.DrawLatex(0.215, 0.935, "#it{Preliminary}")
    
    latex.DrawLatex(0.67, 0.935, "137 fb^{-1} (13 TeV)")

    c1.SaveAs("limits_%s_%s.pdf" % (coupling, args.tag))

