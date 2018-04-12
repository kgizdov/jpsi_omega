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

from PhysSelPython.Wrappers import AutomaticData, SimpleSelection, Selection, MergedSelection, CombineSelection, SelectionSequence
from GaudiConfUtils.ConfigurableGenerators import DecayTreeTuple, Pi0Veto__Tagger2g, DaVinci__N3BodyDecays
from Configurables import FilterDesktop
from Configurables import DaVinci
from Configurables import GaudiSequencer
from Configurables import CondDB
from Configurables import TupleToolDecay, TupleToolTrackPosition, TupleToolRecoStats, TupleToolGeometry, TupleToolTrackInfo, TupleToolTagging
from Configurables import LoKi__Hybrid__TupleTool
from Configurables import LoKi__Hybrid__EvtTupleTool
from Configurables import LoKi__PVReFitter
from Configurables import MCTupleToolHierarchy
from Configurables import TupleToolMCTruth
from Configurables import TupleToolMCBackgroundInfo
from Configurables import TupleToolTrigger, TupleToolTISTOS, TriggerTisTos
from Configurables import TupleToolDecayTreeFitter

## DaVinci settings
mode        = 'DATA'              # DATA or MC
evtMax      = 1000                  # number of events to read, -1 == all
inputType   = 'DST'               # input file format
rootInTES   = ''                  # need to specify if not DST
dataType    = '2016'              # year of input
tupleFile   = 'BdJpsiOmega.root'  # nTuple file name
histFile    = 'DVHistos.root'     # histogram file name
printFreq   = 1000                # log output frequency
outputLevel = ERROR               # log output verbosity
skipEvents  = 0                   # Events to skip from beginning
local       = True                # if running locally

# Data or Simulation settings
lum         = True if mode == 'DATA' else False
sim         = not lum

from GaudiConf import IOHelper
# Use the local input data
if local:
    IOHelper().inputFiles([
        # '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/00041840_00000322_1.dimuon_11.dst'      # 2011
        '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/00069597_00000869_1.dimuon.dst'         # 2016 Str28r1 MagDown
        # '/afs/cern.ch/work/k/kgizdov/Git/BsJpsiPhi/davinci/00061346_00007805_1.dimuon.dst'  # 2016 Str26 MagDown
    ], clear=True)

## Triggers
triglist = [
]

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

# Read DIMUON.DST
jpsi_name        = 'FullDSTDiMuonJpsi2MuMuDetachedLine'
psi2_name        = 'FullDSTDiMuonPsi2MuMuDetachedLine'

jpsi_line        = '/Event/Dimuon/Phys/%s/Particles' % jpsi_name
psi2s_line       = '/Event/Dimuon/Phys/%s/Particles' % psi2_name

jpsi_loc = AutomaticData(jpsi_line)
psi2_loc = AutomaticData(psi2s_line)

# Merge psi lines, as per PSIX0 stream
MergedPsiSelection = MergedSelection('MergedPsiSelection', RequiredSelections = [jpsi_loc, psi2_loc])
FilterJpsiCut = FilterDesktop('FilterJpsiCut')
FilterJpsiCut.Code = '(ADAMASS(\'J/psi(1S)\') < 150.0 * MeV)'
FilteredJPsiSelection = Selection('FilteredJPsiSelection', Algorithm = FilterJpsiCut, RequiredSelections = [MergedPsiSelection])

# Get all pions
# StdAllLooseANNPions has ProbNNpi > 0.05, don't like that
pions  = AutomaticData(Location = '/Event/Phys/StdAllLoosePions/Particles')

# Get all variants of Pi0->: gamma gamma; gamma e+ e-; e+ e- e+ e-
pi0gg  = AutomaticData(Location = '/Event/Phys/StdLoosePi02gg/Particles')
pi0gee = AutomaticData(Location = '/Event/Phys/StdLoosePi02gee/Particles')
pi04e  = AutomaticData(Location = '/Event/Phys/StdLoosePi024e/Particles')

