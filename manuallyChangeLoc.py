import os
import json

path = os.path.dirname(__file__)

f = open(path + '/curLocData.json', "r")
curLocData = json.load(f)
f.close()

def enterRoom1():
    curLocData["person1"]["X"] = 1
    curLocData["person1"]["Y"] = 1

    f = open(path + '/curLocData.json', "w")
    json.dump(curLocData, f)
    f.close()

def exitRoom1():
    curLocData["person1"]["X"] = 1
    curLocData["person1"]["Y"] = 1

    f = open(path + '/curLocData.json', "w")
    json.dump(curLocData, f)
    f.close()

exitRoom1()