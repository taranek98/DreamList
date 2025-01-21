#File contains other functions which help in the rest functions

def checkIfActive_arg1(list):
    if(len(list.curselection()) != 0):
        return True
    else:
        return False
    
def checkIfActive_arg3(list1, list2, list3):
    if(len(list1.curselection()) != 0):
        return list1
    elif(len(list2.curselection()) != 0):
        return list2
    elif(len(list3.curselection()) != 0):
        return list3
    else:
        return None
    
def getSelectElement(list):
    return list.curselection()[0]

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