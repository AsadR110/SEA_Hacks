import json
import os
import time
import requests

# Check if a person is in a certain room
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

# Determine if a room is 4 or 6 Corners, If 4 corners, check that room
# If 6 corners, split room into "2" rooms and check both
def personCheckLocation(curLoc, geofencingData, numberOfRooms):
    roomStatus = {}
    for i in range(numberOfRooms): # Number of rooms
        roomStatus["room"+str(i+1)] = False
    i = 0
    for room in geofencingData: 
        i += 1 
        # When using the roomCheck function, just pass the room you are in
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
            # Define first rectangle
            for j in range(4):
                room6Corners["rectangle 1"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                room6Corners["rectangle 1"]["cornersY"].append(geofencingData["room"+str(i)]["cornersY"][j])
            
            # roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 1"])
            if roomCheck(curLoc, room6Corners["rectangle 1"]) is True:
                roomStatus["room"+str(i)] = True
        
            # If the first rectangle of the room is true, no need to check the second one
            if roomStatus["room"+str(i)] == False:
                # Define second rectangle
                for j in range(4, 7):
                    room6Corners["rectangle 2"]["cornersX"].append(geofencingData["room"+str(i)]["cornersX"][j]) 
                    room6Corners["rectangle 2"]["cornersY"].append(geofencingData["room"+str(i)]["cornersX"][j])

                roomStatus["room"+str(i)] = roomCheck(curLoc, room6Corners["rectangle 2"])

    return roomStatus

# Check all person position in the house
def checkAllPersons(curLocMultiple, geofencingData, numberOfRooms):
    numberOfPeople = len(curLocMultiple)

    personStatus = []
    personStatusAll = {}
    for i in range(numberOfPeople):
        # Check position of each person
        personStatus.append(personCheckLocation(curLocMultiple[i], geofencingData, numberOfRooms))
        # Initialize all status to false
        personStatusAll["room"+str(i+1)] = False

    # Combine all person statuses into one dictionary to easily monitor any position changes
    for i in range(numberOfRooms): 
        for j in range(numberOfPeople):
            if personStatus[j]['room'+str(i+1)] is True:
                personStatusAll['room'+str(i+1)] = True
    
    return personStatusAll

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

numberOfRooms = len(geofencingData)

# Determine Initial Position / Previous Position of Everyone
curLocMultiple = [(1,1), (20,20), (21,21)]
previousStatus = checkAllPersons(curLocMultiple, geofencingData, numberOfRooms)
print(previousStatus)

while True:
    #Pull current position
    f = open(path + '/curLocData.json', "r")
    curLocData = json.load(f)
    f.close()

    curLocMultiple = []
    i = 0
    for person in curLocData:
        i += 1
        curLocMultiple.append((curLocData["person" + str(i)]["X"], curLocData["person" + str(i)]["Y"]))

    currentStatus = checkAllPersons(curLocMultiple, geofencingData, numberOfRooms)

    # Check if a light needs to be turned on/off
    added, removed, modified, same = dict_compare(previousStatus, currentStatus)
    for room in modified:
        if modified[room][1] == True:
            print("Turn light ON for " + str(room))
            os.system("python3 homeScript.py -s " + str(room) + " 1")
        else:
            print("Turn light OFF for " + str(room))
            os.system("python3 homeScript.py -s " + str(room) + " 0")
    
    previousStatus = currentStatus
    time.sleep(2)
    print("refresh")