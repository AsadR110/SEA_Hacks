import json
import os

path = os.path.dirname(__file__)

while True:
    curLoc = (3,13)

    f = open(path + '/sample.json', "r")
    geofencingData = json.load(f)

    for room in geofencingData:
        if room["type"] == "4 corner":
            print(room)

            

    f.close()