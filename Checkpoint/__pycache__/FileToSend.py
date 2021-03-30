from __future__ import unicode_literals
from tkinter import Tk, Entry, Button, Frame
import pafy

# Building main window
root = Tk()
root.geometry("400x240")
root.eval('tk::PlaceWindow %s center' %
          root.winfo_toplevel())  # Centering main window
# Changing icon from tkinter default feather icon
root.iconbitmap(r"Icon/wave.ico")
root.title("Download Manager")
root.resizable(0, 0)  # Can't resize main window


def AudioDownloader(url):

    # By using the <<new>> and <<getbestaudio>> methonds from pafy
    # we can download the best audio quality directly from youtube
    pafy.new(url).getbestaudio().download()


def LinkWindow():
    # Building main window frame
    f = Frame(root, width=400, height=240, bg='#52c2ff')
    f.place(x=0, y=0)

    def on_enter(e):
        # Text disappears when search-bar is clicked
        e1.delete(0, 'end')

    def on_leave(e):
        # Text reappears when clicking elsewhere
        if e1.get() == '':
            e1.insert(0, 'Enter song url...')

    def searchbar():
        # Gets url from search-bar and returns it
        return e1.get()

    # Building search-bar
    e1 = Entry(f, width=30, fg="#686868")
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0, 'Enter song url...')
    e1.place(x=100, y=80)

    Button(f, width=20, height=0, text="Download", command=lambda: AudioDownloader(searchbar()),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=135)
    # We're using lambda to hold the execution of Audiodownloader before call


LinkWindow()

# Keeps root window running
root.mainloop()
