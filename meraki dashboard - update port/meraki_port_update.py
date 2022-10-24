###################################################
### Example python code to update a single port ###
###   HTTP PUT against meraki API               ###
### meraki_port_update.py num vlan desc         ###
###################################################

import requests
import json
from sys import argv,exit

API_KEY = "XXXX"
device_serial = "XXXX"

headers = {"Content-Type": "application/json",
           "Accept": "appliction/json",
           "X-Cisco-Meraki-API-Key": API_KEY}


# throw exception if argument is not passed, print out usage
try:
    port_num = argv[1]
    access_vlan = argv[2]
    port_name = argv[3]
except:
    print("\n\nUsage - meraki_port_update.py portnum vlan 'name'")
    exit()
    
# generate JSON payload from arguments passed
payload = json.dumps({"portId": port_num,
           "name": port_name,
            "enabled": True,
            "poeEnabled": True,
            "type": "access",
            "vlan": access_vlan})


# PUT headers and payload the meraki API via device port url
url = f"https://api.meraki.com/api/v1/devices/{device_serial}/switch/ports/{port_num}"
port_update = requests.put(url, headers = headers, data = payload)

# if port_update checks to see if result was a 200(success) or 400(error)
# if 200 print out result of PUT
# if 400 print out error(s)
if port_update:
    for k,v in port_update.json().items():
        if isinstance(v, list):
            print(f"{k}:")
            for x in v:
                print(f"    {x}")
        else:
            print(f"{k}: {v}")
else:
    for k,v in port_update.json().items():
        print(f"{k}:")
        for x in v:
            print(f"        -{x}")
 

