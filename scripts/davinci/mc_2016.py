# Copyright Konstantin Gizdov 2018


import GaudiKernel.SystemOfUnits as Units
from GaudiKernel.SystemOfUnits import MeV, GeV, micrometer
from Gaudi.Configuration import *

####
from StrippingConf.Configuration import StrippingConf, StrippingStream
from StrippingSettings.Utils import strippingConfiguration
from StrippingArchive.Utils import buildStreams
from StrippingArchive import strippingArchive
####

from PhysSelPython.Wrappers import AutomaticData, Selection, SelectionSequence
from Configurables import FilterDesktop
from Configurables import DaVinci
from Configurables import DecayTreeTuple
from Configurables import TupleToolDecay
from Configurables import GaudiSequencer
from Configurables import CombineParticles
from Configurables import CondDB
from Configurables import LoKi__Hybrid__TupleTool
from Configurables import LoKi__Hybrid__TupleTool
from Configurables import LoKi__Hybrid__EvtTupleTool
from Configurables import MCTupleToolHierarchy
from Configurables import TupleToolMCTruth
from Configurables import TupleToolMCBackgroundInfo
from Configurables import TupleToolTISTOS, TriggerTisTos
from DecayTreeTuple.Configuration import *

# DaVinci settings
mode        = 'MC'                # DATA or MC
mag         = 'Down'              # magnet polarity, Up or Down; None for data
evtMax      = -1                  # number of events to read, -1 == all
inputType   = 'MDST'              # input file format
dataType    = '2016'              # year of input
tupleFile   = 'BdJpsiOmega.root'  # nTuple file name
histFile    = 'DVHistos.root'     # histogram file name
printFreq   = 1000                # log output frequency
outputLevel = ERROR               # log output verbosity
skipEvents  = 0                   # Events to skip from beginning
local       = False               # if running locally

# Data or Simulation settings
rootInTES   = '' if inputType == 'DST' else '/Event/AllStreams'  # need to specify if not DST
lum         = True if mode == 'DATA' else False
sim         = not lum

EVTMAX      = evtMax
MODE        = mode
OUTPUTLEVEL = outputLevel

from GaudiConf import IOHelper
# Use the local input data
if local:
    IOHelper().inputFiles([
        # '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/00041840_00000322_1.dimuon_11.dst'      # 2011
        '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/00074037_00000003_7.AllStreams.mdst'         # 2016 Str28r1 MagDown
        # '/afs/cern.ch/work/k/kgizdov/Git/BsJpsiPhi/davinci/00061346_00007805_1.dimuon.dst'  # 2016 Str26 MagDown
    ], clear=True)


# =============================================================================
## run PSIX0 WG-selections over ALLSTREAMS.DST MC
# =============================================================================
jpsi_name  = 'FullDSTDiMuonJpsi2MuMuDetachedLine'
jpsi_line  = 'Phys/{}/Particles'.format(jpsi_name)

import StrippingSelections.StrippingBandQ.StrippingPsiX0 as PSIX0
psix0  = PSIX0.PsiX0Conf(
    'PsiX0'
    ,config = {
         'NOPIDHADRONS' : True  ## important here!!!
        ,'DIMUONLINES'  : [ jpsi_line ]
    }
)

b2omega_selection = psix0.b2omega()


#########################################################################################################
# Set up the MCDecayTreeTuples for each of the decays that we are interested in.
# We want to save all of the generated events for each mode.
#########################################################################################################
from Configurables import MCDecayTreeTuple, MCTupleToolKinematic, MCTupleToolHierarchy, LoKi__Hybrid__MCTupleTool, TupleToolEventInfo
from Configurables import TupleToolDecayTreeFitter, TupleToolTrackPosition, TupleToolRecoStats, TupleToolGeometry, TupleToolTrackInfo
from Configurables import TupleToolTrigger, LoKi__PVReFitter, TupleToolTagging

