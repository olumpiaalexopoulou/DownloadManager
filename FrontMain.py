from tkinter import Frame,Tk, Entry,Button,NONE,filedialog,messagebox
from BackMain import down
from pathlib import Path
import os

root = Tk()
root.geometry('400x240')
root.resizable(0, 0)
root.title("Download manager")



def SearchWindow():
    w = Frame(root, width=400, height=240, bg='#003F87')
    w.place(x=0, y=28)

    # entrybox
    '''
    def on_entry(e):
        s.delete(0, 'end')

    def on_leave(e):
        if s.get() == "":
            s.insert(0, "Search Song")
    '''

    def searchbar():
        search=s.get()
        return search

    def filetypebar():
        ch=o.get()
        return ch

    def calldown(dm,video_type,user_input):
        down(dm,video_type,user_input)
        




    s = Entry(w, width=30, fg="grey")
    #s.configure(font=("Consolas", 5, "bold"))
    #s.bind("<FocusIn>", on_entry)
    #s.bind("<FocusIn>", on_leave)
    #s.insert(0, "Search Song")
    s.place(x=100, y=42)
    

    # entry box for options
    o = Entry(w, width=30, fg="black")
    o.place(x=100, y=92)

    Button(w, width=20, height=0, text="Download", command=lambda:calldown('1',filetypebar(),searchbar()),
           border=0, bg='light blue', fg='white').place(x=120, y=142)



def LinkWindow():
    q = Frame(root, width=400, height=240, bg='purple')
    q.place(x=0, y=28)

    # entrybox
    '''
    def on_entry(e):
        l.delete(0, 'end')

    def on_leave(e):
        if l.get() == "":
            l.insert(0, "Search Song")
    '''

    l = Entry(q, width=30, fg="grey")
    '''
    l.configure(font=("Consolas", 10, "bold"))
    l.bind("<FocusIn>", on_entry)
    l.bind("<FocusIn>", on_leave)
    l.insert(0, "Search Song")
    '''
    l.place(x=100, y=42)

    

    def searchbar():
        search=l.get()
        return search

    def filetypebar():
        ch=o1.get()
        return ch

    def calldown(dm,video_type,user_input):
        down(dm,video_type,user_input)

    # entry box for options
    o1 = Entry(q, width=30, fg="black")
    o1.place(x=100, y=92)

    Button(q, width=20, height=0, text="Download", command=lambda:calldown('1',filetypebar(),searchbar()),
           border=0, bg='light blue', fg='white').place(x=120, y=142)


def CustomPlaylist():
    c = Frame(root, width=400, height=240, bg='red')
    c.place(x=0, y=28)

    # entrybox
    '''
    def on_entry(e):
        cp.delete(0, 'end')

    def on_leave(e):
        if cp.get() == "":
            cp.insert(0, "Search Song")
    '''
    #cp = Entry(c, width=30, fg="grey")
    '''
    cp.configure(font=("Consolas", 10, "bold"))
    cp.bind("<FocusIn>", on_entry)
    cp.bind("<FocusIn>", on_leave)
    cp.insert(0, "Search Song")
    '''
    #cp.place(x=100, y=42)
    
    def openfile():
        c.songlist=filedialog.askopenfilename()
        p=Path(c.songlist)
        c.directory=p.parent
        return c.directory
        


    def filetypebar():
        ch=o2.get()
        return ch

    def calldown(dm,video_type,user_input):
        down(dm,video_type,user_input)

    # entry box for options
    o2 = Entry(c, width=30, fg="black")
    o2.place(x=100, y=92)

    Button(c,width=20,height=0,text="Select File",command=lambda:openfile(),border=0,bg='orange',fg='white').place(x=100,y=42)
    Button(c, width=20, height=0, text="Download", command=lambda:calldown('3',filetypebar(),c.directory),
           border=0, bg='light blue', fg='white').place(x=120, y=142)


LinkWindow()
CustomPlaylist()
SearchWindow()



Button(root, width=19, height=0, text="Search", command=SearchWindow, border=0, bg='#003F87', pady=4,
       fg='white', activebackground='#003F87', activeforeground='#003F87').place(x=0, y=0)


Button(root, width=19, height=0, text="Link", command=LinkWindow, border=0, bg='purple',pady=4,
       fg='white', activebackground='purple', activeforeground='white').place(x=133, y=0)


Button(root, width=19, height=0, text="Playlist", command=CustomPlaylist, border=0, bg='red',pady=4,
       fg='white', activebackground='red', activeforeground='white').place(x=266, y=0)


root.mainloop()
