from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Shopping List")
list = []

# ------buttons Function------


def btnAdd():
    list.append(item.get())
    item.delete(0, END)


def btnShow():
    for item in list:
        myListBox.insert(END, item)

# ------buttons function------


# ------buttons------
addListbtn = Button(root, text="Add To List", command=btnAdd)
addListbtn.grid(row=3, column=2)
show = Button(root, text="Show List", command=btnShow)
show.grid(row=4, column=2)
# ------buttons------

myListBox = Listbox(root, width=20)
myListBox.grid(row=6, column=2)

lbl = Label(root, text="Item")
lbl.grid(row=1, column=1)

item = Entry(root, width=20)
item.grid(row=1, column=2)


root.mainloop()
