import json
import os
import time

def checkLoc(curLoc, geofencingData, roomStatus):
    i = 0
    for room in geofencingData:
        i += 1
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
            pass #@neil

    return roomStatus


path = os.path.dirname(__file__)
f = open(path + '/sample.json', "r")
geofencingData = json.load(f)
f.close()

#populating dictionary with all rooms
i = 0
roomStatus = {}
for room in geofencingData:
    i += 1
    roomStatus["room"+str(i)] = False

#checking if anyone in room
while True:
    
    curLoc = (20,20)
    print(checkLoc(curLoc, geofencingData, roomStatus))