#dump_misp_ips.py

import requests
import json

MISP_API_KEY = '<YOUR MISP API KEY>'
headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': MISP_API_KEY}
r = requests.get('https://<MISP IP>/attributes/restSearch/returnFormat:json/type:ip-src', headers=headers, verify=False)
response = r.json()
for item in response["response"]["Attribute"]:
    print(item['value'])
