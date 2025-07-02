#File contain functions executes action on lists element

from tkinter import *
from window import showMessage
from sideFunctions import checkIfActive_arg1, checkIfActive_arg3, getSelectElement, convertListToObject
from database import readFromJson, saveToJson

def moveElementOnList(moveIsUp, list):
    if(checkIfActive_arg1(list) == True): 
        currentSelectElement = getSelectElement(list)
        if(currentSelectElement != 0 or moveIsUp == False): #check is element can move up
            if(currentSelectElement < list.size()-1 or moveIsUp == True): #check is element can move down
                var = list.get(currentSelectElement)
                list.delete(currentSelectElement)
                if(moveIsUp == True):
                    list.insert(currentSelectElement-1, str(currentSelectElement) + '. ' + var[var.find(". ")+2:])
                    var = list.get(currentSelectElement)
                    list.delete(currentSelectElement)
                    list.insert(currentSelectElement, str(currentSelectElement+1) + '. ' + var[var.find(". ")+2:])
                else:
                    list.insert(currentSelectElement+1, str(currentSelectElement+2) + '. ' + var[var.find(". ")+2:])
                    var = list.get(currentSelectElement)
                    list.delete(currentSelectElement)
                    list.insert(currentSelectElement, str(currentSelectElement+1) + '. ' + var[var.find(". ")+2:])
                list.activate(currentSelectElement)

def moveElementToOtherList(window, listSource, listDestin):
    if(checkIfActive_arg1(listSource) == True):
        listDestin.insert(END,str(listDestin.size()+1) + '. ' + listSource.get(listSource.curselection())[listSource.get(listSource.curselection()).find(". ")+2:])
        listSource.delete(listSource.curselection())
        refreshList(listSource)
    else:
        showMessage("Zaznacz grę aby dodać do listy", window)

def deleteElement(window, list1, list2, list3):
    activeList = checkIfActive_arg3(list1, list2, list3)
    if(activeList != None):
        activeList.delete(activeList.curselection()[0])
        refreshList(activeList)
    else:
        showMessage("Zaznacz grę aby usunąć do listy", window)

def importDataToList(list_wish, list_playing, list_finish, window):
    try:
        clearList(list_wish)
        objects = readFromJson('wish')
        convertAndLoadData(list_wish, objects)
        clearList(list_playing)
        objects = readFromJson('playing')
        convertAndLoadData(list_playing, objects)
        clearList(list_finish)
        objects = readFromJson('finish')
        convertAndLoadData(list_finish, objects)
    except:
        showMessage("Wczytywanie zakończone niepowodzeniem", window)
            
def exportDataFromList(list_wish, list_playing, list_finish, window):
    operationResult = saveToJson(convertListToObject(list_wish), 'wish')
    if(operationResult == True):
        operationResult = saveToJson(convertListToObject(list_playing), 'playing')
        if(operationResult == True):
            operationResult = saveToJson(convertListToObject(list_finish), 'finish')
            if(operationResult == False):
                showMessage("Zapis zakończony niepowodzeniem", window)
        else:
            showMessage("Zapis zakończony niepowodzeniem", window)
    else:
        showMessage("Zapis zakończony niepowodzeniem", window)

def convertAndLoadData(list, readObjects):
    for object in readObjects:
        list.insert(object["ID"], object["Name"])

def clearList(list):
    lastIndex = list.size()
    while(lastIndex >= 0):
        list.delete(lastIndex)
        lastIndex = lastIndex - 1 
        
def refreshList(list):
    index = 0; 
    lasIndex = list.size()
    while(index < lasIndex):
        var = list.get(index)
        list.delete(index)
        list.insert(index, str(index+1) + '. ' + var[var.find(". ")+2:])
        index += 1