# Filter Pi0 selections with gamma for photon PT
FilterPi0Cut = FilterDesktop('FilterPi0Cut')
FilterPi0Cut.Code = '(250 * MeV < MINTREE(\'gamma\' == ID, PT))'
Pi0ggFiltered  = Selection('Pi0ggFiltered', Algorithm = FilterPi0Cut, RequiredSelections = [pi0gg])
Pi0geeFiltered = Selection('Pi0geeFiltered', Algorithm = FilterPi0Cut, RequiredSelections = [pi0gee])

# Use Tagger2g to get good photons
Pi0Vetoed     = SimpleSelection('Pi0Vetoed', Pi0Veto__Tagger2g, [Pi0ggFiltered], MassWindow = 45 * MeV, MassChi2 = -1, ExtraInfoIndex = 25020)  # unique ExtraInfoIndex!
# Pi0VetoedChi2 = SimpleSelection('Pi0VetoedChi2', Pi0Veto__Tagger2g, [Pi0ggFiltered], MassWindow = 45 * MeV, MassChi2 = 20, ExtraInfoIndex = 25021)  # unique ExtraInfoIndex!

# Merge all Pi0 into one selection
Pi0MergedSelection = MergedSelection('Pi0MergedSelection', RequiredSelections = [Pi0Vetoed, Pi0geeFiltered, pi04e])

# Filter Pion selections
FilterPionCut = FilterDesktop('FilterPionCut')
# Check TRCHI2NDOF, ETA, P, MIPCHI2DV; TRGHOSTPROB < 0.4 in Rec already
# FilterPionCut.Code = '(PT > 200.0 * MeV) & (CLONEDIST > 5000) & (TRGHOSTPROB < 0.5) & (TRCHI2DOF < 4.0) & in_range(2.0, ETA, 5.0) & in_range(3.2 * GeV, P, 150.0 * GeV) & HASRICH & (MIPCHI2DV() > 4.0)'
FilterPionCut.Code = '(PT > 200.0 * MeV) & (CLONEDIST > 5000) & (TRGHOSTPROB < 0.4) & (TRCHI2DOF < 5.0) & HASRICH'
PionFilteredSelection = Selection('PionFilteredSelection', Algorithm = FilterPionCut, RequiredSelections = [pions])

    # ,CombinationCut   = '(APT > 0.7 * GeV) & (ADAMASS(\'omega(782)\') < 100.0 * MeV)'
    # ,MotherCut        = '(PT > 0.7 * GeV) & (VFASPF(VCHI2) < 25.0)'
Omega3Body = SimpleSelection(
    'Omega3Body'
    ,DaVinci__N3BodyDecays
    ,[PionFilteredSelection, Pi0MergedSelection]
    ,DecayDescriptor  = 'omega(782) -> pi+ pi- pi0'
    ,Combination12Cut = '(AM < 1.0 * GeV) & (ACHI2DOCA(1,2) < 30)'
    ,CombinationCut   = '(ADAMASS(\'omega(782)\') < 100.0 * MeV)'
    ,MotherCut        = '(VFASPF(VCHI2) < 25.0)'
)

BdJpsiOmegaCombination = CombineSelection(
    'BdJpsiOmegaCombination'
    ,[MergedPsiSelection, Omega3Body]
    ,DecayDescriptor = 'B0 -> J/psi(1S) omega(782)'
    ,DaughtersCuts   = {
        'omega(782)' : 'PT > 0.5 * GeV'
    }
    ,CombinationCut  = 'in_range(4.50 * GeV, AM, 6.00 * GeV)'
    ,MotherCut       = '(VFASPF(VCHI2PDOF) < 20)'  # & (DTF_CTAU(0,True) > 0.0598)'  # equiv to DecayTreeFitter::tau(B) > 0.2 ps
)

