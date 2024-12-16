#File contains other functions which help in the rest functions

def checkIfActive_arg1(list):
    if(len(list.curselection()) != 0):
        return True
    else:
        return False
    
def checkIfActive_arg2(list1, list2):
    if(len(list1.curselection()) != 0):
        return list1
    elif(len(list2.curselection()) != 0):
        return list2
    else:
        return None
    
def getSelectElement(list):
    return list.curselection()[0]