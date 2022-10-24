import csv
from sys import argv,exit

try:
    operator = argv[1]
    value = int(argv[2])
except:
    exit("usage: csv_parse.py g|l temperature")

with open("weather.csv", "r") as weather_data:
    weather_rows = csv.DictReader(weather_data)
    for row in weather_rows:
        if operator == "g":
            if int(row['Data.Temperature.Max Temp']) >= value:
                print(f"{row['Date.Full']}: {row['Station.Location']}: {row['Data.Temperature.Max Temp']}")
            else:
                pass
        elif operator == "l":
            if int(row['Data.Temperature.Min Temp']) <= value:
                print(f"{row['Date.Full']}: {row['Station.Location']}: {row['Data.Temperature.Min Temp']}")
            else:
                pass
        else:
            exit("usage: csv_parse.py g|l temperature")