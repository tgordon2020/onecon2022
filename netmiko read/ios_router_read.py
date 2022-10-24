from netmiko import ConnectHandler
from time import sleep
from sys import argv
from pprint import pprint

r2 = {"host" : "X.X.X.X",
      "port" : "23",
      "username" : "admin",
      "password" : "password",
      "device_type": "cisco_ios_telnet"}

try:
    net_connect = ConnectHandler(**r2)
    net_connect.find_prompt()
    output_raw = net_connect.send_command(argv[1])
    output_struct = net_connect.send_command(argv[1], use_textfsm=True)


    if argv[2].lower() == "r":
        print("Raw Output")
        print(output_raw)

    elif argv[2].lower() == "s":
        print("Structured Output Unprocessed")
        pprint(output_struct)
        print("\n")

    elif argv[2].lower() == "p":
        print("Structured Output Processed")
        for output in output_struct:
            for k,v in output.items():
                print(f"{k}: {v}")
            print("\n")
    else:
        print("Usage: netmiko_read.py 'command' r|s|p")
except Exception as e:
    print("Usage: netmiko_read.py 'command' r|s|p")
    print(e)