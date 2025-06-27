#File initialize main window program and execute program loop

from tkinter import *
from window import addElement, editElement, closeMainWindow
from element import *
from tests import *
from database import *
from tkinter import font




# Main window initialization
window = Tk()
window.title('Dream List')

f = font.nametofont('TkDefaultFont')
fontSize = f.actual('size')

# print(((window.winfo_screenwidth() / 2) * 0.35))
# print(window.winfo_screenwidth())
window.config(background='#312d2d', width = window.winfo_screenwidth()/2, height = window.winfo_screenheight()/2)
# window.bind('<Destroy>', lambda event: exportDataFromList(list_wish, list_playing, list_finish, window))
window.bind('<+>', lambda event: addElement(window, list_wish))


#Buttons initialization
button_addElement = Button(window, text='Dodaj grę', width = 10, command=lambda:addElement(window, list_wish))
button_addElement.place(x = (window.winfo_screenwidth() / 2) * 0.25, y = (window.winfo_screenheight() / 2) * 0.89)

button_editElement = Button(window, text='Edytuj', width = 10, command= lambda: editElement(window, list_wish, list_playing, list_finish))
button_editElement.place(x = (window.winfo_screenwidth() / 2) * 0.45, y = (window.winfo_screenheight() / 2) * 0.89)

button_deleteElement = Button(window, text='Usuń', width = 10, command = lambda: deleteElement(window, list_wish, list_playing, list_finish))
button_deleteElement.place(x = (window.winfo_screenwidth() / 2) * 0.65, y = (window.winfo_screenheight() / 2) * 0.89)

#Labels initialization
label_wishListTitle = Label(window, text="Lista życzeń", width=20)
label_wishListTitle.place(x = ((window.winfo_screenwidth() / 2) * 0.73), y = (window.winfo_screenheight() / 2) * 0.05)

label_playingListTitle = Label(window, text="Obecnie grane", width=20)
label_playingListTitle.place(x = (window.winfo_screenwidth() / 2) * 0.41, y = (window.winfo_screenheight() / 2) * 0.05)

label_finishListTitle = Label(window, text="Lista ukończonych gier", width=20)
label_finishListTitle.place(x = ((window.winfo_screenwidth() / 2) * 0.09), y = (window.winfo_screenheight() / 2) * 0.05)

#List initializtion
list_wish = Listbox(window)
list_wish.place(x = (window.winfo_screenwidth() / 2) * 0.67, y = (window.winfo_screenheight() / 2) * 0.12, 
                width= window.winfo_screenwidth()/2 * 0.3, height = (window.winfo_screenheight() / 2) * 0.72)
list_wish.bind('<Up>', lambda event:moveElementOnList(True, list_wish))
list_wish.bind('<Down>', lambda event:moveElementOnList(False, list_wish))
list_wish.bind('<Left>', lambda event: moveElementToOtherList(window, list_wish, list_playing))

list_playing = Listbox(window)
list_playing.place(x = ((window.winfo_screenwidth() / 2) * 0.35), y = (window.winfo_screenheight() / 2) * 0.12, 
                width= window.winfo_screenwidth()/2 * 0.3, height = (window.winfo_screenheight() / 2) * 0.72)
list_playing.bind('<Down>', lambda event:moveElementOnList(False, list_playing))
list_playing.bind('<Up>', lambda event:moveElementOnList(True, list_playing))
list_playing.bind('<Left>', lambda event: moveElementToOtherList(window, list_playing, list_finish))

list_finish = Listbox(window)
list_finish.place(x = ((window.winfo_screenwidth() / 2) * 0.03), y = (window.winfo_screenheight() / 2) * 0.12, 
                  width= window.winfo_screenwidth()/2 * 0.3, height = (window.winfo_screenheight() / 2) * 0.72)
list_finish.bind('<Up>', lambda event:moveElementOnList(True, list_finish))
list_finish.bind('<Down>', lambda event:moveElementOnList(False, list_finish))
# print(int((window.winfo_screenwidth()/2 * 0.35)/fontSize))

# Menubar init
menuBar = Menu(window)
file = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(menu = file, label= 'File')
file.add_command(command=lambda: exportDataFromList(list_wish, list_playing, list_finish, window), label= 'Save')
file.add_command(command=lambda: importDataToList(list_wish, list_playing, list_finish, window), label= 'Load')
importDataToList(list_wish, list_playing, list_finish, window)
# TESTS
# fillWishList(list_wish)
# fillFinishList(list_finish)
# fillPlayingList(list_playing)

# Display menubar
window.config(menu=menuBar)

# Handled exit button
window.protocol("WM_DELETE_WINDOW", lambda: closeMainWindow(window))

# program loop
window.mainloop()