from tkinter import *
from window import addElement
from element import *

window = Tk()
window.title('Dream List')
window.geometry("700x500")
window.config(background='#312d2d')

button_addElement = Button(window, text='Dodaj grę', width=15, height= 2, command=lambda:addElement(window, list_wish))
button_addElement.place(x = 220, y = 420)

button_editElement = Button(window, text='Edytuj', width=15, height= 2, command= lambda: editElement(window, list_wish))
button_editElement.place(x = 370, y = 420)

button_MoveElement = Button(window, text='<-', command = lambda: moveElementToOtherList(window, list_wish, list_finish))
button_MoveElement.place(x = 340, y = 200)

button_deleteElement = Button(window, text='kosz', command = lambda: deleteElement(window, list_wish))
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