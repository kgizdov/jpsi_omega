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

ganga ../data/scripts/ganga_DV_data_21.py 2011 b2
ganga ../data/scripts/ganga_DV_data_21.py 2012 b2
ganga ../data/scripts/ganga_DV_MC_21.py 2011 BdJpOm MagUp
ganga ../data/scripts/ganga_DV_MC_21.py 2011 BdJpOm MagDown
ganga ../data/scripts/ganga_DV_MC_21_1.py 2012 BdJpOm MagUp
ganga ../data/scripts/ganga_DV_MC_21_1.py 2012 BdJpOm MagDown