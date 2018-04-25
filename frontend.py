#from tkinter import *
from tkinter import Tk
from tkinter import Button
from tkinter import Listbox
from tkinter import Entry
from tkinter import Label
from tkinter import Scrollbar
from tkinter import StringVar
from tkinter import Text
from tkinter import END

from backend import Database

bk = Database("book.db")

def view_command():
    lb.delete(0, END)
    for row in bk.view():
        lb.insert(END,row)

def search_command():
    lb.delete(0, END)
    for row in bk.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        lb.insert(END,row)

def add_command():
    lb.delete(0, END)
    bk.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lb.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def update_command():
    bk.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lb.delete(0,END)
    lb.insert(END,(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    id = selected_tuple[0]
    bk.delete(id)
    lb.delete(0,END)
    lb.insert(END,"Deleted Successfully!")



def get_selected_row(event):
    global selected_tuple
    index = lb.curselection()[0]
    selected_tuple = lb.get(index)

    e1.delete(0, END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])

    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])

    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])    
    

window = Tk()

window.title("Book Store")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

lb = Listbox(window, width = 30)
lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(window)
sb.grid(row = 2, column = 2, rowspan = 6)

lb.configure(yscrollcommand = sb.set)
sb.configure(command = lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window, text = "View All", width = 16, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry", width = 16, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 16, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 16, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete Selected", width = 16, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 16, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