# LoKi variables
LoKi_Photos = LoKi__Hybrid__MCTupleTool('LoKi_Photos')
LoKi_Photos.Variables = {
     'nPhotons' : 'MCNINTREE((\'gamma\' == MCABSID))'
    ,'MC_PT'    : 'MCPT'
    ,'MC_THETA' : 'MCTHETA'
    ,'MC_ETA'   : 'MCETA'
    ,'MC_PHI'   : 'MCPHI'
    ,'MC_ABSID' : 'MCABSID'
}

# all of MC events
mc_alg = MCDecayTreeTuple('MCTuple')
mc_alg.Decay = '[B0]cc ==> ^(J/psi(1S) ==> ^mu+ ^mu-) ^(omega(782) ==> ^pi+ ^pi- ^(pi0 ==> ^gamma ^gamma))'
mc_alg.TupleName = 'MCTuple'
# mc_alg.ToolList += [
#      'MCTupleToolKinematic'
#     ,'TupleToolEventInfo'
#     ,'MCTupleToolHierarchy'
#     ,'MCTupleToolPrimaries'
#     ,'MCTupleToolReconstructed'
#     ,'MCTupleToolPID'
# ]
mc_alg.Branches = {
     'B'       : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'Jpsi'    : '[B0]cc ==> ^(J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'muplus'  : '[B0]cc ==>  (J/psi(1S) ==> ^mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'muminus' : '[B0]cc ==>  (J/psi(1S) ==>  mu+ ^mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'X'       : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-) ^(omega(782) ==>  pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'hplus'   : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==> ^pi+  pi-  (pi0 ==>  gamma  gamma))'
    ,'hminus'  : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+ ^pi-  (pi0 ==>  gamma  gamma))'
    ,'hzero'   : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+  pi- ^(pi0 ==>  gamma  gamma))'
    ,'gamma1'  : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==> ^gamma  gamma))'
    ,'gamma2'  : '[B0]cc ==>  (J/psi(1S) ==>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 ==>  gamma ^gamma))'
}

from GaudiConfUtils.ConfigurableGenerators import MCDecayTreeTuple as MCTUPLE
from PhysSelPython.Wrappers                import SimpleSelection

mc_selection = SimpleSelection(
    'MCTupleSel'
    ,MCTUPLE
    ,[ b2omega_selection ]
    ## properties
    ,Decay = '[B0]cc => ^(J/psi(1S) => ^mu+ ^mu-) ^(omega(782) ==> ^pi+ ^pi- ^(pi0 => ^gamma ^gamma))'
    ,Branches = {
         'B'       : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'Jpsi'    : '[B0]cc => ^(J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'muplus'  : '[B0]cc =>  (J/psi(1S) => ^mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'muminus' : '[B0]cc =>  (J/psi(1S) =>  mu+ ^mu-)  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'X'       : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-) ^(omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'hplus'   : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==> ^pi+  pi-  (pi0 =>  gamma  gamma))'
        ,'hminus'  : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+ ^pi-  (pi0 =>  gamma  gamma))'
        ,'hzero'   : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+  pi- ^(pi0 =>  gamma  gamma))'
        ,'gamma1'  : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 => ^gamma  gamma))'
        ,'gamma2'  : '[B0]cc =>  (J/psi(1S) =>  mu+  mu-)  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma ^gamma))'
    }
)
mctuple_B2psiomega = mc_selection.algorithm()


# List of the mc tuples
mctuples = [
     mctuple_B2psiomega
    ,mc_alg
]

for tup in mctuples:
    # mc_kinem = tup.addTupleTool('MCTupleToolKinematic')  # for some reason doesn't work
    MCKinematic = tup.addTool(MCTupleToolKinematic, name = 'MCKinematic')
    tup.MCKinematic.Verbose = True
    tup.addTupleTool('TupleToolMCTruth')
    tup.addTupleTool('TupleToolMCBackgroundInfo')
    # tup.addTupleTool('TupleToolEventInfo')  # for some reason doesn't work
    tup.addTool(TupleToolEventInfo, name = 'EventInfo')
    tup.addTupleTool('MCTupleToolHierarchy')
    tup.addTupleTool('MCTupleToolPrimaries')
    tup.addTupleTool('MCTupleToolReconstructed')
    tup.addTupleTool('MCTupleToolPID')
    tup.addTool(LoKi_Photos)
    tup.ToolList  = [
         'MCTupleToolKinematic'
        ,'TupleToolEventInfo'
        ,'LoKi::Hybrid::MCTupleTool/LoKi_Photos'  # doesn't work with DaVinci v36r6
    ]

