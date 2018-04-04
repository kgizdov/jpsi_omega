l0_prescale_11 = {
    '0x0037': {
        'PhotonNoSPD'      : '0.01',
        'Electron,lowMult' : '100',
        'MuonNoSPD'        : '0.01',
        'HighSumETJet'     : '0.0001',
        'Photon,lowMult'   : '100',
        'Photon'           : '100',
        'Electron'         : '100',
        'ElectronNoSPD'    : '0.01',
        'Hadron'           : '100',
        'MUON,minbias'     : '0.001',
        'B1gas'            : '100',
        'B2gas'            : '100',
        'PhotonHi'         : '100',
        'CALO'             : '0.0001',
        'ElectronHi'       : '100',
        'Muon,lowMult'     : '100',
        'HadronNoSPD'      : '0.01',
        'DiHadron,lowMult' : '10',
        'Muon'             : '100',
        'NoPVFlag'         : '100',
        'DiMuon'           : '100',
        'DiMuon,lowMult'   : '100',
        'DiEM,lowMult'     : '100',
        'DiMuonNoSPD'      : '0.01'
    }
}

l0_prescale_12 = {
    '0x0046': {
        'PhotonNoSPD'      : '0.01',
        'Electron,lowMult' : '100',
        'MuonNoSPD'        : '0.01',
        'PhotonHi'         : '100',
        'Photon,lowMult'   : '100',
        'Photon'           : '100',
        'Electron'         : '100',
        'ElectronNoSPD'    : '0.01',
        'Hadron'           : '100',
        'MUON,minbias'     : '0.001',
        'B1gas'            : '100',
        'B2gas'            : '100',
        'DiEM,lowMult'     : '100',
        'ElectronHi'       : '100',
        'Muon,lowMult'     : '100',
        'HadronNoSPD'      : '0.01',
        'DiHadron,lowMult' : '25',
        'Muon'             : '100',
        'NoPVFlag'         : '100',
        'DiMuon'           : '100',
        'HighSumETJet'     : '0.01',
        'DiMuon,lowMult'   : '100',
        'CALO'             : '0.0001',
        'DiMuonNoSPD'      : '0.01'
    }
}

l0_trig = [
     'L0PhysicsDecision'
    ,'L0ElectronDecision'
    ,'L0ElectronNoSPDDecision'
    ,'L0ElectronHighDecision'
    ,'L0HighSumETJetDecision'
    ,'L0HadronDecision'
    ,'L0HadronNoSPDDecision'
    ,'L0DiHadronDecision'
    ,'L0B1gasDecision'
    ,'L0B2gasDecision'
    ,'L0CALODecision'
    ,'L0DiEMDecision'
    ,'L0MuonDecision'
    ,'L0MuonHighDecision'
    ,'L0MuonNoSPDDecision'
    ,'L0DiMuonDecision'
    ,'L0DiMuonNoSPDDecision'
    ,'L0PhotonDecision'
    ,'L0PhotonHighDecision'
    ,'L0PhotonNoSPDDecision'
]

hlt1_trig = [
     'Hlt1DiMuonHighMassDecision'
    ,'Hlt1DiMuonLowMassDecision'
    ,'Hlt1SingleMuonNoIPDecision'
    ,'Hlt1SingleMuonHighPTDecision'
    ,'Hlt1SingleElectronNoIPDecision'
    ,'Hlt1TrackAllL0Decision'
    ,'Hlt1TrackMuonDecision'
    ,'Hlt1TrackPhotonDecision'
    ,'Hlt1TrackForwardPassThroughDecision'
    ,'Hlt1TrackForwardPassThroughLooseDecision'
    ,'Hlt1LumiDecision'
    ,'Hlt1LumiMidBeamCrossingDecision'
    ,'Hlt1MBNoBiasDecision'
    ,'Hlt1CharmCalibrationNoBiasDecision'
    ,'Hlt1MBMicroBiasVeloDecision'
    ,'Hlt1MBMicroBiasVeloRateLimitedDecision'
    ,'Hlt1MBMicroBiasTStationDecision'
    ,'Hlt1MBMicroBiasTStationRateLimitedDecision'
    ,'Hlt1L0AnyDecision'
    ,'Hlt1L0AnyRateLimitedDecision'
    ,'Hlt1L0AnyNoSPDDecision'
    ,'Hlt1L0AnyNoSPDRateLimitedDecision'
    ,'Hlt1L0HighSumETJetDecision'
    ,'Hlt1NoPVPassThroughDecision'
    ,'Hlt1DiProtonDecision'
    ,'Hlt1DiProtonLowMultDecision'
    ,'Hlt1BeamGasNoBeamBeam1Decision'
    ,'Hlt1BeamGasNoBeamBeam2Decision'
    ,'Hlt1BeamGasBeam1Decision'
    ,'Hlt1BeamGasBeam2Decision'
    ,'Hlt1BeamGasCrossingEnhancedBeam1Decision'
    ,'Hlt1BeamGasCrossingEnhancedBeam2Decision'
    ,'Hlt1BeamGasCrossingForcedRecoDecision'
    ,'Hlt1ODINTechnicalDecision'
    ,'Hlt1Tell1ErrorDecision'
    ,'Hlt1VeloClosingMicroBiasDecision'
    ,'Hlt1BeamGasCrossingParasiticDecision'
    ,'Hlt1ErrorEventDecision'
    ,'Hlt1GlobaDecisionl'
]

