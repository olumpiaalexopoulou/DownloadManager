from tkinter import Frame, Tk, Entry, Button, filedialog, messagebox, StringVar, ttk
from BackMain import download_files
from pathlib import Path

root = Tk()
root.geometry('400x240')
root.iconbitmap(r"Icon/wave.ico")
root.resizable(0, 0)
root.title("Download Manager")


def SearchWindow():
    w = Frame(root, width=400, height=240, bg='#57deff')
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
    q = Frame(root, width=400, height=240, bg='#52c2ff')
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
    c = Frame(root, width=400, height=240, bg='#4da6ff')
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


Button(root, width=19, height=0, text="Search", command=SearchWindow, border=0, bg='#57deff', pady=4,
       fg='#ffffff', activebackground='#57deff', activeforeground='#003F87').place(x=0, y=0)


Button(root, width=19, height=0, text="Link", command=LinkWindow, border=0, bg='#52c2ff',pady=4,
       fg='#ffffff', activebackground='#52c2ff', activeforeground='#ffffff').place(x=133, y=0)


Button(root, width=19, height=0, text="Playlist", command=CustomPlaylist, border=0, bg='#4da6ff',pady=4,
       fg='#ffffff', activebackground='#4da6ff', activeforeground='#ffffff').place(x=266, y=0)


root.mainloop()