tl = [
     'TupleToolTrigger'
    ,'TupleToolGeometry'
    ,'TupleToolKinematic'
    ,'TupleToolPropertime'
    ,'TupleToolPrimaries'
    ,'TupleToolEventInfo'
    ,'TupleToolTrackInfo'
    ,'TupleToolTagging'
    ,'TupleToolPid'
    ,'TupleToolANNPID'
    ,'TupleToolRecoStats'
    ,'TupleToolTrackPosition'
    ,'TupleToolL0Calo'
    ,'TupleToolL0Data'
    ,'TupleToolTISTOS'
]

BdJpsiOmega = SimpleSelection(
    'Tuple'
    ,DecayTreeTuple
    ,[BdJpsiOmegaCombination]
    ## Properties:
    , Decay    = '[B0]cc -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(omega(782) -> ^pi+ ^pi- ^pi0)'
    , ToolList = tl
    , Branches = {
         'B'       : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  pi0)'
        ,'Jpsi'    : '[B0]cc -> ^(J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi-  pi0)'
        ,'muplus'  : '[B0]cc ->  (J/psi(1S) -> ^mu+  mu-)  (omega(782) ->  pi+  pi-  pi0)'
        ,'muminus' : '[B0]cc ->  (J/psi(1S) ->  mu+ ^mu-)  (omega(782) ->  pi+  pi-  pi0)'
        ,'X'       : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-) ^(omega(782) ->  pi+  pi-  pi0)'
        ,'hplus'   : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) -> ^pi+  pi-  pi0)'
        ,'hminus'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+ ^pi-  pi0)'
        ,'hzero'   : '[B0]cc ->  (J/psi(1S) ->  mu+  mu-)  (omega(782) ->  pi+  pi- ^pi0)'
    }
)

tuple_bdjpsiomega = BdJpsiOmega.algorithm()

tuples = [tuple_bdjpsiomega]

for particle in ['B', 'Jpsi', 'muplus', 'muminus', 'X', 'hplus', 'hminus', 'hzero']:
    tuple_bdjpsiomega.addTool(TupleToolDecay, name = particle)

tuple_bdjpsiomega.ReFitPVs = True
tuple_bdjpsiomega.IgnoreP2PVFromInputLocations = True  # it ignores refitted PVs created in earlier steps in the decay chain

myPVRefitter = LoKi__PVReFitter('myPVRefitter')
myPVRefitter.CheckTracksByLHCbIDs = True
myPVRefitter.DeltaChi2 = 0.01  # float, delta-chi2 stopping criteria, default 0.01
myPVRefitter.DeltaDistance = 5 * micrometer  # float, delta-distance stopping criteria, default 5 um, units are millimeters

tuple_bdjpsiomega.addTool(myPVRefitter)
tuple_bdjpsiomega.PVReFitters.update({'': 'LoKi::PVReFitter/myPVRefitter'})

tuple_bdjpsiomega.ToolList += tl

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

tuple_bdjpsiomega.B.addTool(TISTOSTool, name = 'TISTOSTool')
tuple_bdjpsiomega.B.ToolList += ['TupleToolTISTOS/TISTOSTool']

tuple_bdjpsiomega.Jpsi.addTool(TISTOSTool, name = 'TISTOSTool')
tuple_bdjpsiomega.Jpsi.ToolList += ['TupleToolTISTOS/TISTOSTool']

