# Copyright
# Greig Cowan 2015
# Konstantin Gizdov 2016

# import StrippingPsiX0

import GaudiKernel.SystemOfUnits as Units
from Gaudi.Configuration import *

####
from StrippingConf.Configuration import StrippingConf, StrippingStream
from StrippingSettings.Utils import strippingConfiguration
from StrippingArchive.Utils import buildStreams
from StrippingArchive import strippingArchive
####

# from GaudiUtils import *
from GaudiConf import IOHelper
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

EVTMAX = -1
MODE = "MC"
OUTPUTLEVEL = ERROR

rootInTES = '/Event/PSIX0'
location='Phys/SelB2PsiOmegaForPsiX0/Particles'

# # Use the local input data
# IOHelper().inputFiles([
#     '/afs/cern.ch/work/k/kgizdov/00041170_00000020_1.psix0.mdst'
# ], clear=True)

#########################################################################################################
# Set up the MCDecayTreeTuples for each of the decays that we are interested in.
# We want to save all of the generated events for each mode.
#########################################################################################################
from Configurables import MCDecayTreeTuple, MCTupleToolKinematic, MCTupleToolHierarchy, LoKi__Hybrid__MCTupleTool

# LoKi variables
LoKi_Photos = LoKi__Hybrid__MCTupleTool("LoKi_Photos")
LoKi_Photos.Variables = {
    "nPhotons" : "MCNINTREE ( ('gamma'==MCABSID) )",
    "MC_PT"    : "MCPT",
    "MC_THETA" : "MCTHETA",
    "MC_ETA"   : "MCETA",
    "MC_PHI"   : "MCPHI",
    "MC_ABSID" : "MCABSID"
	}

# mctuple_B2Kmumu = MCDecayTreeTuple( 'MCTuple_B2Kmumu' )
mctuple_B2psiomega = MCDecayTreeTuple( 'MCTuple_B2psiomega' )
# mctuple_B2psiomega.Decay = "[ [ (Beauty & LongLived) --> ^(J/psi(1S) -> ^mu+ ^mu- ...) ^(omega(782) -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma) ) ]CC"
mctuple_B2psiomega.Decay = "[ (Beauty & LongLived) --> ^(J/psi(1S) -> ^mu+ ^mu- ...) ^(omega(782) -> ^pi+ ^pi- ^pi0 ) ]CC"
mctuple_B2psiomega.Branches = {
        # 'B'       : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'Jpsi'    : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'muplus'  : "[ (Beauty & LongLived) -->  (J/psi(1S) -> ^mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'muminus' : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+ ^mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'omega'   : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...) ^(omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'piplus'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) -> ^pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'piminus' : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+ ^pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'pizero'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi- ^(pi0 ->  gamma  gamma ) ) ]CC",
        # 'gamma1'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 -> ^gamma  gamma ) ) ]CC",
        # 'gamma2'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma ^gamma ) ) ]CC",
        #
        'B'       : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'Jpsi'    : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'omega'   : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...) ^(omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'muplus'  : "[ (Beauty & LongLived) -->  (J/psi(1S) -> ^mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'muminus' : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+ ^mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'piplus'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) -> ^pi+  pi-  pi0 ) ]CC",
        'piminus' : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+ ^pi-  pi0 ) ]CC",
        'pizero'  : "[ (Beauty & LongLived) -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi- ^pi0 ) ]CC",
        #
		# 'B'       : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+  mu- ...)  K+  ... ]CC",
		# 'Kplus'   : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+  mu- ...) ^K+  ... ]CC",
		# 'psi'     : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+  mu- ...)  K+  ... ]CC",
		# 'muplus'  : "[ (Beauty & LongLived) --> ^(J/psi(1S) -> ^mu+  mu- ...)  K+  ... ]CC",
		# 'muminus' : "[ (Beauty & LongLived) --> ^(J/psi(1S) ->  mu+ ^mu- ...)  K+  ... ]CC",
		}

# List of the mc tuples
mctuples = [
        mctuple_B2psiomega
	]

