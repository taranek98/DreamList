from tkinter import Toplevel, Entry, Button, Label

def addElement(window, list):
    newWindow = Toplevel(window)        
    newWindow.title('Dodaj nową grę')
    newWindow.geometry("400x130")
    newWindow.config(background='#312d2d')

    entry_title = Entry(newWindow, width = 40)
    entry_title.place(x = 100, y = 25)

    button_accept = Button(newWindow, text='Zatwierdź', width=10, height=2, command=lambda:newWindow.destroy())
    button_accept.place(x = 100, y = 75)
    button_accept.bind("<Button-1>", lambda event:list.insert(list.size(), entry_title.get()),'+')
    button_accept.bind("<Button-1>", lambda event:newWindow.destroy(), "+")

    button_cancel = Button(newWindow, text='Anuluj', width=10, height=2, command=lambda:newWindow.destroy())
    button_cancel.place(x = 220, y = 75)

    label_title = Label(newWindow, text="Tytuł:", background = '#312d2d', foreground= "white", font=('Arial',16))
    label_title.place(x = 40, y = 20)


def showMessage(message, window):
    messageWindow = Toplevel(window)        
    messageWindow.title('Message')
    messageWindow.geometry("300x100")
    messageWindow.config(background='#312d2d')

    label_message = Label(messageWindow, text = message)
    label_message.place(x = 55, y = 30)

    button_close = Button(messageWindow, text = 'Zamknij', command = messageWindow.destroy)
    button_close.place(x = 120, y = 65)