hlt2_trig = [
     'Hlt2SingleTFElectronDecision'
    ,'Hlt2SingleElectronTFLowPtDecision'
    ,'Hlt2SingleElectronTFHighPtDecision'
    ,'Hlt2SingleTFVHighPtElectronDecision'
    ,'Hlt2DiElectronHighMassDecision'
    ,'Hlt2DiElectronBDecision'
    ,'Hlt2B2HHLTUnbiasedDecision'
    ,'Hlt2B2HHLTUnbiasedDetachedDecision'
    ,'Hlt2Topo2BodySimpleDecision'
    ,'Hlt2Topo3BodySimpleDecision'
    ,'Hlt2Topo4BodySimpleDecision'
    ,'Hlt2Topo2BodyBBDTDecision'
    ,'Hlt2Topo3BodyBBDTDecision'
    ,'Hlt2Topo4BodyBBDTDecision'
    ,'Hlt2TopoMu2BodyBBDTDecision'
    ,'Hlt2TopoMu3BodyBBDTDecision'
    ,'Hlt2TopoMu4BodyBBDTDecision'
    ,'Hlt2TopoE2BodyBBDTDecision'
    ,'Hlt2TopoE3BodyBBDTDecision'
    ,'Hlt2TopoE4BodyBBDTDecision'
    ,'Hlt2TopoRad2BodyBBDTDecision'
    ,'Hlt2TopoRad2plus1BodyBBDTDecision'
    ,'Hlt2IncPhiDecision'
    ,'Hlt2IncPhiSidebandsDecision'
    ,'Hlt2CharmHadD02HHKsLLDecision'
    ,'Hlt2Dst2PiD02PiPiDecision'
    ,'Hlt2Dst2PiD02MuMuDecision'
    ,'Hlt2Dst2PiD02KMuDecision'
    ,'Hlt2Dst2PiD02KPiDecision'
    ,'Hlt2PassThroughDecision'
    ,'Hlt2TransparentDecision'
    ,'Hlt2LumiDecision'
    ,'Hlt2ForwardDecision'
    ,'Hlt2DebugEventDecision'
    ,'Hlt2CharmHadD02HH_D02PiPiDecision'
    ,'Hlt2CharmHadD02HH_D02PiPiWideMassDecision'
    ,'Hlt2CharmHadD02HH_D02KKDecision'
    ,'Hlt2CharmHadD02HH_D02KKWideMassDecision'
    ,'Hlt2CharmHadD02HH_D02KPiDecision'
    ,'Hlt2CharmHadD02HH_D02KPiWideMassDecision'
    ,'Hlt2ExpressJPsiDecision'
    ,'Hlt2ExpressJPsiTagProbeDecision'
    ,'Hlt2ExpressLambdaDecision'
    ,'Hlt2ExpressKSDecision'
    ,'Hlt2ExpressDs2PhiPiDecision'
    ,'Hlt2ExpressBeamHaloDecision'
    ,'Hlt2ExpressDStar2D0PiDecision'
    ,'Hlt2CharmHadLambdaC2KPPiDecision'
    ,'Hlt2Bs2PhiGammaDecision'
    ,'Hlt2Bs2PhiGammaWideBMassDecision'
    ,'Hlt2Bd2KstGammaDecision'
    ,'Hlt2Bd2KstGammaWideKMassDecision'
    ,'Hlt2Bd2KstGammaWideBMassDecision'
    ,'Hlt2CharmHadD2KS0H_D2KS0PiDecision'
    ,'Hlt2CharmHadD2KS0H_D2KS0KDecision'
    ,'Hlt2CharmRareDecayD02MuMuDecision'
    ,'Hlt2B2HHDecision'
    ,'Hlt2MuonFromHLT1Decision'
    ,'Hlt2SingleMuonDecision'
    ,'Hlt2SingleMuonHighPTDecision'
    ,'Hlt2SingleMuonVHighPTDecision'
    ,'Hlt2SingleMuonLowPTDecision'
    ,'Hlt2DiProtonDecision'
    ,'Hlt2DiProtonLowMultDecision'
    ,'Hlt2CharmSemilepD02HMuNu_D02KMuNuWSDecision'
    ,'Hlt2CharmSemilepD02HMuNu_D02PiMuNuWSDecision'
    ,'Hlt2CharmSemilepD02HMuNu_D02KMuNuDecision'
    ,'Hlt2CharmSemilepD02HMuNu_D02KMuNuTightDecision'
    ,'Hlt2CharmSemilepD02HMuNu_D02PiMuNuDecision'
    ,'Hlt2CharmHadMinBiasLambdaC2KPPiDecision'
    ,'Hlt2CharmHadMinBiasD02KPiDecision'
    ,'Hlt2CharmHadMinBiasD02KKDecision'
    ,'Hlt2CharmHadMinBiasDplus2hhhDecision'
    ,'Hlt2CharmHadMinBiasLambdaC2LambdaPiDecision'
    ,'Hlt2TFBc2JpsiMuXDecision'
    ,'Hlt2TFBc2JpsiMuXSignalDecision'
    ,'Hlt2diPhotonDiMuonDecision'
    ,'Hlt2LowMultMuonDecision'
    ,'Hlt2LowMultHadronDecision'
    ,'Hlt2LowMultHadron_nofilterDecision'
    ,'Hlt2LowMultPhotonDecision'
    ,'Hlt2LowMultElectronDecision'
    ,'Hlt2LowMultElectron_nofilterDecision'
    ,'Hlt2DisplVerticesHighMassSingleDecision'
    ,'Hlt2DisplVerticesDoubleDecision'
    ,'Hlt2DisplVerticesHighFDSingleDecision'
    ,'Hlt2DisplVerticesSingleDecision'
    ,'Hlt2DisplVerticesSinglePostScaledDecision'
    ,'Hlt2DisplVerticesDoublePostScaledDecision'
    ,'Hlt2DisplVerticesSingleHighMassPostScaledDecision'
    ,'Hlt2DisplVerticesSingleHighFDPostScaledDecision'
    ,'Hlt2DisplVerticesSingleMVPostScaledDecision'
    ,'Hlt2DisplVerticesSingleDownDecision'
    ,'Hlt2CharmSemilepD2HMuMuDecision'
    ,'Hlt2CharmSemilepD2HMuMuWideMassDecision'
    ,'Hlt2RadiativeTopoTrackTOSDecision'
    ,'Hlt2RadiativeTopoPhotonL0Decision'
    ,'Hlt2B2HHPi0_MergedDecision'
    ,'Hlt2CharmHadD2HHHDecision'
    ,'Hlt2CharmHadD2HHHWideMassDecision'
    ,'Hlt2DiMuonDecision'
    ,'Hlt2DiMuonLowMassDecision'
    ,'Hlt2DiMuonJPsiDecision'
    ,'Hlt2DiMuonJPsiHighPTDecision'
    ,'Hlt2DiMuonPsi2SDecision'
    ,'Hlt2DiMuonPsi2SHighPTDecision'
    ,'Hlt2DiMuonBDecision'
    ,'Hlt2DiMuonZDecision'
    ,'Hlt2DiMuonDY1Decision'
    ,'Hlt2DiMuonDY2Decision'
    ,'Hlt2DiMuonDY3Decision'
    ,'Hlt2DiMuonDY4Decision'
    ,'Hlt2DiMuonDetachedDecision'
    ,'Hlt2DiMuonDetachedHeavyDecision'
    ,'Hlt2DiMuonDetachedJPsiDecision'
    ,'Hlt2TriMuonDetachedDecision'
    ,'Hlt2DoubleDiMuonDecision'
    ,'Hlt2DiMuonAndMuonDecision'
    ,'Hlt2TriMuonTauDecision'
    ,'Hlt2DiMuonAndGammaDecision'
    ,'Hlt2DiMuonAndD0Decision'
    ,'Hlt2DiMuonAndDpDecision'
    ,'Hlt2DiMuonAndDsDecision'
    ,'Hlt2DiMuonAndLcDecision'
    ,'Hlt2CharmSemilepD02HHMuMuHardHadronsSoftMuonsDecision'
    ,'Hlt2CharmSemilepD02HHMuMuHardHadronsSoftMuonsWideMassDecision'
    ,'Hlt2CharmSemilepD02HHMuMuHardHadronsAndMuonsDecision'
    ,'Hlt2CharmSemilepD02HHMuMuHardHadronsAndMuonsWideMassDecision'
    ,'Hlt2CharmSemilepD02HHMuMuDecision'
    ,'Hlt2CharmSemilepD02HHMuMuWideMassDecision'
    ,'Hlt2CharmHadD02HHHHDecision'
    ,'Hlt2CharmHadD02HHHHWideMassDecision'
    ,'Hlt2ErrorEventDecision'
    ,'Hlt2GlobaDecisionl'
]


