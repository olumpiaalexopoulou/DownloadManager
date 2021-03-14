from tkinter import Frame, Tk, Entry, Button, NONE, filedialog, messagebox, StringVar, OptionMenu, ttk
from BackMain import download_files
from pathlib import Path
import os

root = Tk()
root.geometry('400x240')
root.resizable(0, 0)
root.title("Download Manager")


def SearchWindow():
    w = Frame(root, width=400, height=240, bg='#044f64')
    w.place(x=0, y=28)

    # entrybox
    
    def searchbar():
        search = s.get()
        return search

    def filetypebar():
        ch = n.get()
        return ch

    
    n=StringVar()
    options = ttk.Combobox(w, width = 10, textvariable = n)
    options["values"]=(
    "mp3",
    "m4a",
    "mp4")
    
    options.current()
    options.place(x=150, y=92)

    s = Entry(w, width=30, fg="grey")
    s.place(x=100, y=42)

    Button(w, width=20, height=0, text="Download", command=lambda:download_files('1',filetypebar(),searchbar()),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=142)


def LinkWindow():
    q = Frame(root, width=400, height=240, bg='#077190')
    q.place(x=0, y=28)

    
    l = Entry(q, width=30, fg="grey")
    l.place(x=100, y=42)
    l.place(x=100, y=42)

    def searchbar():
        search = l.get()
        return search

    def filetypebar():
        ch = n.get()
        return ch

    n = StringVar()
    options = ttk.Combobox(q, width=10, textvariable=n)

    options["values"] = (
        "mp3",
        "m4a",
        "mp4")
    options.current()
    options.place(x=150, y=92)

    Button(q, width=20, height=0, text="Download", command=lambda:download_files('1',filetypebar(),searchbar()),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=142)


def CustomPlaylist():
    c = Frame(root, width=400, height=240, bg='#519bb1')
    c.place(x=0, y=28)

    def openfile():
        c.songlist = filedialog.askopenfilename()
        p = Path(c.songlist)
        c.directory = p.parent
        return c.directory

    def filetypebar():
        ch = n.get()
        return ch

    n = StringVar()
    options = ttk.Combobox(c, width=10, textvariable=n)

    options["values"] = (
        "mp3",
        "m4a",
        "mp4")
    options.current()
    options.place(x=150, y=92)

    Button(c,width=20,height=0,text="Select File",command=lambda:openfile(),border=0,bg='#ffffff',fg='#000000').place(x=120,y=42)
    Button(c, width=20, height=0, text="Download", command=lambda:download_files('3',filetypebar(),c.directory),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=142)


LinkWindow()
CustomPlaylist()
SearchWindow()


Button(root, width=19, height=0, text="Search", command=SearchWindow, border=0, bg='#044f64', pady=4,
       fg='#ffffff', activebackground='#044f64', activeforeground='#003F87').place(x=0, y=0)


Button(root, width=19, height=0, text="Link", command=LinkWindow, border=0, bg='#077190',pady=4,
       fg='#ffffff', activebackground='#077190', activeforeground='#ffffff').place(x=133, y=0)


Button(root, width=19, height=0, text="Playlist", command=CustomPlaylist, border=0, bg='#519bb1',pady=4,
       fg='#ffffff', activebackground='#519bb1', activeforeground='#ffffff').place(x=266, y=0)


root.mainloop()
