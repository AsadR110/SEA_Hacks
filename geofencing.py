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
    return False

def checkLoc(curLoc, geofencingData):
    #populating dictionary with all rooms
    i = 0
    roomStatus = {}
    for room in geofencingData:
        i += 1
        roomStatus["room"+str(i)] = False
    
    i = 0
    for room in geofencingData: 
        i += 1 
        # When using the roomCheck function, just pass the room you are in
        # -> roomCheck(curLoc, geofencingData["room"+str(i)])
        if geofencingData["room"+str(i)]["type"] == "4 corner":
            roomStatus["room"+str(i)] = roomCheck(curLoc, geofencingData["room"+str(i)])
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

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same

path = os.path.dirname(__file__)
f = open(path + '/geofenceData.json', "r")
geofencingData = json.load(f)
f.close()

#checking if anyone in room
while True:
    #"pull" current location
    curLoc = (20,20)
    initialStatus = checkLoc(curLoc, geofencingData)

    #"pull" current location
    curLoc = (3.5,3)
    finalStatus = checkLoc(curLoc, geofencingData)

    added, removed, modified, same = dict_compare(initialStatus, finalStatus)
    for room in modified:
        if modified[room][1] == True:
            print("Turn light ON for " + str(room))
        else:
            print("Turn light OFF for " + str(room))