if OUTPUTLEVEL == DEBUG:
    from Configurables import PrintMCTree, PrintMCDecayTreeTool
    mctree = PrintMCTree('PrintTrue')
    mctree.addTool(PrintMCDecayTreeTool)
    mctree.PrintMCDecayTreeTool.Information = 'Name M P Px Py Pz Pt Vx Vy Vz'
    mctree.ParticleNames = [ 'B+', 'B-' ]
    mctree.Depth = 3  # down to the K and mu

#########################################################################################################
# Now set up the DecayTreeTuples for the reconstructed particles
#########################################################################################################
tupletools = [
     'TupleToolTrigger'
    ,'TupleToolGeometry'
    ,'TupleToolKinematic'
    # ,'TupleToolPropertime'
    ,'TupleToolPrimaries'
    ,'TupleToolEventInfo'
    ,'TupleToolTrackInfo'
    # ,'TupleToolTagging'
    ,'TupleToolPid'
    ,'TupleToolANNPID'
    ,'TupleToolRecoStats'
    ,'TupleToolTrackPosition'
    ,'TupleToolL0Calo'
    ,'TupleToolL0Data'
    ,'TupleToolTISTOS'
]

## Triggers
triglist = []

l0_lines = [
     'L0PhysicsDecision'
    ,'L0MuonDecision'
    ,'L0DiMuonDecision'
    ,'L0MuonHighDecision'
    ,'L0HadronDecision'
    ,'L0ElectronDecision'
    ,'L0PhotonDecision'
    ,'L0GlobalDecision'
]

hlt1_lines = [
     'Hlt1TrackMVADecision'
    ,'Hlt1DiMuonHighMassDecision'
    ,'Hlt1DiMuonLowMassDecision'
    ,'Hlt1SingleMuonNoIPDecision'
    ,'Hlt1SingleMuonHighPTDecision'
    ,'Hlt1TrackAllL0Decision'
    ,'Hlt1TrackMuonDecision'
    ,'Hlt1TrackPhotonDecision'
    ,'Hlt1L0AnyDecision'
    ,'Hlt1TwoTrackMVADecision'
    ,'Hlt1TrackMVALooseDecision'
    ,'Hlt1TwoTrackMVALooseDecision'
    ,'Hlt1TrackMuonMVADecision'
    ,'Hlt1DiMuonNoL0Decision'
    ,'Hlt1GlobalDecision'
]

hlt2_lines = [
     'Hlt2Topo2BodyDecision'
    ,'Hlt2Topo3BodyDecision'
    ,'Hlt2Topo4BodyDecision'
    ,'Hlt2TopoMu2BodyDecision'
    ,'Hlt2TopoMu3BodyDecision'
    ,'Hlt2TopoMu4BodyDecision'
    ,'Hlt2TopoMuMu2BodyDecision'
    ,'Hlt2TopoMuMu3BodyDecision'
    ,'Hlt2TopoMuMu4BodyDecision'
    ,'Hlt2SingleMuonDecision'
    ,'Hlt2SingleMuonHighPTDecision'
    ,'Hlt2SingleMuonLowPTDecision'
    ,'Hlt2SingleMuonRareDecision'
    ,'Hlt2SingleMuonVHighPTDecision'
    ,'Hlt2DiMuonDetachedDecision'
    ,'Hlt2DiMuonDetachedHeavyDecision'
    ,'Hlt2DiMuonDetachedJPsiDecision'
    ,'Hlt2DiMuonDetachedPsi2SDecision'
    ,'Hlt2SingleElectronTFLowPtDecision'
    ,'Hlt2SingleElectronTFHighPtDecision'
    ,'Hlt2DiElectronHighMassDecision'
    ,'Hlt2DiElectronBDecision'
    ,'Hlt2B2HHLTUnbiasedDecision'
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
    ,'Hlt2MuonFromHLT1Decision'
    ,'Hlt2DiMuonDecision'
    ,'Hlt2DiMuonLowMassDecision'
    ,'Hlt2DiMuonJPsiDecision'
    ,'Hlt2DiMuonJPsiHighPTDecision'
    ,'Hlt2DiMuonPsi2SDecision'
    ,'Hlt2DiMuonBDecision'
]

