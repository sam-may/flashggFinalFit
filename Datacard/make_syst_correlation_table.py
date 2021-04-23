import json

signal_shape_systematics = [
        {'name':'CMS_hgg_nuisance_deltafracright','title':'CMS_hgg_nuisance_deltafracright','type':'signal_shape','mean':'0.0','sigma':'0.02'},
        {'name':'CMS_hgg_nuisance_NonLinearity_13TeVscale','title':'CMS_hgg_nuisance_NonLinearity_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'0.001'},
        {'name':'CMS_hgg_nuisance_Geant4_13TeVscale','title':'CMS_hgg_nuisance_Geant4_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'0.0005'},
        {'name':'CMS_hgg_nuisance_HighR9EB_13TeVscale','title':'CMS_hgg_nuisance_HighR9EB_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_HighR9EE_13TeVscale','title':'CMS_hgg_nuisance_HighR9EE_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EB_13TeVscale','title':'CMS_hgg_nuisance_LowR9EB_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EE_13TeVscale','title':'CMS_hgg_nuisance_LowR9EE_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_ShowerShapeHighR9EB_scale','title':'CMS_hgg_nuisance_ShowerShapeHighR9EB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_ShowerShapeHighR9EE_scale','title':'CMS_hgg_nuisance_ShowerShapeHighR9EE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_ShowerShapeLowR9EB_scale','title':'CMS_hgg_nuisance_ShowerShapeLowR9EB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_ShowerShapeLowR9EE_scale','title':'CMS_hgg_nuisance_ShowerShapeLowR9EE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_MaterialCentralBarrel_scale','title':'CMS_hgg_nuisance_MaterialCentralBarrel_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_MaterialOuterBarrel_scale','title':'CMS_hgg_nuisance_MaterialOuterBarrel_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_MaterialForward_scale','title':'CMS_hgg_nuisance_MaterialForward_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_FNUFEE_scale','title':'CMS_hgg_nuisance_FNUFEE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_FNUFEB_scale','title':'CMS_hgg_nuisance_FNUFEB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_HighR9EBRho_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EBRho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_HighR9EERho_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EERho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EBRho_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EBRho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
        {'name':'CMS_hgg_nuisance_LowR9EERho_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EERho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'}
          ]


experimental_systematics = [
        #{'name':'lumi_13TeV','title':'lumi_13TeV','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016':'1.025','2017':'1.023','2018':'1.025'}},
        {'name':'lumi_13TeV_Uncorrelated','title':'lumi_13TeV_Uncorrelated','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016':'1.022','2017':'1.020','2018':'1.015'}},
        {'name':'lumi_13TeV_X_Y_Factorization','title':'lumi_13TeV_X_Y_Factorization','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.009','2017':'1.008','2018':'1.020'}},
        {'name':'lumi_13TeV_Length_Scale','title':'lumi_13TeV_Length_Scale','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.003','2018':'1.002'}},
        {'name':'lumi_13TeV_Beam_Beam_Deflection','title':'lumi_13TeV_Beam_Beam_Deflection','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.004','2017':'1.004','2018':'-'}},
        {'name':'lumi_13TeV_Dynamic_Beta','title':'lumi_13TeV_Dynamic_Beta','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.005','2017':'1.005','2018':'-'}},
        {'name':'lumi_13TeV_Beam_Current_Calibration','title':'lumi_13TeV_Beam_Current_Calibration','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.003','2018':'1.002'}},
        {'name':'lumi_13TeV_Ghosts_And_Satellites','title':'lumi_13TeV_Ghosts_And_Satellites','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.004','2017':'1.001','2018':'-'}},
        {'name':'LooseMvaSF','title':'CMS_hgg_LooseMvaSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
        {'name':'PreselSF','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'electronVetoSF','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
        {'name':'TriggerWeight','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':0},
        {'name':'MvaShift','title':'CMS_hgg_phoIdMva','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'ElectronIDWeight', 'title':'CMS_hgg_ElectronIDWeight', 'type':'factory', 'prior':'lnN','correlateAcrossYears':0},
        {'name':'ElectronRecoWeight', 'title':'CMS_hgg_ElectronRecoWeight', 'type':'factory', 'prior':'lnN','correlateAcrossYears':0},
        {'name':'MuonIDWeight', 'title':'CMS_hgg_MuonIDWeight', 'type':'factory', 'prior':'lnN','correlateAcrossYears':0},
        {'name':'MuonIsoWeight', 'title':'CMS_hgg_MuonIsoWeight', 'type':'factory', 'prior':'lnN','correlateAcrossYears':0},
        {'name':'JEC','title':'CMS_scale_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
        {'name':'JER','title':'CMS_res_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
        {'name':'metJecUncertainty','title':'CMS_hgg_MET_scale_j','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'metJerUncertainty','title':'CMS_hgg_MET_res_j','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'metPhoUncertainty','title':'CMS_hgg_MET_PhotonScale','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'metUncUncertainty','title':'CMS_hgg_MET_Unclustered','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'prefireWeight', 'title':'L1PrefireWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
        {'name':'genTopPtReweight', 'title':'GenTopPtWeight', 'type':'factory','prior':'lnN','correlateAcrossYears':1},
]

btag_sources = ["jes", "hfstats1", "hfstats2", "cferr1", "cferr2", "lfstats1", "lfstats2", "lf", "hf"] # need to add lf, hf
correlations = [0, 0, 0, 1, 1, 0, 0, 1, 1]
for source, corr in zip(btag_sources, correlations):
    entry = {
        'name'  : 'JetBTagReshapeWeight_%s' % (source),
        'title' : 'CMS_hgg_bTagReshape_%s' % (source),
        'type'  : 'factory',
        'prior' : 'lnN',
        'correlateAcrossYears' : 0
    }
    experimental_systematics.append(entry)


correlation_dict = {
    1 : "fully correlated",
    0 : "uncorrelated",
    -1 : "partially correlated"
}

print "\\begin{tabular}{ l | c }"
print "\multicolumn{2}{c}{Correlation of experimental uncertainties across years} \\\\ \\hline \\hline"
print "Syst & Correlation \\\\ \\hline"
for syst in experimental_systematics:
    name = syst['name'].replace("_", "-")
    correlation = correlation_dict[syst['correlateAcrossYears']]
    print "%s & %s \\\\" % (name, correlation)
print " \\hline \\hline"
print " \\end{tabular}" 
