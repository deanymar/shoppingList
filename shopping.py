from tkinter import *
from typing import List
root = Tk()
class Item:
    def __init__(self,name):
        self.name = name
        self.price = price

def btnAdd():
    list.append(item.get())
    item.delete(0,END)
def btnShow():
    for items in list:
        i = Item(items)
        myListBox.insert(END,i.name)
    
root.geometry("500x500")
root.title("Shopping List")

addListbtn = Button(root,text= "Add To List",command=btnAdd)
addListbtn.grid(row = 3,column= 2)
show = Button(root,text= "Show List",command=btnShow)
show.grid(row =4 ,column=2)

myListBox = Listbox(root,width=20)
myListBox.grid(row=6,column=2)

  
lbl = Label(root,text= "Item")
lbl.grid(row =1,column =1)

item = Entry(root,width = 20)
item.grid(row = 1, column =2)


lbl2 = Label(root,text = "Price")
lbl2.grid(row= 2, column =1)
price = Entry(root,width = 20)
try:
    price = float(int(price.get()))
except ValueError:
    price.config(text = "Not a Price")
price.grid(row =2, column = 2)

list = []













root.mainloop()