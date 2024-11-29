from tkinter import *
from window import addElement, showMessage

def defineCurrentSelectElement(list):
    if(len(list.curselection()) != 0): #check is element of list is selected
        global currentSelectElement
        currentSelectElement = list.curselection()[0]

def moveElementOnList(moveIsUp, list, isMouse):
    if(len(list.curselection()) != 0): #check is element of list is selected
        global currentSelectElement
        if(isMouse == False):
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


def moveElementToOtherList():
    if(len(list_wish.curselection()) != 0): #check is element of list is selected
        list_finish.insert(END, list_wish.get(list_wish.curselection()))
        list_wish.delete(list_wish.curselection())
        print(list_wish.get(0,5))
        print(list_wish.size())
    else:
        showMessage("Zaznacz grę aby dodać do listy", window)

def deleteElement():
    list = list_wish
    if(len(list.curselection()) != 0):
        list.delete(list.curselection()[0])
    else:
        showMessage("Zaznacz grę aby usunąć do listy", window)

def editElement(list):
    def saveEdit(title, index):
        list.delete(index)
        list.insert(index, title)

    if(len(list.curselection()) != 0):
        currentIndex = list.curselection()[0]
        editWindow = Toplevel(window)        
        editWindow.title('Edytuj grę')
        editWindow.geometry("400x130")
        editWindow.config(background='#312d2d')

        entry_title = Entry(editWindow, width = 40)
        entry_title.insert(0, list.get(currentIndex))
        entry_title.place(x = 100, y = 25)

        button_accept = Button(editWindow, text='Zatwierdź', width=10, height=2)
        button_accept.place(x = 100, y = 75)
        button_accept.bind('<Button-1>', lambda event: saveEdit(entry_title.get(),currentIndex))
        button_accept.bind('<Button-1>', lambda event: editWindow.destroy(), add= '+')

        button_cancel = Button(editWindow, text='Anuluj', width=10, height=2, command=lambda:editWindow.destroy())
        button_cancel.place(x = 220, y = 75)

        label_title = Label(editWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
        label_title.place(x = 40, y = 20)
    else:
        showMessage("Zaznacz grę aby ją edytować", window)


window = Tk()
window.title('Dream List')
window.geometry("700x500")
window.config(background='#312d2d')


button_addElement = Button(window, text='Dodaj grę', width=15, height= 2, command=lambda:addElement(window, list_wish))
button_addElement.place(x = 220, y = 420)

button_editElement = Button(window, text='Edytuj', width=15, height= 2, command= lambda: editElement(list_wish))
button_editElement.place(x = 370, y = 420)

button_MoveElement = Button(window, text='<-', command = moveElementToOtherList)
button_MoveElement.place(x = 340, y = 200)

button_deleteElement = Button(window, text='kosz', command = deleteElement)
button_deleteElement.place(x = 335, y = 280)

label_wishListTitle = Label(window, text="Lista życzeń")
label_wishListTitle.place(x = 480, y = 20)

list_wish = Listbox(window, height=20, width=40)
list_wish.place(x = 400, y = 50)
list_wish.insert(0, 'The Legend of Zelda Tears of the Kingdom')
list_wish.insert(2, "Pokemom Let's go Pikachu")
list_wish.insert(1, 'Dark Souls Remaster')
list_wish.insert(2, '1111111111')
list_wish.insert(3, '2222222222')
list_wish.insert(4, '33333333')
list_wish.bind('<Up>', lambda event:moveElementOnList(True, list_wish, False))
list_wish.bind('<Down>', lambda event:moveElementOnList(False, list_wish, False))

label_finishListTitle = Label(window, text="Lista ukończonych gier")
label_finishListTitle.place(x = 130, y = 20)

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.insert(0, 'The Legend of Zelda Breath of the Wild')
list_finish.insert(1, '1111111111')
list_finish.insert(2, '2222222222')
list_finish.insert(3, '33333333')
list_finish.bind('<Up>', lambda event:moveElementOnList(True, list_finish, False))
list_finish.bind('<Down>', lambda event:moveElementOnList(False, list_finish, False))

window.mainloop()