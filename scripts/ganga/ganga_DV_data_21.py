# Script to create DaVinci Job
# Greig Cowan
# Konstantin Gizdov

import sys

year = sys.argv[1]
mode = sys.argv[2]

end = '.py'
if mode not in ['norm', 'b2']: sys.exit()
if year not in ['2011', '2012']:
    print "\n## THIS SCRIPT IS FOR 2011 & 2012 ONLY ##\n"
    sys.exit()
if mode != 'b2':
    print "\n## THIS SCRIPT IS FOR SIGNAL ONLY ##\n"
    sys.exit()
if mode == 'norm': middle = '_norm_'
if mode == 'b2': middle = '_B2psiomega_'

# script='/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/python/DV' + middle + year + end  # fix path to script
script='/afs/cern.ch/work/k/kgizdov/Git/jpsi_omega/data/python/data_' + year + '.py'  # fix path to script

job_name = 'B2JpOm' + str(year)[2:] + 'data'
print ('Job Name: ' + str(job_name))
print ('Script: ' + script)

DV = DaVinci()
# DV.version = 'v36r7p7'  # latest is v38r1p1, was set to v36r3p1, working is v36r7p7
DV.version = 'v39r1'  # latest is v38r1p1, was set to v36r3p1, working is v36r7p7
# DV.version = 'v35r0'  # latest is v38r1p1, was v36r1, working now is v36r7p7
# DV.platform = 'x86_64-slc6-gcc48-opt' # necessary for the older version of DaVinci
DV.optsfile = [File(script)]


BK_locations = []

if year == '2011':
    BK_locations = [
        '/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r1/WGBandQSelection11/90000000/PSIX0.MDST'
        ,'/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r1/WGBandQSelection11/90000000/PSIX0.MDST'
    ]
if year == '2012':
    BK_locations = [
        '/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21/WGBandQSelection11/Merge/90000000/PSIX0.MDST'
        ,'/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21/WGBandQSelection11/Merge/90000000/PSIX0.MDST'
    ]

data = LHCbDataset()
bk = BKQuery()

for path in BK_locations:
    bk.path = path
    tmp = bk.getDataset()
    print path, len(tmp.files)
    if len(tmp.files) > 0:
            data.extend( tmp )

print data

debug = 0
max_files = -1
files_per_job = 4
if debug:
    max_files = 2
    files_per_job = 1
print ('Max Files = ' + str(max_files))
print ('Files Per Job = ' + str(files_per_job))

import sys
if len(data.files) < 1:
    sys.exit()

j = Job(
      name              = job_name
    , application       = DV
    , splitter          = SplitByFiles(filesPerJob = files_per_job, maxFiles = max_files)
    , inputdata         = data
    , outputfiles       = [LocalFile("*.root")]
    , do_auto_resubmit  = True
    , backend           = Dirac()  # Local() for quick debugging, Dirac() for online
    # , postprocessors    = [RootMerger( files = ['DVTuples1.root'], ignorefailed = True )]
    # , postprocessors    = [RootMerger( files = ['DVTuples1.root'], ignorefailed = True, overwrite = True )]
    # , postprocessors    = [SmartMerger( files = ['DVTuples1.root'], ignorefailed = True )]
    )
j.submit()