for tup in mctuples:
    tup.addTool(MCTupleToolKinematic())
    tup.MCTupleToolKinematic.Verbose=True
    tup.addTool(LoKi_Photos)
    tup.ToolList  = [ "MCTupleToolHierarchy"
            , "MCTupleToolKinematic"
            , "LoKi::Hybrid::MCTupleTool/LoKi_Photos" # doesn't work with DaVinci v36r6
            ]
    tup.addTool(TupleToolMCTruth, name = "TruthTool")
    tup.addTool(TupleToolMCBackgroundInfo, name = "BackgroundInfo")
    tup.ToolList += ["TupleToolMCTruth/TruthTool"]
    tup.ToolList += ["TupleToolMCBackgroundInfo/BackgroundInfo"]

if OUTPUTLEVEL == DEBUG:
	from Configurables import PrintMCTree, PrintMCDecayTreeTool
	mctree = PrintMCTree("PrintTrue")
	mctree.addTool( PrintMCDecayTreeTool )
	mctree.PrintMCDecayTreeTool.Information = "Name M P Px Py Pz Pt Vx Vy Vz"
	mctree.ParticleNames = [ "B+", "B-" ]
	mctree.Depth = 3  # down to the K and mu

#########################################################################################################
# Now set up the DecayTreeTuples for the reconstructed particles
#########################################################################################################
tupletools = []
tupletools.append("TupleToolKinematic")
tupletools.append("TupleToolGeometry")
tupletools.append("TupleToolTrackInfo")
tupletools.append("TupleToolPid")
tupletools.append("TupleToolRecoStats")
tupletools.append("TupleToolEventInfo")
triglist = [
	 "L0PhysicsDecision"
	,"L0MuonDecision"
	,"L0DiMuonDecision"
	,"L0MuonHighDecision"
	,"L0HadronDecision"
	,"L0ElectronDecision"
	,"L0PhotonDecision"
	,"Hlt1DiMuonHighMassDecision"
	,"Hlt1DiMuonLowMassDecision"
	,"Hlt1SingleMuonNoIPDecision"
	,"Hlt1SingleMuonHighPTDecision"
	,"Hlt1TrackAllL0Decision"
	,"Hlt1TrackMuonDecision"
	,"Hlt1TrackPhotonDecision"
	,"Hlt1L0AnyDecision"
	,"Hlt2SingleElectronTFLowPtDecision"
	,"Hlt2SingleElectronTFHighPtDecision"
	,"Hlt2DiElectronHighMassDecision"
	,"Hlt2DiElectronBDecision"
	,"Hlt2B2HHLTUnbiasedDecision"
	,"Hlt2Topo2BodySimpleDecision"
	,"Hlt2Topo3BodySimpleDecision"
	,"Hlt2Topo4BodySimpleDecision"
	,"Hlt2Topo2BodyBBDTDecision"
	,"Hlt2Topo3BodyBBDTDecision"
	,"Hlt2Topo4BodyBBDTDecision"
	,"Hlt2TopoMu2BodyBBDTDecision"
	,"Hlt2TopoMu3BodyBBDTDecision"
	,"Hlt2TopoMu4BodyBBDTDecision"
	,"Hlt2TopoE2BodyBBDTDecision"
	,"Hlt2TopoE3BodyBBDTDecision"
	,"Hlt2TopoE4BodyBBDTDecision"
	,"Hlt2MuonFromHLT1Decision"
	,"Hlt2DiMuonDecision"
	,"Hlt2DiMuonLowMassDecision"
	,"Hlt2DiMuonJPsiDecision"
	,"Hlt2DiMuonJPsiHighPTDecision"
	,"Hlt2DiMuonPsi2SDecision"
	,"Hlt2DiMuonBDecision"
]
TISTOSTool = TupleToolTISTOS('TISTOSTool')
TISTOSTool.VerboseL0   = True
TISTOSTool.VerboseHlt1 = True
TISTOSTool.VerboseHlt2 = True
TISTOSTool.TriggerList = triglist[:]
TISTOSTool.addTool( TriggerTisTos, name="TriggerTisTos")

