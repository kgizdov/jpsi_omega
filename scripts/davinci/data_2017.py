# Copyright
# Greig Cowan 2015
# Konstantin Gizdov 2016


import GaudiKernel.SystemOfUnits as Units
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

EVTMAX      = -1
MODE        = 'DATA'
OUTPUTLEVEL = ERROR
LOC         = True

# # Use the local input data
# from GaudiConf import IOHelper
# if LOC == True:
#     IOHelper().inputFiles([
#         '/afs/cern.ch/work/k/kgizdov/00041162_00000046_1.psix0.mdst'
#     ], clear=True)

## # =============================================================================
## ## read PSIX0.MDST
## # =============================================================================

rootInTES = '/Event/PSIX0'
location  = 'Phys/SelB2PsiOmegaForPsiX0/Particles'
from PhysSelPython.Wrappers import AutomaticData
b2omega_selection = AutomaticData( location )


# ## # =============================================================================
# ## ## run PSIX0 WG-selections over ALLSTREAM.DST MC
# ## # =============================================================================
# jpsi_name  = 'FullDSTDiMuonJpsi2MuMuDetachedLine'
# # jpsi_name  = 'SelB2PsiOmegaForPsiX0'
# # jpsi_line  = '/Event/AllStream/Dimuon/Phys/%s/Particles' % jpsi_name
# jpsi_line  = '/Event/AllStreams/Phys/%s/Particles' % jpsi_name

# if MODE == 'DATA':
#     jpsi_line  = '/Event/PSIX0/Phys/%s/Particles' % jpsi_name

# import StrippingSelections.StrippingBandQ.StrippingPsiX0          as PSIX0
# psix0  = PSIX0.PsiX0Conf  (
#     'PsiX0'          ,
#     config = {
#         # 'NOPIDHADRONS' : True          ,  ## important here!!!
#         'DIMUONLINES'  : [ jpsi_line ]
#         # 'PsiX0Lines'  : [ jpsi_line ]
#         }
#     )

# b2omega_selection = psix0.b2omega()


#########################################################################################################
# Set up the MCDecayTreeTuples for each of the decays that we are interested in.
# We want to save all of the generated events for each mode.
#########################################################################################################
# from Configurables import MCDecayTreeTuple, MCTupleToolKinematic, MCTupleToolHierarchy, LoKi__Hybrid__MCTupleTool

# # LoKi variables
# LoKi_Photos = LoKi__Hybrid__MCTupleTool("LoKi_Photos")
# LoKi_Photos.Variables = {
#     "nPhotons" : "MCNINTREE ( ('gamma'==MCABSID) )",
#     "MC_PT"    : "MCPT",
#     "MC_THETA" : "MCTHETA",
#     "MC_ETA"   : "MCETA",
#     "MC_PHI"   : "MCPHI",
#     "MC_ABSID" : "MCABSID"
#   }

# from GaudiConfUtils.ConfigurableGenerators import MCDecayTreeTuple as MCTUPLE
# from PhysSelPython.Wrappers                import SimpleSelection

# mc_selection = SimpleSelection (
#     'MCTuple'
#     , MCTUPLE
#     , [ b2omega_selection ]
#     ## properties
#     , Decay = " [B0]cc => ^(J/psi(1S) => ^mu+ ^mu- ) ^(omega(782) ==> ^pi+ ^pi- ^(pi0 => ^gamma ^gamma) ) "
#     , Branches = {
#           'B0'      : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'Jpsi'    : "[B0]cc => ^(J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'muplus'  : "[B0]cc =>  (J/psi(1S) => ^mu+  mu- )  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'muminus' : "[B0]cc =>  (J/psi(1S) =>  mu+ ^mu- )  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'omega'   : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- ) ^(omega(782) ==>  pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'piplus'  : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==> ^pi+  pi-  (pi0 =>  gamma  gamma) )"
#         , 'piminus' : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+ ^pi-  (pi0 =>  gamma  gamma) )"
#         , 'pizero'  : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+  pi- ^(pi0 =>  gamma  gamma) )"
#         , 'gamma1'  : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+  pi-  (pi0 => ^gamma  gamma) )"
#         , 'gamma2'  : "[B0]cc =>  (J/psi(1S) =>  mu+  mu- )  (omega(782) ==>  pi+  pi-  (pi0 =>  gamma ^gamma) )"
#         }
#     )
# mctuple_B2psiomega = mc_selection.algorithm()


