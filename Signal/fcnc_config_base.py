signalScriptCfg = {
        # Setup
        'inputWSDir' : '/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_COUPLING_YEAR_v4.4_17-July-2020',
        #'cats' : 'FCNCHadronicTag_3',
        'cats' : 'FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCHadronicTag_2,FCNCHadronicTag_3,FCNCLeptonicTag_0,FCNCLeptonicTag_1,FCNCLeptonicTag_2',
        'ext' : 'fcnc_COUPLING_YEAR',
        'analysis':'fcnc',
        'year' : 'YEAR',
        'beamspot' : '3.4',
        'numberOfBins' : '320',
        'massPoints' : '120,125,130',
        #'procs' : 'tth,vbf,ggh,wh',
        'procs' : 'vbf,wh,zh,ggh,tth,thq,thw,fcnc_COUPLINGLOWER',

        # Use DCB
        'useDCB' : 1,

        #Photon shape systematics  
        'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB',
        'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB',
        'scalesGlobal':'NonLinearity:UntaggedTag_0:2,Geant4',
        'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho',

        # Job Submission
        'batch' : 'uaf',
        'queue' : '1nh',

        # Mode
        'mode' : 'std',
} 
