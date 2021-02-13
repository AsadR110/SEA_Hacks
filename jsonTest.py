import json
import requests

url = "ip"

# receives http post requests

rooms = {
    "room 1" : {
        "name" : "bedroom",
        "type" : "4 corner", 
        "cornersX" : [3, 3, 4, 5],
        "cornersY" : [1, 4, 1, 4]
    },
    "room 2" : {
        "name" : "bathroom",
        "type" : "4 corner",
        "cornersX" : [6, 6, 8, 8],
        "cornersY" : [1, 7, 1, 7]
    }
}

roomSerialized = json.dumps(rooms)
requests.post(url, json=roomSerialized)