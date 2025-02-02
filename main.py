#File initialize main window program and execute program loop

from tkinter import *
from window import addElement, editElement, closeMainWindow
from element import *
from tests import *
from database import *



# Main window initialization
window = Tk()
window.title('Dream List')
window.geometry("1040x500")
window.config(background='#312d2d')
# window.bind('<Destroy>', lambda event: exportDataFromList(list_wish, list_playing, list_finish, window))
window.bind('<+>', lambda event: addElement(window, list_wish))

#Buttons initialization
button_addElement = Button(window, text='Dodaj grę', width=15, height= 2, command=lambda:addElement(window, list_wish))
button_addElement.place(x = 285, y = 420)

button_editElement = Button(window, text='Edytuj', width=15, height= 2, command= lambda: editElement(window, list_wish, list_playing, list_finish))
button_editElement.place(x = 645, y = 420)

button_MoveElementToFinish = Button(window, text='<-', command = lambda: moveElementToOtherList(window, list_playing, list_finish))
button_MoveElementToFinish.place(x = 340, y = 200)

button_MoveElementToPlaying = Button(window, text='<-', command = lambda: moveElementToOtherList(window, list_wish, list_playing))
button_MoveElementToPlaying.place(x = 675, y = 200)

button_deleteElement = Button(window, text='Usuń', width=15, height= 2, command = lambda: deleteElement(window, list_wish, list_playing, list_finish))
button_deleteElement.place(x = 465, y = 420)

#Labels initialization
label_playingListTitle = Label(window, text="Obecnie grane")
label_playingListTitle.place(x = 480, y = 20)

label_wishListTitle = Label(window, text="Lista życzeń")
label_wishListTitle.place(x = 820, y = 20)

label_finishListTitle = Label(window, text="Lista ukończonych gier")
label_finishListTitle.place(x = 130, y = 20)

#List initializtion
list_wish = Listbox(window, height=20, width=40)
list_wish.place(x = 730, y = 50)
list_wish.bind('<Up>', lambda event:moveElementOnList(True, list_wish))
list_wish.bind('<Down>', lambda event:moveElementOnList(False, list_wish))

list_playing = Listbox(window, height=20, width=40)
list_playing.place(x = 400, y = 50)
list_playing.bind('<Up>', lambda event:moveElementOnList(True, list_playing))
list_playing.bind('<Down>', lambda event:moveElementOnList(False, list_playing))

list_finish = Listbox(window, height=20, width=40)
list_finish.place(x = 60, y = 50)
list_finish.bind('<Up>', lambda event:moveElementOnList(True, list_finish))
list_finish.bind('<Down>', lambda event:moveElementOnList(False, list_finish))

# Menubar init
menuBar = Menu(window)
file = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(menu = file, label= 'File')
file.add_command(command=lambda: exportDataFromList(list_wish, list_playing, list_finish, window), label= 'Save')
file.add_command(command=lambda: importDataToList(list_wish, list_playing, list_finish, window), label= 'Load')
# importDataToList(list_wish, list_playing, list_finish)
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