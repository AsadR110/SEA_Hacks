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
    #"pull" current location
    curLoc = (20,20)

    roomStatus1 = checkLoc(curLoc, geofencingData, roomStatus)
    print(roomStatus1)
    time.sleep(2)

    #"pull" current location
    curLoc = (3.5,3)
    roomStatus2 = checkLoc(curLoc, geofencingData, roomStatus)
    print(roomStatus2)

#    if roomStatus1 != roomStatus2:
#        for room in roomStatus1:
#            print(room)
#    else:
#        print(roomStatus1)
#        print(roomStatus2)