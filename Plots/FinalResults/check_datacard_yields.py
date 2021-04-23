import os, sys
import ROOT as r

lumi = { "2016" : 35900, "2017" : 41500, "2018" : 59800 }

def printYields(coupling, proc, tag, year):

    theFile = r.TFile('Models_%s/signal_%s/CMS-HGG_sigfit_mva_' % (coupling, year) + proc+'_'+tag+'.root')
    theWS = theFile.Get('wsig_13TeV')
    MH = theWS.var('MH')
    theNorm = theWS.function('hggpdfsmrel_13TeV_'+proc+'_'+tag+'_norm')
    for m in [120.,125.,130.]:
          MH.setVal(m)
          print 'nEvts for mh = %g is %.7f'%(int(m), theNorm.getVal()*lumi[year])

for coupling in ["Hct", "Hut"]:
    for proc in ["fcnc", "tth"]:
        if proc == "fcnc":
            proc += "_" + coupling.lower()
        for tag in ["FCNCHadronicTag_0", "FCNCHadronicTag_1"]:
            for year in ["2016", "2017", "2018"]:
                print coupling, proc, tag
                printYields(coupling, proc, tag, year)
