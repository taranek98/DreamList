#File contain functions executes action on lists element

from tkinter import *
from window import showMessage
from sideFunctions import checkIfActive_arg1, getSelectElement

def moveElementOnList(moveIsUp, list):
    if(checkIfActive_arg1(list) == True): 
        currentSelectElement = getSelectElement(list)
        if(currentSelectElement != 0 or moveIsUp == False): #check is element can move up
            if(currentSelectElement < list.size()-1 or moveIsUp == True): #check is element can move down
                var = list.get(currentSelectElement)
                list.delete(currentSelectElement)
                if(moveIsUp == True):
                    list.insert(currentSelectElement-1, var)
                else:
                    list.insert(currentSelectElement+1, var)
                list.activate(currentSelectElement)

def moveElementToOtherList(window, listSource, listDestin):
    if(checkIfActive_arg1(listSource) == True):
        listDestin.insert(END, listSource.get(listSource.curselection()))
        listSource.delete(listSource.curselection())
    else:
        showMessage("Zaznacz grę aby dodać do listy", window)

def deleteElement(window, list):
    if(checkIfActive_arg1(list) == True):
        list.delete(list.curselection()[0])
    else:
        showMessage("Zaznacz grę aby usunąć do listy", window)