triglist = l0_lines + hlt1_lines + hlt2_lines

TISTOSTool = TupleToolTISTOS('TISTOSTool')
TISTOSTool.VerboseL0   = True
TISTOSTool.VerboseHlt1 = True
TISTOSTool.VerboseHlt2 = True
TISTOSTool.TriggerList = triglist[:]

# change TOSFracMu for TISTOS bug
TISTOSTool.addTool(TriggerTisTos, name = 'TriggerTisTos')
TISTOSTool.TriggerTisTos.TOSFracMuon = 0.
TISTOSTool.TriggerTisTos.TOSFracEcal = 0.
TISTOSTool.TriggerTisTos.TOSFracHcal = 0.

LoKi_B = LoKi__Hybrid__TupleTool('LoKi_B')
LoKi_B.Variables =  {
     'ETA'                    : 'ETA'
    ,'PHI'                    : 'PHI'
    ,'Y'                      : 'Y'
    ,'LV01'                   : 'LV01'
    ,'LV02'                   : 'LV02'
    ,'LOKI_FDCHI2'            : 'BPVVDCHI2'
    ,'LOKI_FDS'               : 'BPVDLS'  # decay length significance to the best PV
    ,'LOKI_DIRA'              : 'BPVDIRA'
    ,'LOKI_DTF_CTAU'          : 'DTF_CTAU(0, True)'
    ,'LOKI_DTF_CTAUS'         : 'DTF_CTAUSIGNIFICANCE(0, True)'
    ,'LOKI_DTF_CHI2NDOF'      : 'DTF_CHI2NDOF(True)'
    ,'LOKI_DTF_CTAUERR'       : 'DTF_CTAUERR(0, True)'
    ,'LOKI_DTF_JpsiConstr'    : 'DTF_FUN(M, True, \'J/psi(1S)\')'
    ,'LOKI_DTF_JpsiPiConstr'  : 'DTF_FUN(M, True, strings([\'J/psi(1S)\', \'pi0\']))'
    ,'LOKI_DTF_BJpsiPiConstr' : 'DTF_FUN(M, True, strings([\'B0\' , \'J/psi(1S)\', \'pi0\']))'
    ,'LOKI_DTF_VCHI2NDOF'     : 'DTF_FUN(VFASPF(VCHI2/VDOF), True)'
    ,'JpsiOmegaMass'          : 'WM(\'J/psi(1S)\', \'omega(782)\')'
}

LoKi_Jpsi = LoKi__Hybrid__TupleTool('LoKi_Jpsi')
LoKi_Jpsi.Variables = {
     'ETA'         : 'ETA'
    ,'Y'           : 'Y'
    ,'LV01'        : 'LV01'
    ,'LV02'        : 'LV02'
    ,'LOKI_FDCHI2' : 'BPVVDCHI2'
    ,'LOKI_FDS'    : 'BPVDLS'
    ,'LOKI_DIRA'   : 'BPVDIRA'
}

LoKi_muon = LoKi__Hybrid__TupleTool('LoKi_muon')
LoKi_muon.Variables = {
     'ETA'       : 'ETA'
    ,'Y'         : 'Y'
    ,'NSHAREDMU' : 'NSHAREDMU'
}

LoKi_pion = LoKi__Hybrid__TupleTool('LoKi_pion')
LoKi_pion.Variables = {
     'ETA'       : 'ETA'
    ,'Y'         : 'Y'
}

