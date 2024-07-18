from tkinter import *

window = Tk()
window.title('Dream List')
window.geometry("700x500")
window.config(background='#312d2d')


button_addElement = Button(window, text='Dodaj grę', width=15, height= 2)
button_addElement.place(x = 290, y = 420)

label_wishListTitle = Label(window, text="Wish List")
label_wishListTitle.place(x = 490, y = 20)

list_wish = Listbox(window, height=20, width=40)
list_wish.place(x = 400, y = 50)
list_wish.insert(0, 'The Legend of Zelda Tears of the Kingdom')
list_wish.insert(5, "Pokemom Let's go Pikachu")
list_wish.insert(2, 'Dark Souls Remaster')

label_finishListTitle = Label(window, text="Finish Game List")
label_finishListTitle.place(x = 130, y = 20)

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.insert(0, 'The Legend of Zelda Breath of the Wild')

window.mainloop()