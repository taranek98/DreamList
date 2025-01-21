import json

def saveToJson(list, listName):
    operationResult = True
    try:
        if(listName == 'wish'):
            fs = open("table_wish.json", "w")
        elif(listName == 'playing'):
            fs = open("table_playing.json", "w")
        else:
            fs = open("table_finish.json", "w")
        fs.write(json.dumps(list, indent = 3))
    except: 
        operationResult = False
    fs.close()

    return operationResult

def readFromJson(listName):
    operationResult = True
    if(listName == 'wish'):
        fs = open("table_wish.json", "r")
    elif(listName == 'playing'):
        fs = open("table_playing.json", "r")
    else:
        fs = open("table_finish.json", "r")
    jsonObject = json.loads(fs.read())
    fs.close()
    return jsonObject
    

