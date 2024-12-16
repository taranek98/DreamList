from tkinter import *
from window import showMessage
# from status import getSelectList

def moveElementOnList(moveIsUp, list):
    if(len(list.curselection()) != 0): #check is element of list is selected
        currentSelectElement = list.curselection()[0]
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
    if(len(listSource.curselection()) != 0): #check is element of list is selected
        listDestin.insert(END, listSource.get(listSource.curselection()))
        listSource.delete(listSource.curselection())
    else:
        showMessage("Zaznacz grę aby dodać do listy", window)

def deleteElement(window, list):
    list
    if(len(list.curselection()) != 0):
        list.delete(list.curselection()[0])
    else:
        showMessage("Zaznacz grę aby usunąć do listy", window)

def editElement(window):
    pass
    # list = getSelectList()
    # if(len(list.curselection()) != 0):
    #     currentIndex = list.curselection()[0]
    #     editWindow = Toplevel(window)        
    #     editWindow.title('Edytuj grę')
    #     editWindow.geometry("400x130")
    #     editWindow.config(background='#312d2d')

    #     entry_title = Entry(editWindow, width = 40)
    #     entry_title.insert(0, list.get(currentIndex))
    #     entry_title.place(x = 100, y = 25)

    #     button_accept = Button(editWindow, text='Zatwierdź', width=10, height=2)
    #     button_accept.place(x = 100, y = 75)
    #     button_accept.bind('<Button-1>', lambda event: saveEdit(list, entry_title.get(),currentIndex))
    #     button_accept.bind('<Button-1>', lambda event: editWindow.destroy(), add= '+')

    #     button_cancel = Button(editWindow, text='Anuluj', width=10, height=2, command=lambda:editWindow.destroy())
    #     button_cancel.place(x = 220, y = 75)

    #     label_title = Label(editWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
    #     label_title.place(x = 40, y = 20)
    # else:
    #     showMessage("Zaznacz grę aby ją edytować", window)

def saveEdit(list ,title, index):
        list.delete(index)
        list.insert(index, title)