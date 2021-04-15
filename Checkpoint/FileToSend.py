from __future__ import unicode_literals
from tkinter import Tk, Entry, Button, Frame, ttk
import pafy
import urllib.request
import urllib.parse
import re

# Building main window
root = Tk()
root.geometry("400x240")
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())  # Centering main window
# Changing icon from tkinter default feather icon
root.iconbitmap(r"Checkpoint/wave.ico")
root.title("Download Manager")
root.resizable(0, 0)  # Can't resize main window

options = ["mp3", "m4a", "mp4"]  # file supported formats

def AudioDownloader(url):

    # By using the <<new>> and <<getbestaudio>> methonds from pafy
    # we can download the best audio quality directly from youtube
    pafy.new(url).getbestaudio().download()

def GetSongUrl(songname):
    
    # Changes spaces with underscore
    search_keyword = songname.replace(" ", "_")

    # Concatinating Youtube link with search_keyword
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)
    
    # Looking for the best match video
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    # Concatinating the Youtube link with the id of the first video in order  
    url = "https://www.youtube.com/watch?v=" + video_ids[0]

    return url

def LinkWindow():
    # Building main window frame
    f = Frame(root, width=400, height=240, bg='#52c2ff')
    f.place(x=0, y=28)

    def on_enter(e):
        # Text disappears when search-bar is clicked
        l.delete(0, 'end')

    def on_leave(e):
        # Text reappears when clicking elsewhere
        if l.get() == '':
            l.insert(0, 'Enter song url...')

    def searchbar():
        # Gets url from search-bar and returns it
        return l.get()
    
    def filetypebar():
        # Creating the select file button
        ch = optionsbox.get()
        return ch
    
    #Building optionsbox   
    optionsbox = ttk.Combobox(f, width=10, value=options)
    optionsbox.current(0)
    optionsbox.place(x=150, y=92)

    # Building search-bar
    l = Entry(f, width=30, fg="#686868")
    l.bind("<FocusIn>", on_enter)
    l.bind("<FocusOut>", on_leave)
    l.insert(0, 'Enter song url...')
    l.place(x=100, y=40)

    Button(f, width=20, height=0, text="Download", command=lambda: AudioDownloader(searchbar()),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=135)
    # We're using lambda to hold the execution of Audiodownloader before call

def SearchWindow():
    w = Frame(root, width=400, height=240, bg='#57deff')
    w.place(x=0, y=28)

    # entrybox
    def on_enter(e):
        s.delete(0, 'end')

    def on_leave(e):
        if s.get() == '':
            s.insert(0, 'Please enter song name...')

    def searchbar():
        search = rep(s.get())
        return search

    def filetypebar():
        ch = optionsbox.get()
        return ch

    optionsbox = ttk.Combobox(w, width=10, value=options)
    optionsbox.current(0)
    optionsbox.place(x=150, y=92)

    s = Entry(w, width=30, fg="grey")
    s.bind("<FocusIn>", on_enter)
    s.bind("<FocusOut>", on_leave)
    s.insert(0, 'Please enter song name...')
    s.place(x=100, y=42)

    Button(w, width=20, height=0, text="Download", command=lambda: download_files('1', filetypebar(), searchbar()),
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
        ch = optionsbox.get()
        return ch

    optionsbox = ttk.Combobox(c, width=10, value=options)
    optionsbox.current(0)
    optionsbox.place(x=150, y=92)

    Button(c, width=20, height=0, text="Select File", command=lambda: openfile(),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=42)
    Button(c, width=20, height=0, text="Download", command=lambda: download_files('3', filetypebar(), c.directory),
           border=0, bg='#ffffff', fg='#000000').place(x=120, y=142)

LinkWindow()
SearchWindow()
CustomPlaylist()

Button(root, width=19, height=0, text="Link", command=LinkWindow, border=0, bg='#52c2ff', pady=4,
       fg='#ffffff', activebackground='#52c2ff', activeforeground='#ffffff').place(x=133, y=0)

Button(root, width=19, height=0, text="Search", command=SearchWindow, border=0, bg='#57deff', pady=4,
       fg='#ffffff', activebackground='#57deff', activeforeground='#ffffff').place(x=0, y=0)

Button(root, width=19, height=0, text="Playlist", command=CustomPlaylist, border=0, bg='#4da6ff', pady=4,
       fg='#ffffff', activebackground='#4da6ff', activeforeground='#ffffff').place(x=266, y=0)

# Keeps root window running
root.mainloop()
