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

def defineCurrentSelectElement(list):
    global currentSelectElement
    currentSelectElement = list.curselection()[0]

def moveElementOnList(moveIsUp, list):
    if(len(list.curselection()) != 0): #check is element of list is selected
        if(list.curselection()[0] != 0 or moveIsUp == False): #check is element can move up
            if(list.curselection()[0] < list.size()-1 or moveIsUp == True): #check is element can move down
                currentSelectElement = list.curselection()[0]
                var = list.get(currentSelectElement)
                list.delete(currentSelectElement)
                if(moveIsUp == True):
                    list.insert(currentSelectElement-1, var)
                else:
                    list.insert(currentSelectElement+1, var)
                list.activate(currentSelectElement)

def moveElementByMouse(list):
    if(len(list.curselection()) != 0): #check is element of list is selected
        global currentSelectElement
        print(list.curselection()[0])
        newSelection = list.curselection()[0]
        if(currentSelectElement > newSelection):
            moveElementOnList(False, list)
        elif(currentSelectElement < list.curselection()[0]):
            moveElementOnList(True, list)
        
        


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
list_wish.bind('<Up>', lambda event:moveElementOnList(True, list_wish))
list_wish.bind('<Down>', lambda event:moveElementOnList(False, list_wish))
list_wish.bind('<B1-Motion>', lambda event:moveElementByMouse(list_wish))
list_wish.bind('<FocusIn>', lambda event:defineCurrentSelectElement(list_wish))
currentSelectElement = -1

label_finishListTitle = Label(window, text="Lista ukończonych gier")
label_finishListTitle.place(x = 130, y = 20)

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.insert(0, 'The Legend of Zelda Breath of the Wild')
list_finish.insert(1, '1111111111')
list_finish.insert(2, '2222222222')
list_finish.insert(3, '33333333')
list_finish.bind('<Up>', lambda event:moveElementOnList(True, list_finish))
list_finish.bind('<Down>', lambda event:moveElementOnList(False, list_finish))
list_finish.bind('<B1-Motion>', lambda event:moveElementByMouse(list_finish))
list_finish.bind('<FocusIn>', lambda event:defineCurrentSelectElement(list_finish))


window.mainloop()