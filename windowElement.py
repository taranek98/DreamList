#File contain function with element function but can not be implemented by file element.py

def saveAdd(list, title):
    list.insert(list.size(), title)

def saveEdit(list ,title, index):
        list.delete(index)
        list.insert(index, title)