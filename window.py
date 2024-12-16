# File contains functions responsible for create new windows

from tkinter import *
from sideFunctions import checkIfActive_arg2, getSelectElement
from windowElement import *

def addElement(window, list):
    newWindow = Toplevel(window)        
    newWindow.title('Dodaj nową grę')
    newWindow.geometry("400x130")
    newWindow.config(background='#312d2d')
    newWindow.bind("<Return>", lambda event: saveAdd(list, entry_title.get()),'+')
    newWindow.bind("<Return>", lambda event: newWindow.destroy(), "+")
    newWindow.bind("<Escape>", lambda event:  newWindow.destroy())

    entry_title = Entry(newWindow, width = 40)
    entry_title.place(x = 100, y = 25)

    button_accept = Button(newWindow, text='Zatwierdź', width=10, height=2, command=lambda:newWindow.destroy())
    button_accept.place(x = 100, y = 75)
    button_accept.bind("<Button-1>", lambda event: saveAdd(list, entry_title.get()),'+')
    button_accept.bind("<Button-1>", lambda event: newWindow.destroy(), "+")
    
    button_cancel = Button(newWindow, text='Anuluj', width=10, height=2, command=lambda:newWindow.destroy())
    button_cancel.place(x = 220, y = 75)

    label_title = Label(newWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
    label_title.place(x = 40, y = 20)



def editElement(window, list1, list2):
    activeList = checkIfActive_arg2(list1, list2)
    if(activeList != None):
        currentIndex = getSelectElement(activeList)
        editWindow = Toplevel(window)        
        editWindow.title('Edytuj grę')
        editWindow.geometry("400x130")
        editWindow.config(background='#312d2d')
        editWindow.bind("<Return>", lambda event: saveEdit(activeList, entry_title.get(),currentIndex),'+')
        editWindow.bind("<Return>", lambda event: editWindow.destroy(), "+")
        editWindow.bind("<Escape>", lambda event: editWindow.destroy())

        entry_title = Entry(editWindow, width = 40)
        entry_title.insert(0, activeList.get(currentIndex))
        entry_title.place(x = 100, y = 25)

        button_accept = Button(editWindow, text='Zatwierdź', width=10, height=2)
        button_accept.place(x = 100, y = 75)
        button_accept.bind('<Button-1>', lambda event: saveEdit(activeList, entry_title.get(),currentIndex))
        button_accept.bind('<Button-1>', lambda event: editWindow.destroy(), add= '+')

        button_cancel = Button(editWindow, text='Anuluj', width=10, height=2, command=lambda:editWindow.destroy())
        button_cancel.place(x = 220, y = 75)

        label_title = Label(editWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
        label_title.place(x = 40, y = 20)
    else:
        showMessage("Zaznacz grę aby ją edytować", window)



def showMessage(message, window):
    messageWindow = Toplevel(window)        
    messageWindow.title('Message')
    messageWindow.geometry("300x100")
    messageWindow.config(background='#312d2d')

    label_message = Label(messageWindow, text = message)
    label_message.place(x = 55, y = 30)

    button_close = Button(messageWindow, text = 'Zamknij', command = messageWindow.destroy)
    button_close.place(x = 120, y = 65)