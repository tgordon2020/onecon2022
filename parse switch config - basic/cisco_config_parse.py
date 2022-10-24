from ttp import ttp
from glob import glob
import csv

ttp_template = """
<group name = "interface_cfg">
interface {{ interface }}
  description {{ description | ORPHRASE}}
  switchport mode {{ mode }}
  switchport trunk allowed vlan {{ trunk_allowed }}
  switchport trunk native vlan {{ trunk_native }}
  switchport access vlan {{ access_vlan }}
  switchport voice vlan {{ voice_vlan }}
  ip address {{ ip }} {{ mask }}
</group>
<group name = "hostname">
hostname {{ hostname }}
</group>
"""

config_files = glob("switch-*.*") # create iterable list of file names

interface_list = [] #blank list that is used later for CSV generation

#Iterate over config_files list and parse with TTP parser. Append config fields and hostname to interface_list 
for config_file in config_files: 
    with open(config_file, "r") as device_config:
        config = device_config.read()
        parser = ttp(data=config, template=ttp_template)
        parser.parse()
        results = parser.result()[0]
        hostname = results[0]['hostname']['hostname']
        for interface in (results[0]["interface_cfg"]):
            interface['hostname'] = hostname
            interface_list.append(interface)


#
with open("switch_configs.csv", "w", newline='') as configs_csv:
    fieldnames = ['hostname', 'interface', 'mode', 'access_vlan', 'voice_vlan', 'trunk_native', 'trunk_allowed', "ip" , "mask"]
    writer = csv.DictWriter(configs_csv, fieldnames=fieldnames)
    writer.writeheader()
    for interface in interface_list:
        writer.writerow(interface)
