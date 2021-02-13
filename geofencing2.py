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
    # return False

def checkLoc(curLoc, geofencingData, roomStatus):
    i = 0
    for room in geofencingData: 
        i += 1 
        # When using the roomCheck function, just pass the room you are in
        # -> roomCheck(curLoc, geofencingData["room"+str(i)])
        if geofencingData["room"+str(i)]["type"] == "4 corner":
            # Method 1
            # roomStatus["room"+str(i)] = roomCheck(curLoc, geofencingData["room"+str(i)])
            # Method 2
            if roomCheck(curLoc, geofencingData["room"+str(i)]) is True:
                roomStatus["room"+str(i)] == True
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
            # Define first rectangle
            for j in range(4):
                room6Corners["rectangle 1"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                room6Corners["rectangle 1"]["cornersY"].append(geofencingData["room"+str(i)]["cornersY"][j])
            
            # roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 1"])
            if roomCheck(curLoc, room6Corners["rectangle 1"]) is True:
                roomStatus["room"+str(i)] == True
        
            # If the first rectangle of the room is true, no need to check the second one
            if roomStatus["room"+str(i)] == False:
                # Define second rectangle
                for j in range(4, 7):
                    room6Corners["rectangle 2"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                    room6Corners["rectangle 2"]["cornersY"].append(geofencingData["room"+str(i)]["cornersX"][j])

                # roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 2"])
                if roomCheck(curLoc, room6Corners["rectangle 2"]) is True:
                    roomStatus["room"+str(i)] == True

    return roomStatus

path = os.path.dirname(__file__)
f = open(path + '/geofenceData.json', "r")
geofencingData = json.load(f)
f.close()

#populating dictionary with all rooms
i = 0
roomStatus = {
    "room1" : False,
    "room2" : False,
    "room3" : False,
}
for room in geofencingData:
    i += 1
    roomStatus["room"+str(i)] = False

# People positions
curLoc = (11, 4.5)
curLocMultiple = ((11, 4.5), (3.5, 3))

numberOfPeople = len(curLocMultiple)
for i in range(numberOfPeople):
    print(f'Person {i}')
    print(curLocMultiple[i])
    print(checkLoc(curLocMultiple[i], geofencingData, roomStatus))

curLocMultiple = ((7, 4), (3.5, 3))


#checking if anyone in room
#while True:
#    #"pull" current location
#    curLoc = (20,20)
#
#    roomStatus1 = checkLoc(curLoc, geofencingData, roomStatus)
#    print(roomStatus1)
#    time.sleep(2)
#
#    #"pull" current location
#    curLoc = (3.5,3)
#    roomStatus2 = checkLoc(curLoc, geofencingData, roomStatus)
#    print(roomStatus2)

#    if roomStatus1 != roomStatus2:
#        for room in roomStatus1:
#            print(room)
#    else:
#        print(roomStatus1)
#        print(roomStatus2)