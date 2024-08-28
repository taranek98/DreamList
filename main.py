from tkinter import *

def addNewElement(title):
   list_wish.insert(list_wish.size(), title)

def newElementWindow():
    
    def closeWindow():
        addNewElement(entry_title.get())
        newWindow.destroy()

    newWindow = Toplevel(window)        
    newWindow.title('Dodaj nową grę')
    newWindow.geometry("400x130")
    newWindow.config(background='#312d2d')

    entry_title = Entry(newWindow, width = 40)
    entry_title.place(x = 100, y = 25)

    button_accept = Button(newWindow, text='Zatwierdź', width=10, height=2, command=closeWindow)
    button_accept.place(x = 100, y = 75)

    button_cancel = Button(newWindow, text='Anuluj', width=10, height=2, command=lambda:newWindow.destroy())
    button_cancel.place(x = 220, y = 75)

    label_title = Label(newWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
    label_title.place(x = 40, y = 20)

def defineCurrentSelectElement(self):
    global list_wish_currentSelectElement
    if(len(list_wish.curselection()) != 0):
        list_wish_currentSelectElement = list_wish.curselection()[0]
        print(list_wish_currentSelectElement)
    else:
        list_wish_currentSelectElement = -1

def moveElementUp(self):
    moveElementOnList(True)

def moveElementDown(self):
    moveElementOnList(False)

def moveElementOnList(moveIsUp):
    print(list_wish.curselection()[0])
    if(len(list_wish.curselection()) != 0): #check is element of list is selected
        if(list_wish.curselection()[0] != 0 or moveIsUp == False): #check is element can move up
            if(list_wish.curselection()[0] < list_wish.size()-1 or moveIsUp == True): #check is element can move down
                currentSelectElement = list_wish.curselection()[0]
                var = list_wish.get(currentSelectElement)
                list_wish.delete(currentSelectElement)
                if(moveIsUp == True):
                    list_wish.insert(currentSelectElement-1, var)
                else:
                    list_wish.insert(currentSelectElement+1, var)
                list_wish.activate(currentSelectElement)
        


window = Tk()
window.title('Dream List')
window.geometry("700x500")
window.config(background='#312d2d')


button_addElement = Button(window, text='Dodaj grę', width=15, height= 2, command=newElementWindow)
button_addElement.place(x = 290, y = 420)

label_wishListTitle = Label(window, text="Lista życzeń")
label_wishListTitle.place(x = 490, y = 20)

list_wish = Listbox(window, height=20, width=40)
list_wish.place(x = 400, y = 50)
list_wish.insert(0, 'The Legend of Zelda Tears of the Kingdom')
list_wish.insert(2, "Pokemom Let's go Pikachu")
list_wish.insert(1, 'Dark Souls Remaster')
list_wish.bind('<Up>', moveElementUp)
list_wish.bind('<Down>', moveElementDown)
# list_wish.bind('<Button-1>', defineCurrentSelectElement)
list_wish_currentSelectElement = -1

label_finishListTitle = Label(window, text="Lista ukończonych gier")
label_finishListTitle.place(x = 130, y = 20)

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.insert(0, 'The Legend of Zelda Breath of the Wild')


window.mainloop()