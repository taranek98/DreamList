from tkinter import *
listWishIsSelected = False
listFinishIsSelected = False

def selectListWish(event):
    global listWishIsSelected
    listWishIsSelected = True
    print("Select list wish")

def deselectListWish(event):
    global listWishIsSelected
    listWishIsSelected = False
    print("Deselect list wish")

def selectListFinish(event):
    global listFinishIsSelected
    listFinishIsSelected = True
    print("Select list finish")

def deselectListFinish(event):
    global listFinishIsSelected
    listFinishIsSelected = False
    print("Deselect list finish")