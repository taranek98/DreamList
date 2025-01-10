import json

def saveToJson(list_wish, list_playing, list_finish):
    fs_wish = open("table_wish.json", "w")
    fs_wish.write(json.dumps(convertListToObject(list_wish)))
    fs_wish.close()

def convertListToObject(List):
    index = 0
    objects = list()
    while index < List.size():
        object = {
            "ID": index,
            "Name": List.get(index)
        }
        index = index + 1
        objects.append(object)
    return objects