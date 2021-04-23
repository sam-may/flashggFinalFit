from ROOT import *
gROOT.SetBatch(True)

def Plot2Data(ws1,ws2,dataname, savepath):
    print dataname
    #if dataname != "ggh_125_13TeV_TTHLeptonicTag_3_metJecUncertaintyUp01sigma":
    #    return 0

    mass_rv = RooRealVar("CMS_hgg_mass", "", 100, 180)
    frame = mass_rv.frame()
    data1 = ws1.data(dataname)
    data2 = ws2.data(dataname)
    print "data1: ", data1.sumEntries(), data1.numEntries()
    print "data2: ", data2.sumEntries(), data2.numEntries()
    data1.plotOn(frame, RooFit.MarkerColor(1), RooFit.Name("old"))
    data2.plotOn(frame, RooFit.MarkerColor(2), RooFit.Name("new"))

    legend = TLegend(0.5,0.7,0.9,0.9)
    legend.AddEntry(frame.findObject("old"), "old sequence", "ep")
    legend.AddEntry(frame.findObject("new"), "new sequence", "ep")

    c = TCanvas("c", "", 800, 800)

    frame.Draw()
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.45*c.GetTopMargin())
    latex.SetTextFont(42)
    latex.SetTextAlign(11)
    latex.DrawLatex(0.15, 0.5, dataname)

    #c.SaveAs(savepath + dataname + ".png")
    c.SaveAs(savepath + dataname + ".pdf")

roodatasetsname = "roodatahists.txt"

text_file = open(roodatasetsname, "r")
lines = text_file.read().split('\n')

lines = [line for line in lines if not ("FCNCLeptonicTag_3" in line or "FCNCLeptonicTag_2" in line or "FCNCHadronicTag_3" in line or "FCNCHadronicTag_2" in line)]

#wsfilename1 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_Hut_2017_prod_v2.1_2-March-2020/ws_merged_sm_higgs_Hut_tth_125_2017.root"
#wsfilename2 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_Hut_2017_prod_v2.1_2-March-2020/ws_merged_sm_higgs_Hut_tth_125_2017.root"
#wsfilename2 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_Hut_2017_v4.2_11-July-2020/ws_merged_sm_higgs_Hut_tth_125_2017.root"

wsfilename1 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/ttH_2018_2.root"
wsfilename2 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/ttH_2018_2.root"

#wsfilename1 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/output_FCNC_USER.root"
#wsfilename1 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/ttH_2018_2.root"
#wsfilename1 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_8/src/flashgg/ttH_2018_2.root"
#wsfilename2 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/output_FCNC_USER.root"
#wsfilename2 = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_8/src/flashgg/ttH_2018_2.root"

savepath = "/home/users/sjmay/public_html/FCNC/Workspaces/debug/"

file1 = TFile.Open(wsfilename1)
file2 = TFile.Open(wsfilename2)

ws1 = file1.Get("tagsDumper/cms_hgg_13TeV")
ws2 = file2.Get("tagsDumper/cms_hgg_13TeV")

for line in lines[0:50]:
    if line != "":
        Plot2Data(ws1, ws2, line, savepath)

from subprocess import call
call("chmod -R 755 " + savepath, shell=True)