LoKi_B = LoKi__Hybrid__TupleTool("LoKi_B")
LoKi_B.Variables =  {
        "ETA"               : "ETA",
        "PHI"               : "PHI",
        "FDCHI2"            : "BPVVDCHI2",
        "FDS"               : "BPVDLS",
        "DIRA"              : "BPVDIRA",
        "DTF_CTAU"          : "DTF_CTAU( 0, True )",
        "DTF_CTAUS"         : "DTF_CTAUSIGNIFICANCE( 0, True )",
        "DTF_CHI2NDOF"      : "DTF_CHI2NDOF( True )",
        "DTF_CTAUERR"       : "DTF_CTAUERR( 0, True )",
        "DTF_MASS_constr1"  : "DTF_FUN ( M , True , strings(['J/psi(1S)']) )" ,
        "DTF_MASS_constr2"  : "DTF_FUN ( M , True , strings(['psi(2S)']) )" ,
        "DTF_VCHI2NDOF"     : "DTF_FUN ( VFASPF(VCHI2/VDOF) , True )",
    }

LoKi_Mu = LoKi__Hybrid__TupleTool("LoKi_Mu")
LoKi_Mu.Variables =  {
        "NSHAREDMU" : "NSHAREDMU"  # this apparently no longer exists or runs
    }

tuple_B2psiomega = DecayTreeTuple("Tuple")
tuple_B2psiomega.Inputs = [ location ]
tuple_B2psiomega.ToolList = tupletools[:]
# tuple_B2psiomega.Decay = '[B0 -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(omega(782) -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma ) )]CC'
tuple_B2psiomega.Decay = '[B0 -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(omega(782) -> ^pi+ ^pi- ^pi0 )]CC'
tuple_B2psiomega.Branches = {
        # 'B'       : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'Jpsi'    : "[ B0 --> ^(J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'muplus'  : "[ B0 -->  (J/psi(1S) -> ^mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'muminus' : "[ B0 -->  (J/psi(1S) ->  mu+ ^mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'omega'   : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...) ^(omega(782) ->  pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'piplus'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) -> ^pi+  pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'piminus' : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+ ^pi-  (pi0 ->  gamma  gamma ) ) ]CC",
        # 'pizero'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi- ^(pi0 ->  gamma  gamma ) ) ]CC",
        # 'gamma1'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 -> ^gamma  gamma ) ) ]CC",
        # 'gamma2'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  (pi0 ->  gamma ^gamma ) ) ]CC",
        #
        'B'       : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'Jpsi'    : "[ B0 --> ^(J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'muplus'  : "[ B0 -->  (J/psi(1S) -> ^mu+  mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'muminus' : "[ B0 -->  (J/psi(1S) ->  mu+ ^mu- ...)  (omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'omega'   : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...) ^(omega(782) ->  pi+  pi-  pi0 ) ]CC",
        'piplus'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) -> ^pi+  pi-  pi0 ) ]CC",
        'piminus' : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+ ^pi-  pi0 ) ]CC",
        'pizero'  : "[ B0 -->  (J/psi(1S) ->  mu+  mu- ...)  (omega(782) ->  pi+  pi- ^pi0 ) ]CC",
        #
        # "Lambda_b0" : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) ->  mu+  mu-)  gamma)  p+  K-]CC",
        # "chi_c"     : "[Lambda_b0 -> ^(chi_c1(1P) ->  (J/psi(1S) ->  mu+  mu-)  gamma)  p+  K-]CC",
        # "Jpsi"      : "[Lambda_b0 ->  (chi_c1(1P) -> ^(J/psi(1S) ->  mu+  mu-)  gamma)  p+  K-]CC",
        # "gamma"     : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) ->  mu+  mu-) ^gamma)  p+  K-]CC",
        # "muplus"    : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) -> ^mu+  mu-)  gamma)  p+  K-]CC",
        # "muminus"   : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) ->  mu+ ^mu-)  gamma)  p+  K-]CC",
        # "proton"    : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) ->  mu+  mu-)  gamma) ^p+  K-]CC",
        # "kaon"      : "[Lambda_b0 ->  (chi_c1(1P) ->  (J/psi(1S) ->  mu+  mu-)  gamma)  p+ ^K-]CC",
	}
# for particle in ["B0", "Jpsi", "muplus", "muminus", "omega", "piplus", "piminus", "pizero", "gamma1", "gamma2"]:
for particle in ["B", "Jpsi", "muplus", "muminus", "omega", "piplus", "piminus", "pizero"]:
        tuple_B2psiomega.addTool(TupleToolDecay, name = particle)

# List of the reconstructed tuples
tuples = [ tuple_B2psiomega
	]

