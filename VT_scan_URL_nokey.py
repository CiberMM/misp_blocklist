#VT_scan_URL.py

import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', "--url", required=True)
args = parser.parse_args()

VT_API_KEY = '<YOUR VT API KEY>'
headers = {'x-apikey': VT_API_KEY}
form="url=" + args.url
r = requests.post('https://www.virustotal.com/api/v3/urls', data=form, headers=headers, verify=True)
response = r.json()
link=response['data']['links']['self']
r = requests.get(url=link, headers=headers, verify=True)
response = r.json()
#print(response)
print(response['data']['attributes']['stats'])

