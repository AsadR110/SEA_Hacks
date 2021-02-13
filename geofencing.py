import json
import os
import time

# Pass current location, and room data to determine if person is in a certain room
def roomCheck(curLoc, roomData):
    for XValue in roomData["cornersX"]:
        #loc is greater than any single x value
        if  curLoc[0] > XValue:
            for XValue in roomData["cornersX"]:
                #loc is less than any single x value (betweeen 2 X)
                if  curLoc[0] < XValue:
                    for YValue in roomData["cornersY"]:
                        #loc is greater than any single y value
                        if  curLoc[1] > YValue:
                            for YValue in roomData["cornersY"]:
                                #loc is less than any single y value (betweeen 2 Y)
                                if  curLoc[1] < YValue:
                                    return True
                                else:
                                    return False

def checkLoc(curLoc, geofencingData, roomStatus):
    i = 0
    for room in geofencingData: 
        i += 1 
        # When using the roomCheck function, just pass the room you are in
        # -> roomCheck(curLoc, geofencingData["room"+str(i)])
        if geofencingData["room"+str(i)]["type"] == "4 corner":
            for XValue in geofencingData["room"+str(i)]["cornersX"]:
                #loc is greater than any single x value
                if  curLoc[0] > XValue:
                    for XValue in geofencingData["room"+str(i)]["cornersX"]:
                        #loc is less than any single x value (betweeen 2 X)
                        if  curLoc[0] < XValue:
                            for YValue in geofencingData["room"+str(i)]["cornersY"]:
                                #loc is greater than any single y value
                                if  curLoc[1] > YValue:
                                    for YValue in geofencingData["room"+str(i)]["cornersY"]:
                                        #loc is less than any single y value (betweeen 2 Y)
                                        if  curLoc[1] < YValue:
                                            roomStatus["room"+str(i)] = True
        else:
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

            # Split 6 corner room 2 into 2, 4 corners (Includes 7th point)
            # First rectangle
            for j in range(4):
                room6Corners["rectangle 1"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                room6Corners["rectangle 1"]["cornersY"].append(geofencingData["room"+str(i)]["cornersY"][j])
            
            roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 1"])
            
            # Second rectangle
            for j in range(4, 7):
                room6Corners["rectangle 2"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                room6Corners["rectangle 2"]["cornersY"].append(geofencingData["room"+str(i)]["cornersX"][j])

            roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 2"])

    return roomStatus

path = os.path.dirname(__file__)
f = open(path + '/sample.json', "r")
geofencingData = json.load(f)
f.close()