TupleToolTrackPosition       = TupleToolTrackPosition('TupleToolTrackPosition')
TupleToolTrackPosition.Z     = 7500.
TupleToolRecoStats           = TupleToolRecoStats('TupleToolRecoStats')
TupleToolRecoStats.Verbose   = True
TupleToolGeometry            = TupleToolGeometry('TupleToolGeometry')
TupleToolGeometry.RefitPVs   = True
TupleToolGeometry.Verbose    = True
TupleToolTrackInfo           = TupleToolTrackInfo('TupleToolTrackInfo')
TupleToolTrackInfo.Verbose   = True
TupleToolTagging             = TupleToolTagging('TupleToolTagging')
TupleToolTagging.Verbose     = True
TupleToolTrigger             = TupleToolTrigger('TupleToolTrigger')
TupleToolTrigger.Verbose     = True
TupleToolTrigger.TriggerList = triglist
TupleToolTrigger.OutputLevel = 6
tuple_bdjpsiomega.addTool(TupleToolTrackInfo)
tuple_bdjpsiomega.addTool(TupleToolTagging)
tuple_bdjpsiomega.addTool(TupleToolTrackPosition)
tuple_bdjpsiomega.addTool(TupleToolRecoStats)
tuple_bdjpsiomega.addTool(TupleToolGeometry)
tuple_bdjpsiomega.addTool(TupleToolTrigger)

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

tuple_bdjpsiomega.ToolList += ['LoKi::Hybrid::EvtTupleTool/LoKi_EvtTuple']
tuple_bdjpsiomega.addTool(LoKi_EvtTuple)

# specific tagging tuple tool
tuple_bdjpsiomega.B.ToolList += ['TupleToolTagging']
tuple_bdjpsiomega.B.addTool(TupleToolTagging, name = 'TupleToolTagging')
tuple_bdjpsiomega.B.TupleToolTagging.Verbose = True
tuple_bdjpsiomega.B.TupleToolTagging.StoreTaggersInfo = True

LoKi_B = LoKi__Hybrid__TupleTool('LoKi_B')
LoKi_B.Variables = {
     'JpsiOmegaMass'         : 'WM(\'J/psi(1S)\',\'omega(782)\')'
    ,'ETA'                   : 'ETA'
    ,'PHI'                   : 'PHI'
    ,'Y'                     : 'Y'
    ,'LV01'                  : 'LV01'
    ,'LV02'                  : 'LV02'
    ,'LOKI_FDCHI2'           : 'BPVVDCHI2'
    ,'LOKI_FDS'              : 'BPVDLS'
    ,'LOKI_DIRA'             : 'BPVDIRA'
    ,'LOKI_DTF_CTAU'         : 'DTF_CTAU(0, True)'
    ,'LOKI_DTF_CTAUS'        : 'DTF_CTAUSIGNIFICANCE(0, True)'
    ,'LOKI_DTF_CHI2NDOF'     : 'DTF_CHI2NDOF(True)'
    ,'LOKI_DTF_CTAUERR'      : 'DTF_CTAUERR(0, True)'
    ,'LOKI_DTF_VCHI2NDOF'    : 'DTF_FUN(VFASPF(VCHI2/VDOF), True)'
    ,'LOKI_DTF_JpsiConstr'   : 'DTF_FUN(M, True, \'J/psi(1S)\')'
    ,'LOKI_DTF_JpsiOmConstr' : 'DTF_FUN(M, True, strings([\'J/psi(1S)\', \'omega(782)\']))'
}

tuple_bdjpsiomega.B.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_B']
tuple_bdjpsiomega.B.addTool(LoKi_B)

LoKi_Jpsi = LoKi__Hybrid__TupleTool("LoKi_Jpsi")
LoKi_Jpsi.Variables = {
     "ETA"         : "ETA"
    ,"Y"           : "Y"
    ,"LV01"        : "LV01"
    ,"LV02"        : "LV02"
    ,"LOKI_FDCHI2" : "BPVVDCHI2"
    ,"LOKI_FDS"    : "BPVDLS"
    ,"LOKI_DIRA"   : "BPVDIRA"
}

tuple_bdjpsiomega.Jpsi.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_Jpsi"]
tuple_bdjpsiomega.Jpsi.addTool(LoKi_Jpsi)

