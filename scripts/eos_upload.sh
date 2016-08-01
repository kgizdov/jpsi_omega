JOB_ID="$1"
source ./envir.sh

### LOGIN TO EOS
LbLogin.sh
source /afs/cern.ch/project/eos/installation/lhcb/etc/setup.sh

eos cp ${WORK_DIR}/${GANGA_DIR}/${JOB_ID}/tuples_2011.root ${EOS_UDIR}/data/2011/
eos cp ${WORK_DIR}/${GANGA_DIR}/${JOB_ID}/tuples_2011_0.root ${EOS_UDIR}/data/2011/

eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+1))/tuples_2012.root ${EOS_UDIR}/data/2012/
eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+1))/tuples_2012_0.root ${EOS_UDIR}/data/2012/

eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+2))/tuples_2011_up.root ${EOS_UDIR}/mc/2011/
eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+2))/tuples_2011_up_0.root ${EOS_UDIR}/mc/2011/

eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+3))/tuples_2011_down.root ${EOS_UDIR}/mc/2011/
eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+3))/tuples_2011_down_0.root ${EOS_UDIR}/mc/2011/

eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+4))/tuples_2012_up.root ${EOS_UDIR}/mc/2012/
eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+4))/tuples_2012_up_0.root ${EOS_UDIR}/mc/2012/

eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+5))/tuples_2012_down.root ${EOS_UDIR}/mc/2012/
eos cp ${WORK_DIR}/${GANGA_DIR}/$((JOB_ID+5))/tuples_2012_down_0.root ${EOS_UDIR}/mc/2012/