hlt2_only_in_11 = [
    'Hlt2CharmSemilepD02HHMuMu',
    'Hlt2DisplVerticesDoublePostScaled',
    'Hlt2CharmSemilepD02HHMuMuHardHadronsSoftMuonsWideMass',
    'Hlt2MuonFromHLT1',
    'Hlt2CharmSemilepD02HHMuMuHardHadronsAndMuons',
    'Hlt2CharmSemilepD02HHMuMuWideMass',
    'Hlt2CharmSemilepD2HMuMuWideMass',
    'Hlt2DisplVerticesHighMassSingle',
    'Hlt2DisplVerticesSingleHighMassPostScaled',
    'Hlt2CharmHadD02HHHH',
    'Hlt2RadiativeTopoPhotonL0',
    'Hlt2DiMuon',
    'Hlt2CharmHadD02HHHHWideMass',
    'Hlt2RadiativeTopoTrackTOS',
    'Hlt2DisplVerticesHighFDSingle',
    'Hlt2DisplVerticesSingleMVPostScaled',
    'Hlt2DisplVerticesSinglePostScaled',
    'Hlt2DisplVerticesSingleHighFDPostScaled',
    'Hlt2CharmSemilepD02HHMuMuHardHadronsAndMuonsWideMass',
    'Hlt2CharmSemilepD2HMuMu',
    'Hlt2CharmSemilepD02HHMuMuHardHadronsSoftMuons',
    'Hlt2DiMuonLowMass'
]
hlt2_only_in_12 = [
    'Hlt2CharmHadD02HHHHDst_2K2pi',
    'Hlt2DisplVerticesSingleHighMass',
    'Hlt2DisplVerticesSingleVeryHighFD',
    'Hlt2ChargedHyperon_Xi2Lambda0DDMu',
    'Hlt2CharmSemilep3bodyD2KMuMuSS',
    'Hlt2LambdaC_LambdaC2Lambda0LLPi',
    'Hlt2DisplVerticesSingleLoosePS',
    'Hlt2KshortToMuMuPiPi',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithKSLLWideMass',
    'Hlt2ChargedHyperon_Xi2Lambda0LLPi',
    'Hlt2CharmHadD2KS0KS0',
    'Hlt2CharmSemilepD02KPiMuMu',
    'Hlt2CharmHadD02HHXDst_BaryonhhX',
    'Hlt2LowMultD2KPiWS',
    'Hlt2CharmHadD2KS0H_D2KS0DDPi',
    'Hlt2ChargedHyperon_Omega2Lambda0LLK',
    'Hlt2DiMuonDetachedPsi2S',
    'Hlt2CharmHadD02HHHH_2K2pi',
    'Hlt2CharmHadD02HHHHDst_2K2piWideMass',
    'Hlt2CharmHadLambdaC2PiPPiWideMass',
    'Hlt2CharmHadD02HHHHDst_K3piWideMass',
    'Hlt2LowMultChiC2HHHH',
    'Hlt2HighPtJets',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithLambda0DDWideMass',
    'Hlt2CharmHadD02HHHHDst_4pi',
    'Hlt2ExpressD02KPi',
    'Hlt2LowMultLMR2HH',
    'Hlt2CharmHadD02HHHH_KKpipi',
    'Hlt2RadiativeTopoTrack',
    'Hlt2LowMultDDIncVF',
    'Hlt2CharmHadD02HHHH_2K2piWideMass',
    'Hlt2LowMultD2K3Pi',
    'Hlt2LowMultD2KPiPiWS',
    'Hlt2RadiativeTopoPhoton',
    'Hlt2LowMultChiC2PP',
    'Hlt2CharmSemilep3bodyLambdac2PMuMuSS',
    'Hlt2CharmHadD02HHKsDD',
    'Hlt2CharmHadD02HHHH_3KpiWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithLambda0LL',
    'Hlt2CharmHadLambdaC2PiPK',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithKSDD',
    'Hlt2DisplVerticesDoublePS',
    'Hlt2CharmHadD02HHHH_K3piWideMass',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWideMass',
    'Hlt2LowMultD2KPiPi',
    'Hlt2LowMultChiC2HHWS',
    'Hlt2CharmHadD02HHHH_KKpipiWideMass',
    'Hlt2CharmHadD02HHXDst_hhXWideMass',
    'Hlt2CharmHadD02HHXDst_LeptonhhX',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithLambda0DD',
    'Hlt2DiPhi',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithKSLL',
    'Hlt2CharmHadD02HHHH_3Kpi',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithLambda0DD',
    'Hlt2CharmHadD02HHHHDst_KKpipi',
    'Hlt2CharmSemilep3bodyLambdac2PMuMu',
    'Hlt2CharmHadD02HHHH_4piWideMass',
    'Hlt2CharmSemilep3bodyD2PiMuMuSS',
    'Hlt2CharmHadD2HHHKsLL',
    'Hlt2LowMultChiC2HH',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithLambda0LLWideMass',
    'Hlt2LambdaC_LambdaC2Lambda0DDK',
    'Hlt2CharmHadD02HHHHDst_3Kpi',
    'Hlt2CharmHadD02HHHHDst_KKpipiWideMass',
    'Hlt2ChargedHyperon_Omega2Lambda0DDK',
    'Hlt2LowMultChiC2HHHHWS',
    'Hlt2LowMultD2K3PiWS',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithLambda0LL',
    'Hlt2DisplVerticesSingleHighFD',
    'Hlt2ChargedHyperon_Xi2Lambda0LLMu',
    'Hlt2CharmSemilep3bodyD2PiMuMu',
    'Hlt2CharmHadD2KS0H_D2KS0DDK',
    'Hlt2CharmHadD02HHHH_K3pi',
    'Hlt2CharmHadD2HHHKsDD',
    'Hlt2CharmSemilepD02PiPiMuMu',
    'Hlt2DisplVerticesSinglePS',
    'Hlt2CharmHadLambdaC2KPKWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithKSDDWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithLambda0DDWideMass',
    'Hlt2LambdaC_LambdaC2Lambda0DDPi',
    'Hlt2CharmHadLambdaC2PiPKWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithKSDD',
    'Hlt2CharmHadD02HHHHDst_K3pi',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithKSLL',
    'Hlt2LowMultDDIncCP',
    'Hlt2CharmSemilepD02KKMuMu',
    'Hlt2CharmHadD02HHHHDst_4piWideMass',
    'Hlt2CharmHadLambdaC2KPK',
    'Hlt2CharmSemilep3bodyD2KMuMu',
    'Hlt2CharmHadD02HHXDst_hhX',
    'Hlt2LowMultD2KPi',
    'Hlt2CharmHadLambdaC2PiPPi',
    'Hlt2CharmHadD2KS0KS0WideMass',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithKSDDWideMass',
    'Hlt2ChargedHyperon_Xi2Lambda0DDPi',
    'Hlt2CharmHadD02HHHH_4pi',
    'Hlt2CharmHadLambdaC2KPPiWideMass',
    'Hlt2CharmHadD02HHHHDst_3KpiWideMass',
    'Hlt2CharmHadD02HHXDst_BaryonhhXWithLambda0LLWideMass',
    'Hlt2LambdaC_LambdaC2Lambda0LLK',
    'Hlt2CharmHadD02HHXDst_LeptonhhXWithKSLLWideMass'
]

hlt1_only_in_11 = [
    'Hlt1MBMicroBiasVeloRateLimited',
    'Hlt1L0AnyNoSPDRateLimited',
    'Hlt1L0AnyRateLimited',
    'Hlt1MBMicroBiasTStationRateLimited'
]

hlt1_only_in_12 = [
    'Hlt1HighPtJetsSinglePV',
    'Hlt1BeamGasCrossingForcedRecoFullZ',
    'Hlt1VertexDisplVertex',
    'Hlt1BeamGasHighRhoVertices',
    'Hlt1TrackAllL0Tight'
]
