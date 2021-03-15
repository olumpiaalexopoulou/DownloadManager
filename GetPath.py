from tkinter import filedialog
from pathlib import Path
import os



def getsrcPath():
    # Epistrefei to current directoy
    return os.getcwd()


def getdstPath():
    # Epistrefei to teliko directory
    #save_directory = str(Path.home()/"Downloads")
    save_directory = filedialog.askdirectory()
    return save_directory
