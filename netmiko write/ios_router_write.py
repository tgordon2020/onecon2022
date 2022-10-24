from netmiko import ConnectHandler
from time import sleep
from sys import argv


interface_name = argv[1]
ip = argv[2]

r2 = {"host" : "X.X.X.X",
      "port" : "23",
      "username" : "admin",
      "password" : "password",
      "device_type": "cisco_ios_telnet"}

net_connect = ConnectHandler(**r2)
net_connect.find_prompt()



config_list = [f"interface {interface_name}",
                f"ip address {ip}",
                "no shut"
                ]

config_output = net_connect.send_config_set(config_list)
print(config_output)

output_struct = net_connect.send_command("show ip int brief", use_textfsm=True)
for output in output_struct:
      for k,v in output.items():
            print(f"{k}: {v}")
      print("\n")
