from tkinter import Tk
from tkinter import messagebox

message=Tk()
message.eval('tk::PlaceWindow %s center' % message.winfo_toplevel())
message.iconbitmap(r"Icon/wave.ico")
message.withdraw()

def display(destinationPath):
    messagebox.showinfo('Friendly Remainder',"Your file is at: " + destinationPath)
