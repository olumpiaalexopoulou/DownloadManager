from __future__ import unicode_literals
from tkinter import Tk, Entry, Button, Frame
import pafy

# Building main window
root = Tk()
root.geometry("400x240")
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.iconbitmap(r"Checkpoint/wave.ico")
root.title("Download Manager")
root.resizable(0, 0)


def AudioDownloader(url):

    # By using the <<new>> and <<getbestaudio>> methonds we can download thw best audio quality directly from youtube
    pafy.new(url).getbestaudio().download()


def LinkWindow():
    # Building main windo frame
    f = Frame(root, width=400, height=240, bg='#52c2ff')
    f.place(x=0, y=0)

    # Building entry box
    e = Entry(f, width=30, fg="grey")
    e.place(x=100, y=42)
    e.place(x=100, y=42)

    def searchbar():
        # Gets text from entry field and returns it
        search = e.get()
        return search

    Button(f, width=20, height=0, text="Download", command=lambda: AudioDownloader(searchbar()),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=142)


LinkWindow()
root.mainloop()