LoKi_Tuple = LoKi__Hybrid__TupleTool('LoKi_Tuple')
LoKi_Tuple.Variables = {
     'IsNotE'   : 'PPINFO(LHCb.ProtoParticle.IsNotE, -1000)'
    ,'IsNotH'   : 'PPINFO(LHCb.ProtoParticle.IsNotH, -1000)'
    ,'PhotonID' : 'PPINFO(LHCb.ProtoParticle.PhotonID, -1000)'
    ,'IsPhoton' : 'PPINFO(LHCb.ProtoParticle.IsPhoton, -1000)'
    ,'Veto'     : 'PINFO(25019, -1)'  # ID given to 'pizero' by StrippingSelections.StrippingBandQ.StrippingPsiX0
    ,'LOKI_E'   : 'E'
}

# event tuple
from Configurables import LoKi__Hybrid__EvtTupleTool
LoKi_EvtTuple = LoKi__Hybrid__EvtTupleTool('LoKi_EvtTuple')
LoKi_EvtTuple.VOID_Variables = {
     'LoKi_nPVs'              : 'CONTAINS(\'Rec/Vertex/Primary\')'
    ,'LoKi_nSpdMult'          : 'CONTAINS(\'Raw/Spd/Digits\')'
    ,'LoKi_nVeloClusters'     : 'CONTAINS(\'Raw/Velo/Clusters\')'
    ,'LoKi_nVeloLiteClusters' : 'CONTAINS(\'Raw/Velo/LiteClusters\')'
    ,'LoKi_nITClusters'       : 'CONTAINS(\'Raw/IT/Clusters\')'
    ,'LoKi_nTTClusters'       : 'CONTAINS(\'Raw/TT/Clusters\')'
    ,'LoKi_nOThits'           : 'CONTAINS(\'Raw/OT/Times\')'
}


from GaudiConfUtils.ConfigurableGenerators import DecayTreeTuple as TUPLE
from PhysSelPython.Wrappers                import SimpleSelection
rd_selection = SimpleSelection(
    'Tuple'
    ,TUPLE
    ,[b2omega_selection]
    ## Properties:
    ,Decay    = '[B0]cc -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(omega(782) -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma) )'
    ,ToolList = tupletools
    ,Branches = {
         'B'       : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'Jpsi'    : '[B0]cc -> ^(J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'muplus'  : '[B0]cc ->  (J/psi(1S) -> ^mu+  mu-)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'muminus' : '[B0]cc ->  (J/psi(1S) ->  mu+ ^mu-)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'X'       : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-) ^(omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'hplus'   : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) -> ^pi+  pi-  (pi0 ->  gamma  gamma))'
        ,'hminus'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+ ^pi-  (pi0 ->  gamma  gamma))'
        ,'hzero'   : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi- ^(pi0 ->  gamma  gamma))'
        ,'gamma1'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  (pi0 -> ^gamma  gamma))'
        ,'gamma2'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma ^gamma))'
    }
)

tuple_B2psiomega = rd_selection.algorithm()

for particle in ['B', 'Jpsi', 'muplus', 'muminus', 'X', 'hplus', 'hminus', 'hzero', 'gamma1', 'gamma2']:
    tuple_B2psiomega.addTool(TupleToolDecay, name = particle)

# List of the reconstructed tuples
tuples = [
    tuple_B2psiomega
]

TupleToolTrackPosition       = TupleToolTrackPosition('TupleToolTrackPosition')
TupleToolTrackPosition.Z     = 7500.
TupleToolRecoStats           = TupleToolRecoStats('TupleToolRecoStats')
TupleToolRecoStats.Verbose   = True
TupleToolGeometry            = TupleToolGeometry('TupleToolGeometry')
TupleToolGeometry.RefitPVs   = True
TupleToolGeometry.Verbose    = True
TupleToolTrackInfo           = TupleToolTrackInfo('TupleToolTrackInfo')
TupleToolTrackInfo.Verbose   = True
TupleToolTrigger             = TupleToolTrigger('TupleToolTrigger')
TupleToolTrigger.Verbose     = True
TupleToolTrigger.TriggerList = triglist
TupleToolTrigger.OutputLevel = 6

