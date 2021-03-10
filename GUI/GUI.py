from tkinter import *


root = Tk()
root.geometry('400x240')
root.resizable(0, 0)
root.title('Download Manager')


def Main_Window():
    w = Frame(root, width=400, height=240, bg='#EFAD29')
    w.place(x=0, y=0)

    # link entry box
    link_box = Entry(w, width=35, fg='grey')
    link_box.place(x=55, y=40)
    # Me ton idio tropo tha prosthesoume kai ta txt fields gia tis upoloipew leitourgies

    Button(w, width=12, height=-1, text='Download', command=None, border=0,
           bg='dark red', fg='white').place(x=135, y=146)


Main_Window()

root.mainloop()
