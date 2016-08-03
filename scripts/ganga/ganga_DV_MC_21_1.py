# Script to create DaVinci Job
# Greig Cowan
# Konstantin Gizdov

import sys
import os
curr_dir = os.getcwd()

# sys.path.insert(1, '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/python/stripping_lib')
# sys.path.insert(1, '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/python')
# sys.path.insert(1, '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/scripts')

year    = sys.argv[1]
mode    = sys.argv[2]
magnet  = sys.argv[3]

if mode not in ['BdJpOm', 'norm', 'signal', 'background_Bd', 'Bu_JpsiX', 'Bd_JpsiX', 'Bs_JpsiX', 'Lb_JpsiX', 'b2']: sys.exit()
if year not in ['2011', '2012']:
    print "\n## THIS SCRIPT IS FOR 2011 & 2012 ONLY ##\n"
    sys.exit()

if mode != 'BdJpOm':
    print "\n## THIS SCRIPT IS FOR SIGNAL ONLY ##\n"
    sys.exit()

if magnet not in ['MagDown', 'MagUp']:
    print "\n## WRONG OPTION FOR MAGNET ##\n"
    sys.exit()

if mode == 'norm':
    script = '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/scripts/davinci/DV_Lb2chicpK_norm_' + year + '_MC_21.py'
else:
    # script = '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/scripts/davinci/DV_B2psiomega_' + year + '_MC_21.py'
    # script = '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/scripts/davinci/mc_' + year + '.py'
    script = str(curr_dir) + '/davinci/mc_' + year + '.py'

# job_name = 'MC' + str(year) + mode + magnet
job_name = 'MC' + str(year)[2:] + mode
if magnet[3] == 'D':
    job_name = job_name + 'MD'
if magnet[3] == 'U':
    job_name = job_name + 'MU'

print ('Job Name: ' + job_name)
print ('Script: ' + script)

# stripping_1 = '/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/python/stripping_lib/StrippingPsiX0.py'

DV = DaVinci()
DV.version = 'v39r1'  # latest is v38r1p1, was v36r1, working now is v36r7p7
# DV.version = 'v35r0'  # latest is v38r1p1, was v36r1, working now is v36r7p7
# DV.platform = 'x86_64-slc6-gcc48-opt' # necessary for the older version of DaVinci
DV.optsfile = [File(script)]

BK_locations = []

## 2011 ##

if year == '2011' and mode == 'Bd_JpsiOm':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08h/Digi13/Trig0x40760037/Reco14c/Stripping21r1NoPrescalingFlagged/11140400/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'Bd_JpsiX':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST'
        ,'/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11442001/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'Bu_JpsiX':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST'
        ,'/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12442001/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'Bs_JpsiX':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia6/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
        ,'/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'Lb_JpsiX':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-EmNoCuts/Sim05/Trig0x40760037Flagged/Reco12a/Stripping17NoPrescalingFlagged/15442001/ALLSTREAMS.DST'
    ]

##########

if year == '2011' and mode == 'background_Bd':
        # Bd -> chic(1,2)K* reflection
    BK_locations = [
    ]
if year == '2011' and mode == 'signal':
    BK_locations = [
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia6/Sim08e/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/15244202/ALLSTREAMS.DST'
        ,'/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08e/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/15244202/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'b2':
    BK_locations = [
        # '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia6/Sim08h/Digi13/Trig0x40760037/Reco14c/Stripping20r1NoPrescalingFlagged/11140400/ALLSTREAMS.DST',
        '/MC/2011/Beam3500GeV-2011-' + magnet + '-Nu2-Pythia8/Sim08h/Digi13/Trig0x40760037/Reco14c/Stripping20r1NoPrescalingFlagged/11140400/ALLSTREAMS.DST'
    ]

if year == '2012' and mode =='signal':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia6/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/15244202/ALLSTREAMS.DST'
        ,'/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/15244202/ALLSTREAMS.DST'
    ]

if year == '2011' and mode == 'signal_Bs':
    BK_locations = [
    ]
if year == '2012' and mode =='signal_Bs':
    BK_locations = [
    ]

if year == '2011' and mode == 'norm':
    BK_locations = [
    ]
if year == '2012' and mode =='norm':
    BK_locations = [
    ]

### 2012 ###

if year == '2012' and mode == 'Bd_JpsiOm':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08h/Digi13/Trig0x409f0045/Reco14c/Stripping21NoPrescalingFlagged/11140400/ALLSTREAMS.DST'
    ]

if year == '2012' and mode == 'Bd_JpsiX':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST'
        ,'/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/11442001/ALLSTREAMS.DST'
    ]

if year == '2012' and mode == 'Bu_JpsiX':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST'
        ,'/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12442001/ALLSTREAMS.DST'
    ]

if year == '2012' and mode == 'Bs_JpsiX':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
        ,'/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
    ]

if year == '2012' and mode == 'b2':
    BK_locations = [
        '/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
        ,'/MC/2012/Beam4000GeV-2012-' + magnet + '-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/13442001/ALLSTREAMS.DST'
    ]

############

data = LHCbDataset()
bk = BKQuery()

for path in BK_locations:
    bk.path = path
    tmp = bk.getDataset()
    print path, len(tmp.files)
    if len(tmp.files) > 0:
        data.extend( tmp )

import sys
if len(data.files) < 1:
    sys.exit()

debug = 0

max_files = -1
files_per_job = 1
if debug:
    max_files = 2
    files_per_job = 1
print ('Max Files =' + str(max_files))
print ('Files Per Job = ' + str(files_per_job))

j = Job(
      name              = job_name
    , application       = DV
    , splitter          = SplitByFiles(filesPerJob = files_per_job, maxFiles = max_files)
    , inputdata         = data
    , outputfiles       = [LocalFile("*.root")]
    , do_auto_resubmit  = True
    , backend           = Dirac()  # Local() for quick debugging, Dirac() for online
    , postprocessors    = [RootMerger( files = ['DVTuples1.root'], ignorefailed = True, overwrite = True )]
    )
j.submit()

