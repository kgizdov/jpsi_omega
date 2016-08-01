source ./envir.sh
source ./cuts.sh

### LOGIN TO EOS
LbLogin.sh
source /afs/cern.ch/project/eos/installation/lhcb/etc/setup.sh

### CUT TUPLES
# LD_LIBRARY_PATH=../simpletools_2.0s/lib  ../simpletools_2.0s/bin/cutapplier "${EOS_ROOT}${EOS_UDIR}/data/tuples.root" "DecayTree" "${ALLCUT}" "cut_tuples.root"
# eos cp ./cut_tuples.root ${EOS_UDIR}/data/
# rm ./cut_tuples.root
# LD_LIBRARY_PATH=../simpletools_2.0s/lib  ../simpletools_2.0s/bin/cutapplier "${EOS_ROOT}${EOS_UDIR}/mc/tuples.root" "DecayTree" "${ALLCUT}" "cut_tuples.root"
# eos cp ./cut_tuples.root ${EOS_UDIR}/mc/
# rm ./cut_tuples.root

### CUT N3 TUPLES
LD_LIBRARY_PATH=../simpletools_2.0s/lib  ../simpletools_2.0s/bin/cutapplier "${EOS_ROOT}${EOS_UDIR}/data/cut_tuples_n3.root" "DecayTree" "${ALLCUT}" "cut_tuples.root"
eos cp ./cut_tuples.root ${EOS_UDIR}/data/
rm ./cut_tuples.root
LD_LIBRARY_PATH=../simpletools_2.0s/lib  ../simpletools_2.0s/bin/cutapplier "${EOS_ROOT}${EOS_UDIR}/mc/cut_tuples_n3.root" "DecayTree" "${ALLCUT}" "cut_tuples.root"
eos cp ./cut_tuples.root ${EOS_UDIR}/mc/
rm ./cut_tuples.root
