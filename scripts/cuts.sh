###### OLD CUTS ######

### B0 CUT
# CHI2/NDOF < 5; NDOF == 1  # applied at stripping level
# DTF_CHI2NDOF < 5; later DTF, same as above
# HLT Jpsi Decision TOS == 1
# ct > 150 um
# BCUT="(B0_L0DiMuonDecision_TOS == 1 || B0_L0MuonDecision_TOS == 1) && ( B0_Hlt1DiMuonHighMassDecision_TOS == 1 || B0_Hlt1DiMuonLowMassDecision_TOS == 1 || B0_Hlt1TrackMuonDecision_TOS == 1 || B0_Hlt1SingleMuonHighPTDecision_TOS == 1 || B0_Hlt1TrackAllL0Decision_TOS == 1 ) && (B0_Hlt2DiMuonJPsiDecision_TOS == 1 || B0_Hlt2DiMuonJPsiHighPTDecision_TOS == 1) && B0_DTF_CTAU > 0.150 && B0_DTF_CHI2NDOF < 5"
BCUT="((B0_L0DiMuonDecision_TOS == 1 || B0_L0MuonDecision_TOS == 1) && ( B0_Hlt1DiMuonHighMassDecision_TOS == 1 || B0_Hlt1TrackMuonDecision_TOS == 1 || B0_Hlt1SingleMuonHighPTDecision_TOS == 1) && (B0_Hlt2DiMuonJPsiDecision_TOS == 1 || B0_Hlt2DiMuonJPsiHighPTDecision_TOS == 1) && B0_DTF_CTAU > 0.150 && B0_DTF_CHI2NDOF < 5)"

### MUON CUT
# CHI2/NDOF < 5; NDOF == 1  # applied at stripping level
# PT > 550 MeV
# L(muon) - L(hadron) > 0; L - likelihood  # applied at stripping level
# delta-KL > 5000; Kullback-Leibler divergence  # applied at stripping level - produces CloneDist var
# VXCHI2 < 20  # applied at stripping level
MUONCUT="(muplus_PT > 550 && muminus_PT > 550 && ((muplus_PIDmu - muplus_PIDK) > 0) && ((muminus_PIDmu - muminus_PIDK) > 0) && ((muplus_PIDmu - muplus_PIDp) > 0) && ((muminus_PIDmu - muminus_PIDp) > 0))"

### J/PSI CUT
# mass +/- 40 MeV
# DLS > 3 sigma  # decay length significance
JPSICUT="(Jpsi_M > 3059 && Jpsi_M < 3139 && Jpsi_BPVDLS > 3)"

### PION CUT
# CHI2/NDOF < 4; NDOF == 1  # applied at stripping level
# 2 < ETA < 5  # applied at stripping level
# 3.2 < P < 150 GeV
# MIPCHI2DV > 4; minimum distance from PV  # applied at stripping level
# L(pion) - L(kaon) > 0; L - likelihood
# delta-KL > 5000; Kullback-Leibler divergence  # applied at stripping level - produces CloneDist var
# TRGHOSTPROB < 0.5; track ghost probabilty < 0.5
# PT > 250 MeV
PIONCUT="(piplus_P > 3200 && piminus_P > 3200 && piplus_P < 150000 && piminus_P < 150000 && piplus_PT > 250 && piminus_PT > 250 && piplus_PIDK < 0 && piminus_PIDK < 0 && piplus_ProbNNghost < 0.5 && piminus_ProbNNghost < 0.5)"

### OMEGA CUT
# PT > 1.2 GeV  # applied at stripping
# mass +/- 50 MeV
# PT > 3 GeV
OMEGACUT="(omega_M > 732 && omega_M < 832 && omega_PT > 3000)"

### PIZERO CUT
# mass +/- 25
PIZEROCUT="(pizero_M > 109 && pizero_M < 159)"

### GAMMA CUT
# PT > 300
GAMMACUT="(gamma1_PT > 300 && gamma2_PT > 300)"

### ALL CUT
ALLCUT="(${BCUT} && ${MUONCUT} && ${JPSICUT} && ${PIONCUT} && ${OMEGACUT} && ${PIZEROCUT} && ${GAMMACUT})"
