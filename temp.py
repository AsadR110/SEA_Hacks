import json
import os

path = os.path.dirname(__file__)

while True:
    curLoc = (3,13)

    f = open(path + '/sample.json', "r")
    geofencingData = json.load(f)
    # convert geofencingData to python

    for room in geofencingData:
        if room["type"] == "4 corner":
            print(room)

        # If 6 corner, generate 2, 4 corner rectangles
        if room["type"] == "6 corner":
            # Generate 2 "rooms"
            room6Corners = {
                "rectangle 1" : {
                    "cornersX" : [x1, 3, 4, 5],
                    "cornersY" : [y1, 4, 1, 4]
                },
                "rectangle 2" : {
                    "cornersX" : [6, 6, 8, 8],
                    "cornersY" : [1, 7, 1, 7]
                },
                "rectangle 3" : {
                    "cornersX" : [6, 6, 8, 8],
                    "cornersY" : [1, 7, 1, 7]
                }
            }

            


    f.close()