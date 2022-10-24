import re
from macdb import ouiread
from collections import defaultdict

#########################################################################
##                         arp_parse REG                               ##
## Internet  10.15.30.2             30   0008.6600.09b6  ARPA   Vlan15 ##
##             [1]                  [2]        [3]                     ##
#########################################################################

#########################################################################
##                         mac_parse REG                               ##
##  120    000f.d403.a8a4    DYNAMIC     Gi1/1/1                       ##
##  [1]         [2]                        [3]                         ##
#########################################################################

arp_parse = r'Internet\s+([0-9\.]+)\s+([0-9]+)\s+([0-9a-fA-F.-:]+)\s+ARPA\s+'
mac_parse = r'\s+([0-9]+)\s+([0-9a-fA-F.-:]+)\s+DYNAMIC\s+([a-zA-Z0-9\/]+)'


with open("mac.txt", "r") as route_arp_file:
    route_arp = route_arp_file.read()
    arp_reg = re.finditer(arp_parse, route_arp)
    mac_reg = re.finditer(mac_parse, route_arp)

arpdict = {}
int_arp_mac = defaultdict(list)

for arp in arp_reg:
    arpdict[arp[3]]=arp[1]

for mac in mac_reg:
    if mac[3] == "Po40":
        pass
    else:
        try:
            int_arp_mac[mac[3]].append(f"{mac[1]} : {arpdict[mac[2]]}: {mac[2]} : {ouiread(mac[2])}")
        except:
            int_arp_mac[mac[3]].append(f"{mac[1]} : {mac[2]} : {ouiread(mac[2])}")

for k,v in int_arp_mac.items():
    print(k)
    for x in v:
        print("    ",x)
        print("\n")