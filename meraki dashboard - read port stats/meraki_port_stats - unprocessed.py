###############################################
### Example python code to display a simple ###
###   HTTP GET request against meraki API   ###
###############################################

import requests
import os
import json
from time import sleep, gmtime, strftime

API_KEY = "XXXX"
device_serial = "XXXX"

headers = {"Content-Type": "application/json",
           "Accept": "appliction/json",
           "X-Cisco-Meraki-API-Key": API_KEY}

payload = None

base_url = f"https://api.meraki.com/api/v1/devices/{device_serial}/switch/ports/statuses/packets"   
port_stats = requests.get(base_url, headers=headers, data = payload)           ## perform http GET against meraki API url, passing header information defined above
port_stats_json = port_stats.json()
print(json.dumps(port_stats_json, indent=4))

