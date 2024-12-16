#File initialize main window program and execute program loop

from tkinter import *
from window import addElement, editElement
from element import *
from tests import *

# Main window initialization
window = Tk()
window.title('Dream List')
window.geometry("700x500")
window.config(background='#312d2d')

#Buttons initialization
button_addElement = Button(window, text='Dodaj grę', width=15, height= 2, command=lambda:addElement(window, list_wish))
button_addElement.place(x = 220, y = 420)

button_editElement = Button(window, text='Edytuj', width=15, height= 2, command= lambda: editElement(window, list_wish, list_finish))
button_editElement.place(x = 370, y = 420)

button_MoveElement = Button(window, text='<-', command = lambda: moveElementToOtherList(window, list_wish, list_finish))
button_MoveElement.place(x = 340, y = 200)

button_deleteElement = Button(window, text='kosz', command = lambda: deleteElement(window, list_wish))
button_deleteElement.place(x = 335, y = 280)

#Labels initialization
label_wishListTitle = Label(window, text="Lista życzeń")
label_wishListTitle.place(x = 480, y = 20)

label_finishListTitle = Label(window, text="Lista ukończonych gier")
label_finishListTitle.place(x = 130, y = 20)

#List initializtion
list_wish = Listbox(window, height=20, width=40)
list_wish.place(x = 400, y = 50)
list_wish.bind('<Up>', lambda event:moveElementOnList(True, list_wish))
list_wish.bind('<Down>', lambda event:moveElementOnList(False, list_wish))

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.bind('<Up>', lambda event:moveElementOnList(True, list_finish))
list_finish.bind('<Down>', lambda event:moveElementOnList(False, list_finish))

# TESTS
fillWishList(list_wish)
fillFinishList(list_finish)

window.mainloop()