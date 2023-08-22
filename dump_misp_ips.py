#dump_misp_ips.py

import requests
import json

MISP_API_KEY = 'LiQ2q8KWQ21rVltb84Wv2IzWIVRhb3Ev03cgJSwU'
headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': MISP_API_KEY}
r = requests.get('https://172.30.158.48/attributes/restSearch/returnFormat:json/type:ip-src', headers=headers, verify=False)
response = r.json()
for item in response["response"]["Attribute"]:
    print(item['value'])
