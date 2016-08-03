#!/bin/bash

### Setup Ganga
LbLogin.sh
source SetupProject.sh Ganga

### Check if proxy is setup
lhcb-proxy-info | grep -i timeleft
if [[ $? != 0 ]]; then
    echo "NO PROXY FOUND - CANNOT CONTINUE"
    echo "PLEASE SETUP PROXY FIRST"
    exit -1
fi

ganga ganga/ganga_DV_data_21.py 2011 b2
ganga ganga/ganga_DV_data_21.py 2012 b2
ganga ganga/ganga_DV_MC_21.py 2011 BdJpOm MagUp
ganga ganga/ganga_DV_MC_21.py 2011 BdJpOm MagDown
ganga ganga/ganga_DV_MC_21_1.py 2012 BdJpOm MagUp
ganga ganga/ganga_DV_MC_21_1.py 2012 BdJpOm MagDown