LoKi_muon = LoKi__Hybrid__TupleTool("LoKi_muon")
LoKi_muon.Variables = {
     'ETA'       : 'ETA'
    ,'Y'         : 'Y'
    ,'NSHAREDMU' : 'NSHAREDMU'
}
tuple_bdjpsiomega.muplus.ToolList  += ["LoKi::Hybrid::TupleTool/LoKi_muon"]
tuple_bdjpsiomega.muminus.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_muon"]
tuple_bdjpsiomega.muplus.addTool(LoKi_muon)
tuple_bdjpsiomega.muminus.addTool(LoKi_muon)

LoKi_pion = LoKi__Hybrid__TupleTool("LoKi_pion")
LoKi_pion.Variables = {
     'ETA'       : 'ETA'
    ,'Y'         : 'Y'
}
tuple_bdjpsiomega.hplus.ToolList  += ["LoKi::Hybrid::TupleTool/LoKi_pion"]
tuple_bdjpsiomega.hminus.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_pion"]
tuple_bdjpsiomega.hzero.ToolList  += ["LoKi::Hybrid::TupleTool/LoKi_pion"]
tuple_bdjpsiomega.hplus.addTool(LoKi_pion)
tuple_bdjpsiomega.hminus.addTool(LoKi_pion)
tuple_bdjpsiomega.hzero.addTool(LoKi_pion)

# # refit with mass constraint
# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsi']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsi'))
# tuple_bdjpsiomega.B.ConstJpsi.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsi.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsi.constrainToOriginVertex = True
# tuple_bdjpsiomega.B.ConstJpsi.daughtersToConstrain = ['J/psi(1S)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiNoPV']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsiNoPV'))
# tuple_bdjpsiomega.B.ConstJpsiNoPV.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsiNoPV.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsiNoPV.constrainToOriginVertex = False
# tuple_bdjpsiomega.B.ConstJpsiNoPV.daughtersToConstrain = ['J/psi(1S)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsi']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstBJpsi'))
# tuple_bdjpsiomega.B.ConstBJpsi.Verbose = True
# tuple_bdjpsiomega.B.ConstBJpsi.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstBJpsi.constrainToOriginVertex = True
# tuple_bdjpsiomega.B.ConstBJpsi.daughtersToConstrain = ['B0', 'J/psi(1S)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstBJpsiNoPV']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstBJpsiNoPV'))
# tuple_bdjpsiomega.B.ConstBJpsiNoPV.Verbose = True
# tuple_bdjpsiomega.B.ConstBJpsiNoPV.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstBJpsiNoPV.constrainToOriginVertex = False
# tuple_bdjpsiomega.B.ConstBJpsiNoPV.daughtersToConstrain = ['B0', 'J/psi(1S)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiOmega']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsiOmega'))
# tuple_bdjpsiomega.B.ConstJpsiOmega.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsiOmega.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsiOmega.constrainToOriginVertex = True
# tuple_bdjpsiomega.B.ConstJpsiOmega.daughtersToConstrain = ['J/psi(1S)', 'omega(782)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiOmegaNoPV']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsiOmegaNoPV'))
# tuple_bdjpsiomega.B.ConstJpsiOmegaNoPV.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsiOmegaNoPV.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsiOmegaNoPV.constrainToOriginVertex = False
# tuple_bdjpsiomega.B.ConstJpsiOmegaNoPV.daughtersToConstrain = ['J/psi(1S)', 'omega(782)']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiPi0']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsiPi0'))
# tuple_bdjpsiomega.B.ConstJpsiPi0.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsiPi0.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsiPi0.constrainToOriginVertex = True
# tuple_bdjpsiomega.B.ConstJpsiPi0.daughtersToConstrain = ['J/psi(1S)', 'pi0']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstJpsiPi0NoPV']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstJpsiPi0NoPV'))
# tuple_bdjpsiomega.B.ConstJpsiPi0NoPV.Verbose = True
# tuple_bdjpsiomega.B.ConstJpsiPi0NoPV.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstJpsiPi0NoPV.constrainToOriginVertex = False
# tuple_bdjpsiomega.B.ConstJpsiPi0NoPV.daughtersToConstrain = ['J/psi(1S)', 'pi0']

# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/ConstOnlyPV']
# tuple_bdjpsiomega.B.addTool(TupleToolDecayTreeFitter('ConstOnlyPV'))
# tuple_bdjpsiomega.B.ConstOnlyPV.Verbose = True
# tuple_bdjpsiomega.B.ConstOnlyPV.UpdateDaughters = True
# tuple_bdjpsiomega.B.ConstOnlyPV.constrainToOriginVertex = True

# ### Backgrounds
# # - eta  -> gamma gamma,
# # - eta  -> pi+ pi- pi0,
# # - eta' -> rho0 gamma
# # - eta' -> pi+ pi- (eta -> gamma gamma)

# # B -> JpsiEtaPrime(pi pi eta)
# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/B2JpsiEtaPrimeEta']
# B2JpsiEtaPrimeEta = TupleToolDecayTreeFitter(
#     'B2JpsiEtaPrimeEta'
#     ,Verbose = True
#     ,Substitutions = {
#         'Beauty -> Meson (omega(782) -> X+ X- ^pi0)': 'eta'
#     }
#     ,daughtersToConstrain = ['J/psi(1S)']
#     ,constrainToOriginVertex = True
# )
# tuple_bdjpsiomega.B.addTool(B2JpsiEtaPrimeEta)

# # B -> JpsiEtaPrime(rho0 gamma) or B -> Jpsi pi pi gamma
# tuple_bdjpsiomega.B.ToolList += ['TupleToolDecayTreeFitter/B2JpsiEtaPrimeRho']
# B2JpsiEtaPrimeRho = TupleToolDecayTreeFitter(
#     "B2JpsiEtaPrimeRho"
#     ,Verbose = True
#     ,Substitutions = {
#         'Beauty -> Meson (omega(782) -> X+ X- ^pi0)': 'gamma'
#     }
#     ,daughtersToConstrain = ['J/psi(1S)']
#     ,constrainToOriginVertex = True
# )
# tuple_bdjpsiomega.B.addTool(B2JpsiEtaPrimeRho)

# # B -> JpsiEta(pi pi pi)
# tuple_bdjpsiomega.B.ToolList += ["TupleToolDecayTreeFitter/B2JpsiEta"]
# B2JpsiEta = TupleToolDecayTreeFitter(
#     "B2JpsiEta"
#     ,Verbose = True
#     ,Substitutions = {
#         'Beauty -> Meson (^(omega(782) -> pi+ pi- pi0))': 'eta'
#     }
#     ,daughtersToConstrain = ["J/psi(1S)"]
#     ,constrainToOriginVertex = True
# )
# tuple_bdjpsiomega.B.addTool(B2JpsiEta)


## Force update of CondDB to use proper momentum scaling
from Configurables import CondDB
CondDB(LatestGlobalTagByDataType = '2016')

## primary vertex selection
from Configurables import CheckPV
checkpv = CheckPV()

from Configurables import TrackScaleState
smear = TrackScaleState('TrackScaleState')

from PhysSelPython.Wrappers import SelectionSequence
BdJpsiOmegaSequense = SelectionSequence('DATA', BdJpsiOmega)

# Configure DaVinci
from Configurables import DaVinci
DaVinci().UserAlgorithms = [checkpv, smear, BdJpsiOmegaSequense.sequence()]
DaVinci().DataType       = dataType
DaVinci().EvtMax         = evtMax
DaVinci().InputType      = inputType
DaVinci().PrintFreq      = printFreq
DaVinci().SkipEvents     = skipEvents
DaVinci().TupleFile      = tupleFile
DaVinci().HistogramFile  = histFile
DaVinci().Simulation     = sim
DaVinci().Lumi           = lum
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

###################################################################################
####################### THE END ###################################################
###################################################################################
