###############################################
### Example python code to display a simple ###
###   HTTP GET request against meraki API   ###
###############################################

import requests
import os
from time import sleep, gmtime, strftime

API_KEY = "XXXX"
device_serial = "XXXX"

headers = {"Content-Type": "application/json",
           "Accept": "appliction/json",
           "X-Cisco-Meraki-API-Key": API_KEY}

payload = None


while(True):  ## While true is a perpetual while loop. Will keep running until script is quit via ctrl+c.
    base_url = f"https://api.meraki.com/api/v1/devices/{device_serial}/switch/ports/statuses/packets"      
    port_stats = requests.get(base_url, headers=headers, data = payload)           ## perform http GET against meraki API url, passing header information defined above
    os.system('cls')       ## clear screen on windows host between each display
    print(f"Switch {device_serial} port stats at {strftime('%H:%M:%S')}")  ## print current time in status
    print(f"{'PortID':<10}{'Total': <15}{'Bcast': <15}{'Mcast': <15}{'CRC Errors': <15}{'Fragments': <15}{'Collisions': <15}{'TCNs': <15}") ## table headers.  Left justification padded to 15
    for port in port_stats.json():            ## iterate over all ports
        if port['packets'][0]['total'] == 0:  ## Only display interfaces > 0 total packets -- active ports
            pass
        else:
            print(f"{port['portId']: <10}", end = "")  ## print portID with left justification, and padded to 10
            for portstatus in port['packets']:
                    print(f"{portstatus['total']: <15}", end = "")  ## iterate over port status, and display the value of key ['total'] on each iteration.  Left justification padded to 15
            print("\n", end="") ## print new line
    sleep(10)  ## sleep for 10 seconds, then run again


