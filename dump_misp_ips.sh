#!/bin/bash

python3 -W ignore dump_misp_ips.py | sort -nu > misp_blocklist.txt
git add misp_blocklist.txt
export DATE=`date +%Y%m%d`
git commit -m "last update $DATE"
git push -u origin main