# # List of the mc tuples
# mctuples = [
#         mctuple_B2psiomega
#   ]

# for tup in mctuples:
#     tup.addTool(MCTupleToolKinematic())
#     tup.MCTupleToolKinematic.Verbose=True
#     tup.addTool(LoKi_Photos)
#     tup.ToolList  = [ "MCTupleToolHierarchy"
#             , "MCTupleToolKinematic"
#             , "LoKi::Hybrid::MCTupleTool/LoKi_Photos" # doesn't work with DaVinci v36r6
#             ]
#     tup.addTool(TupleToolMCTruth, name = "TruthTool")
#     tup.addTool(TupleToolMCBackgroundInfo, name = "BackgroundInfo")
#     tup.ToolList += ["TupleToolMCTruth/TruthTool"]
#     tup.ToolList += ["TupleToolMCBackgroundInfo/BackgroundInfo"]

# if OUTPUTLEVEL == DEBUG:
#   from Configurables import PrintMCTree, PrintMCDecayTreeTool
#   mctree = PrintMCTree("PrintTrue")
#   mctree.addTool( PrintMCDecayTreeTool )
#   mctree.PrintMCDecayTreeTool.Information = "Name M P Px Py Pz Pt Vx Vy Vz"
#   mctree.ParticleNames = [ "B+", "B-" ]
#   mctree.Depth = 3  # down to the K and mu

#########################################################################################################
# Now set up the DecayTreeTuples for the reconstructed particles
#########################################################################################################
tupletools = []
tupletools.append('TupleToolKinematic')
tupletools.append('TupleToolGeometry')
tupletools.append('TupleToolTrackInfo')
tupletools.append('TupleToolPid')
tupletools.append('TupleToolRecoStats')
tupletools.append('TupleToolEventInfo')
triglist = [
     'L0PhysicsDecision'
    ,'L0MuonDecision'
    ,'L0DiMuonDecision'
    ,'L0MuonHighDecision'
    ,'L0HadronDecision'
    ,'L0ElectronDecision'
    ,'L0PhotonDecision'
    ,'Hlt1DiMuonHighMassDecision'
    ,'Hlt1DiMuonLowMassDecision'
    ,'Hlt1SingleMuonNoIPDecision'
    ,'Hlt1SingleMuonHighPTDecision'
    ,'Hlt1TrackAllL0Decision'
    ,'Hlt1TrackMuonDecision'
    ,'Hlt1TrackPhotonDecision'
    ,'Hlt1L0AnyDecision'
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
TISTOSTool = TupleToolTISTOS('TISTOSTool')
TISTOSTool.VerboseL0   = True
TISTOSTool.VerboseHlt1 = True
TISTOSTool.VerboseHlt2 = True
TISTOSTool.TriggerList = triglist[:]
TISTOSTool.addTool(TriggerTisTos, name = 'TriggerTisTos')

LoKi_B0 = LoKi__Hybrid__TupleTool('LoKi_B0')
LoKi_B0.Variables =  {
      'ETA'                    : 'ETA'
    , 'PHI'                    : 'PHI'
    , 'FDCHI2'                 : 'BPVVDCHI2'
    , 'BPVDLS'                 : 'BPVDLS'  # decay length significance to the best PV
    , 'DIRA'                   : 'BPVDIRA'
    , 'DTF_CTAU'               : 'DTF_CTAU( 0, True )'
    , 'DTF_CTAUS'              : 'DTF_CTAUSIGNIFICANCE( 0, True )'
    , 'DTF_CHI2NDOF'           : 'DTF_CHI2NDOF( True )'
    , 'DTF_CTAUERR'            : 'DTF_CTAUERR( 0, True )'
    , 'DTF_MASS_constr'        : 'DTF_FUN ( M , True , strings([\'J/psi(1S)\', \'pi0\']) )'
    , 'DTF_VCHI2NDOF'          : 'DTF_FUN ( VFASPF(VCHI2/VDOF) , True )'
    }

LoKi_Jpsi = LoKi__Hybrid__TupleTool('LoKi_Jpsi')
LoKi_Jpsi.Variables =  {
    'BPVDLS' : 'BPVDLS'  # decay length significance to the best PV
}

LoKi_Mu = LoKi__Hybrid__TupleTool('LoKi_Mu')
LoKi_Mu.Variables =  {
    'NSHAREDMU' : 'NSHAREDMU'
}


from GaudiConfUtils.ConfigurableGenerators import DecayTreeTuple as TUPLE
from PhysSelPython.Wrappers                import SimpleSelection
rd_selection = SimpleSelection (
    'Tuple'
    , TUPLE
    , [ b2omega_selection ]
    ## Properties:
    , Decay    = '[B0]cc -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(omega(782) -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma) )'
    , ToolList = tupletools
    , Branches = {
        #
          'B0'      : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'Jpsi'    : '[B0]cc -> ^(J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'muplus'  : '[B0]cc ->  (J/psi(1S) -> ^mu+  mu- )  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'muminus' : '[B0]cc ->  (J/psi(1S) ->  mu+ ^mu- )  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'omega'   : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- ) ^(omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'piplus'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) -> ^pi+  pi-  (pi0 ->  gamma  gamma) )'
        , 'piminus' : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+ ^pi-  (pi0 ->  gamma  gamma) )'
        , 'pizero'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+  pi- ^(pi0 ->  gamma  gamma) )'
        , 'gamma1'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+  pi-  (pi0 -> ^gamma  gamma) )'
        , 'gamma2'  : '[B0]cc ->  (J/psi(1S) ->  mu+  mu- )  (omega(782) ->  pi+  pi-  (pi0 ->  gamma ^gamma) )'
    }
)

