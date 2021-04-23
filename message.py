from tkinter import messagebox
from tkinter import Tk

message = Tk()
message.eval('tk::PlaceWindow %s center' % message.winfo_toplevel())
# message.iconbitmap(r"wave.ico")
message.withdraw()


def display(destinationPath):
    messagebox.showinfo('Friendly Remainder',
                        "Your file is at: " + destinationPath)


def TitleError():
    messagebox.showinfo('Friendly Remainder', "Please enter a title")


def LinkError():
    messagebox.showinfo('Friendly Remainder', "Please enter a link")


def FileError():
    messagebox.showinfo('Friendly Remainder', "Please use a .txt file")


def FileEmptyError():
    messagebox.showinfo('Friendly Remainder', "This file is empty")