for tup in tuples:
    # tup.ReFitPVs = True
    tup.ReFitPVs = True
    tup.IgnoreP2PVFromInputLocations = True  # it ignores refitted PVs created in earlier steps in the decay chain

    myPVRefitter = tup.addTool(LoKi__PVReFitter, name = 'myPVRefitter')
    myPVRefitter.CheckTracksByLHCbIDs = True
    myPVRefitter.DeltaChi2 = 0.01  # float, delta-chi2 stopping criteria, default 0.01
    myPVRefitter.DeltaDistance = 5 * micrometer  # float, delta-distance stopping criteria, default 5 um, units are millimetres
    myPVRefitter.OutputLevel = 3
    tup.PVReFitters.update({'': 'LoKi::PVReFitter/myPVRefitter'})

    tup.addTool(TupleToolTrackInfo)
    tup.addTool(TupleToolTrackPosition)
    tup.addTool(TupleToolRecoStats)
    tup.addTool(TupleToolGeometry)
    tup.addTool(TupleToolTrigger)

    # # specific tagging tuple tool
    # btag = tup.addTupleTool('TupleToolTagging')
    # btag.UseFTfromDST = True
    # btag.Verbose = True
    # btag.AddMVAFeatureInfo = True

    if MODE == 'MC':
        tup.addTupleTool('TupleToolMCTruth')
        tup.addTupleTool('TupleToolMCBackgroundInfo')

    tup.addTool(LoKi_EvtTuple)
    tup.ToolList += ['LoKi::Hybrid::EvtTupleTool/LoKi_EvtTuple']
    tup.addTool(LoKi_Tuple)
    tup.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_Tuple']

    tup.B.addTool( LoKi_B )
    tup.B.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_B']
    tup.Jpsi.addTool( LoKi_Jpsi )
    tup.Jpsi.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_Jpsi']
    tup.muplus.addTool(LoKi_muon)
    tup.muplus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_muon']
    tup.muminus.addTool(LoKi_muon)
    tup.muminus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_muon']
    tup.hplus.addTool(LoKi_pion)
    tup.hplus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_pion']
    tup.hminus.addTool(LoKi_pion)
    tup.hminus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_pion']
    tup.hzero.addTool(LoKi_pion)
    tup.hzero.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_pion']
    for particle in [tup.B, tup.Jpsi]:
        particle.addTool(TISTOSTool, name = 'TISTOSTool')
        particle.ToolList += ['TupleToolTISTOS/TISTOSTool']

    ## refit with mass constraint
    tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsi']
    tup.B.addTool(TupleToolDecayTreeFitter('ConstJpsi'))
    tup.B.ConstJpsi.Verbose = True
    tup.B.ConstJpsi.UpdateDaughters = True
    tup.B.ConstJpsi.constrainToOriginVertex = True
    tup.B.ConstJpsi.daughtersToConstrain = ['J/psi(1S)']

    # tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiNoPV']
    # tup.B.addTool(TupleToolDecayTreeFitter('ConstJpsiNoPV'))
    # tup.B.ConstJpsiNoPV.Verbose = True
    # tup.B.ConstJpsiNoPV.UpdateDaughters = True
    # tup.B.ConstJpsiNoPV.constrainToOriginVertex = False
    # tup.B.ConstJpsiNoPV.daughtersToConstrain = ['J/psi(1S)']

    tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsi']
    tup.B.addTool(TupleToolDecayTreeFitter('ConstBJpsi'))
    tup.B.ConstBJpsi.Verbose = True
    tup.B.ConstBJpsi.UpdateDaughters = True
    tup.B.ConstBJpsi.constrainToOriginVertex = True
    tup.B.ConstBJpsi.daughtersToConstrain = ['B0', 'J/psi(1S)']

    # tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsiNoPV']
    # tup.B.addTool(TupleToolDecayTreeFitter('ConstBJpsiNoPV'))
    # tup.B.ConstBJpsiNoPV.Verbose = True
    # tup.B.ConstBJpsiNoPV.UpdateDaughters = True
    # tup.B.ConstBJpsiNoPV.constrainToOriginVertex = False
    # tup.B.ConstBJpsiNoPV.daughtersToConstrain = ['B0', 'J/psi(1S)']

    tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiPi0']
    tup.B.addTool(TupleToolDecayTreeFitter('ConstJpsiPi0'))
    tup.B.ConstJpsiPi0.Verbose = True
    tup.B.ConstJpsiPi0.UpdateDaughters = True
    tup.B.ConstJpsiPi0.constrainToOriginVertex = True
    tup.B.ConstJpsiPi0.daughtersToConstrain = ['J/psi(1S)', 'pi0']

    # tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiPi0NoPV']
    # tup.B.addTool(TupleToolDecayTreeFitter('ConstJpsiPi0NoPV'))
    # tup.B.ConstJpsiPi0NoPV.Verbose = True
    # tup.B.ConstJpsiPi0NoPV.UpdateDaughters = True
    # tup.B.ConstJpsiPi0NoPV.constrainToOriginVertex = False
    # tup.B.ConstJpsiPi0NoPV.daughtersToConstrain = ['J/psi(1S)', 'pi0']

    tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsiPi0']
    tup.B.addTool(TupleToolDecayTreeFitter('ConstBJpsiPi0'))
    tup.B.ConstBJpsiPi0.Verbose = True
    tup.B.ConstBJpsiPi0.UpdateDaughters = True
    tup.B.ConstBJpsiPi0.constrainToOriginVertex = True
    tup.B.ConstBJpsiPi0.daughtersToConstrain = ['B0', 'J/psi(1S)', 'pi0']

    # tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsiPi0NoPV']
    # tup.B.addTool(TupleToolDecayTreeFitter('ConstBJpsiPi0NoPV'))
    # tup.B.ConstBJpsiPi0NoPV.Verbose = True
    # tup.B.ConstBJpsiPi0NoPV.UpdateDaughters = True
    # tup.B.ConstBJpsiPi0NoPV.constrainToOriginVertex = False
    # tup.B.ConstBJpsiPi0NoPV.daughtersToConstrain = ['B0', 'J/psi(1S)', 'pi0']

    tup.B.ToolList += ['TupleToolDecayTreeFitter/ConstOnlyPV']
    tup.B.addTool(TupleToolDecayTreeFitter('ConstOnlyPV'))
    tup.B.ConstOnlyPV.Verbose = True
    tup.B.ConstOnlyPV.UpdateDaughters = True
    tup.B.ConstOnlyPV.constrainToOriginVertex = True