for tup in tuples:
    tup.ReFitPVs = True
    if MODE == "MC":
        tup.addTool(TupleToolMCTruth, name = "TruthTool")
        tup.addTool(TupleToolMCBackgroundInfo, name = "BackgroundInfo")
        tup.ToolList += ["TupleToolMCTruth/TruthTool"]
        tup.ToolList += ["TupleToolMCBackgroundInfo/BackgroundInfo"]

    # tup.B0.addTool( LoKi_B )
    tup.B.addTool( LoKi_B )
    # tup.B0.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_B"]
    tup.B.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_B"]
    tup.muplus.addTool( LoKi_Mu )
    tup.muplus.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_Mu"]
    tup.muminus.addTool( LoKi_Mu )
    tup.muminus.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_Mu"]
    # for particle in [ tup.B0 ]:
    for particle in [ tup.B ]:
        particle.addTool(TISTOSTool, name = "TISTOSTool")
        particle.ToolList += [ "TupleToolTISTOS/TISTOSTool" ]

##################################################################
# If we want to write a DST do this
##################################################################
from DSTWriters.microdstelements import *
from DSTWriters.Configuration import (SelDSTWriter,
                                              stripDSTStreamConf,
                                              stripDSTElements
                                              )
### NEW CODE ###

# from python.stripping_lib import StrippingPsiX0
# import sys
# sys.path.insert(0, './stripping_lib')
# import StrippingPsiX0

from StrippingSelections import StrippingPsiX0

stripping='stripping20'
config  = strippingConfiguration(stripping)
archive = strippingArchive(stripping)
streams = buildStreams(stripping=config, archive=archive)

# Select my line
MyStream = StrippingStream("MyStream")
MyLines = [ 'StrippingPsiX0' ]

for stream in streams:
    for line in stream.lines:
            if line.name() in MyLines:
                        MyStream.appendLines( [ line ] )

# Configure Stripping
from Configurables import ProcStatusCheck
filterBadEvents = ProcStatusCheck()

sc = StrippingConf( Streams = [ MyStream ],
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = filterBadEvents )

################

SelDSTWriterElements = {
    'default'              : stripDSTElements()
    }
SelDSTWriterConf = {
    'default'              : stripDSTStreamConf()
    }
#sc = StrippingConf(Streams = [StrippingPsiX0.stream])
if MODE == 'MC':
  dstWriter = SelDSTWriter( "MyDSTWriter",
                          StreamConf = SelDSTWriterConf,
                          MicroDSTElements = SelDSTWriterElements,
                          OutputFileSuffix ='MC',
                          SelectionSequences = sc.activeStreams()
                          )

###################### DAVINCI SETTINGS ############################################
DaVinci().SkipEvents = 0  #1945
DaVinci().PrintFreq = 1000
DaVinci().EvtMax = EVTMAX
DaVinci().TupleFile = "DVTuples1.root"
DaVinci().HistogramFile = 'DVHistos.root'
DaVinci().RootInTES = rootInTES
DaVinci().InputType = "MDST"
DaVinci().Simulation = False
DaVinci().Lumi = True
# DaVinci().DataType = "2011"
DaVinci().DataType = "2012"
# CondDB( LatestGlobalTagByDataType = '2011' )
CondDB( LatestGlobalTagByDataType = '2012' )

if False: # Add the DST writing algorithms
	DaVinci().appendToMainSequence( [ dstWriter.sequence(), printTree ] )

if True: # Add the ntuple writing algorithms
	DaVinci().UserAlgorithms = [
                tuple_B2psiomega
			]
if MODE == 'MC':
    DaVinci().Simulation = True
    DaVinci().Lumi = False
    DaVinci().UserAlgorithms += [
                mctuple_B2psiomega
                ]

if OUTPUTLEVEL == DEBUG:
	DaVinci().MoniSequence += [ mctree ]

from Configurables import DaVinciInit
DaVinciInit().OutputLevel = OUTPUTLEVEL

if MODE != "MC":
    from Configurables import LumiIntegrateFSR, LumiIntegratorConf
    LumiIntegrateFSR('IntegrateBeamCrossing').SubtractBXTypes = ['None']

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

###################################################################################
####################### THE END ###################################################
###################################################################################