tuple_B2psiomega = rd_selection.algorithm()

for particle in ['B0', 'Jpsi', 'muplus', 'muminus', 'omega', 'piplus', 'piminus', 'pizero', 'gamma1', 'gamma2']:
    tuple_B2psiomega.addTool(TupleToolDecay, name = particle)

# List of the reconstructed tuples
tuples = [tuple_B2psiomega]

for tup in tuples:
    # tup.ReFitPVs = True
    if MODE == 'MC':
        tup.addTool(TupleToolMCTruth, name = 'TruthTool')
        tup.addTool(TupleToolMCBackgroundInfo, name = 'BackgroundInfo')
        tup.ToolList += ['TupleToolMCTruth/TruthTool']
        tup.ToolList += ['TupleToolMCBackgroundInfo/BackgroundInfo']

    tup.B0.addTool(LoKi_B0)
    tup.B0.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_B0']
    tup.Jpsi.addTool(LoKi_Jpsi)
    tup.Jpsi.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_Jpsi']
    tup.muplus.addTool(LoKi_Mu)
    tup.muplus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_Mu']
    tup.muminus.addTool(LoKi_Mu)
    tup.muminus.ToolList += ['LoKi::Hybrid::TupleTool/LoKi_Mu']
    for particle in [ tup.B0 ]:
        particle.addTool(TISTOSTool, name = 'TISTOSTool')
        particle.ToolList += ['TupleToolTISTOS/TISTOSTool']



from PhysSelPython.Wrappers import SelectionSequence
rd_SEQ = SelectionSequence('DATA', rd_selection)


###################### DAVINCI SETTINGS ############################################

lum = True
sim = False

if MODE == 'MC':
    lum = False
    sim = True

daVinci = DaVinci (
      EvtMax             = EVTMAX
    , RootInTES          = rootInTES
    , InputType          = 'MDST'
    , TupleFile          = 'BdJpsiOmega.root'
    , HistogramFile      = 'DVHistos.root'
    , DataType           = '2017'
    , Simulation         = sim
    , Lumi               = lum
    , UserAlgorithms     =  [rd_SEQ.sequence()]
    )

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

###################################################################################
####################### THE END ###################################################
###################################################################################
