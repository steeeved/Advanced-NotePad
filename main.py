from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk
from datetime import datetime
import webbrowser

def New():
    text.delete('1.0', 'end')

def open():
    root.filename = filedialog.askopenfilename(
        initialdir = '/', 
        title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))
    )
    file = open(root.filename)
    text.insert('end', file.read())

# def save_as():
#     root.filename = filedialog.asksaveasfile(mode="w",
#     dafaulttextension='.txt')
#     if root.filename is None:
#         return file_save =  str(text.get(1.0,END))
#                root.filename.write(file_save)
#                root.filename.close()

def exit():
    message = messagebox.askquestion('NotePad', 'Do you want to save changes')
    if message == "yes":
        save_as()
    else:
        root.destory()

def cut():
    text.event_generate("<<Cup>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    message = messagebox.askqustion('NotePad', "Do you want to Delete all")
    if messsage == "yes":
        text.delete('1.0', 'end')
    else:
        return "break"

def select_all():
    text.tag_add('sel',
    '1.0', 'end')
    return 'break'

def time():
    t = datetime.now()
    text.insert('end', d)



def new_window():
    root = tk.Tk()
    root.geometry('500x500')
    menubar = Menu(root)
    file = Menu(menubar, tearoff = 0)
    file.add_command(label="New", command=New)
    file.add_command(label="New Window", command=new_window)
    file.add_command(label="Open", command=open)
    #file.add_command(label="Save", command=save)
    #file.add_command(label="Save as", command=save_as)
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="file", menu=file, font=('verdana', 10, 'bold'))
    edit = Menu(menubar, tearoff = 0)
    #edit.add_command(label="Undo", command=undo)
    edit.add_separator()
    edit.add_command(label = "Cut", command=cut)
    edit.add_command(label = "Copy", command=copy)
    edit.add_command(label = "Paste", command=paste)
    edit.add_command(label = "Delete", command=delete)
    edit.add_command(label = "Select All",accelerator="Ctrl+A", command=select_all)
    edit.add_command(label = "Time/Date", accelerator="F5", command=time)
    menubar.add_cascade(label="Edit", menu=edit)
    Format = Menu(menubar, tearoff =0)
    Format.add_command(label="Word Wrap")
    #Format.add_command(label="Font....", commant=fonts)
    menubar.add_cascade(label="Format", menu=Format)
    Help = Menu(menubar, tearoff = 0)
    #Help.add_command(label="View Help", command=view_help)
    #Help.add_command(label="Send FeedBack", command=send_feedback)
    Help.add_command(label="About NotePad")
    menubar.add_cascade(label="Help", menu=Help)
    root.config(menu=menubar)
    text = ScrolledText(root, width=1000, height=1000)
    text.place(x=0, y=0)
    root.mainloop()
    
new_window()