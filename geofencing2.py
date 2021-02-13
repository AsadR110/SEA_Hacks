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

        if room["type"] == "6 corner":
            # Generate 2 "rooms"
            room6Corners = {
                "rectangle 1" : {
                    "cornersX" : [],
                    "cornersY" : []
                },
                "rectangle 2" : {
                    "cornersX" : [],
                    "cornersY" : []
                }
            }

            for i in range(4):
                room6Corners["rectangle 1"]["cornersX"].append(room["cornersX"][i]) 
                room6Corners["rectangle 1"]["cornersY"].append(room["cornersY"][i])
            
            for i in range(4, 7):
                room6Corners["rectangle 2"]["cornersX"].append(room["cornersX"][i]) 
                room6Corners["rectangle 2"]["cornersY"].append(room["cornersY"][i])
    f.close()