# Force update of CondDB to use proper momentum scaling
_db = None
if mode == 'DATA':
    from Configurables import CondDB
    _db = CondDB(LatestGlobalTagByDataType = '2016')
mag_tag = 'u' if mag == 'Up' else 'd'
db = dict()
db['CondDBtag'] = _db.CondDBtag if mode == 'DATA' else 'sim-20170721-2-vc-m{}100'.format(mag_tag)
db['DDDBtag']   = _db.DDDBtag if mode == 'DATA' else 'dddb-20170721-3'

## primary vertex selection
from Configurables import CheckPV
checkpv = CheckPV()

from Configurables import TrackScaleState, TrackSmearState
smear = TrackScaleState('TrackScaleState') if mode == 'DATA' else TrackSmearState('TrackSmearState')

from PhysSelPython.Wrappers import SelectionSequence
rd_SEQ = SelectionSequence('DATA', rd_selection)
mc_SEQ = SelectionSequence('MC', mc_selection)


###################### DAVINCI SETTINGS ############################################

daVinci = DaVinci(
     EvtMax         = EVTMAX
    ,InputType      = inputType
    ,RootInTES      = rootInTES
    ,TupleFile      = 'BdJpsiOmega.root'
    ,HistogramFile  = 'DVHistos.root'
    ,DataType       = '2016'
    ,Simulation     = sim
    ,Lumi           = lum
    ,UserAlgorithms = [checkpv, smear, mc_alg, mc_SEQ.sequence(), rd_SEQ.sequence()]
    ,CondDBtag      = db['CondDBtag']
    ,DDDBtag        = db['DDDBtag']
)

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

###################################################################################
####################### THE END ###################################################
###################################################################################
