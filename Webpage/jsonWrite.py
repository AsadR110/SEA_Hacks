import json

roomData = {
    "room1": {
        "name" : "bedroom",
        "type" : "4 corner",
        "cornersX" : [0,0,4,4],
        "cornersY" : [0,3,0,3]
    },
    "room2": {
        "name" : "bathroom",
        "type" : "4 corner",
        "cornersX" : [5,5,6,6],
        "cornersY" : [0,5,0,5]
    },
    "room3" : {
        "name" : "living room",
        "type" : "6 corner",
        "cornersX" : [9, 9, 7, 7, 7, 10, 10],
        "cornersY" : [2, 7, 7, 2, 0, 0, 2]
    }
}

# Write
with open('demo.json', 'w') as json_write:
	json.dump(roomData, json_write)

# Read
with open('demo.json', 'r') as json_read:
	data = json.load(json_read)
	print(json.dumps(data, indent=4))

