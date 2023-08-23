#!/bin/bash

python3 -W ignore dump_misp_ips.py | sort -nu > misp_blocklist.txt
git add misp_blocklist.txt
export DATE=`date +%Y%m%d%HH%MM`
export GITHUB_TOKEN=`cat github_CiberMM_token.txt`
git commit -m "last update $DATE"
git push -u origin main
