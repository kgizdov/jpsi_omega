# notes on how to work with EOS
# kinit kgizdov -k -t /root/my.keytab  # login to kerberos

# after KRB login XROOTD can load file directly like this
# EOS_ROOT="root://eoslhcb.cern.ch/"
# EOS_UDIR="/eos/lhcb/user/k/kgizdov/jpsi_omega/"
# TFile * file = TFile::Open("root://eoslhcb.cern.ch//eos/lhcb/user/k/kgizdov/jpsi_omega/data/2011/DVTuples_new.root")

# # MC with cuts stats
# total:          366588      +/-   605.465
# accepted:       30171       +/-   173.698
# rejected:       336417      +/-   580.015
# efficiency:     0.0823022   +/-   0.000453907
# reject. rate:   0.917698    +/-   0.000453907
# OLD
# total:          361055      +/- 600.879
# accepted:       32375       +/- 179.931
# rejected:       328680      +/- 573.306
# efficiency:     0.0896678   +/- 0.000475479
# reject. rate:   0.910332    +/- 0.000475479

# # Data with cuts stats
# total:          1.60327e+07 +/- 4004.09
# accepted:       38122       +/- 195.249
# rejected:       1.59946e+07 +/- 3999.33
# efficiency:     0.00237776  +/- 1.21636e-05
# reject. rate:   0.997622    +/- 1.21636e-05
# OLD
# total:          1.60327e+07 +/- 4004.09
# accepted:       40366       +/- 200.913
# rejected:       1.59924e+07 +/- 3999.05
# efficiency:     0.00251772  +/- 1.25156e-05
# reject. rate:   0.997482    +/- 1.25156e-05

# # Data with cuts stats, without omega_PT
# total:          1.60327e+07 +/- 4004.09
# accepted:       314934      +/- 561.19
# rejected:       1.57178e+07 +/- 3964.57
# efficiency:     0.0196432   +/- 3.46572e-05
# reject. rate:   0.980357    +/- 3.46572e-05

# # MC with cuts stats, without omega_PT
# total:          361055      +/- 600.879
# accepted:       65664       +/- 256.25
# rejected:       295391      +/- 543.499
# efficiency:     0.181867    +/- 0.000641952
# reject. rate:   0.818133    +/- 0.000641952
