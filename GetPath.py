import os
from pathlib import Path
from tkinter import filedialog


def getsrcPath():
    # Epistrefei to current directoy
    return os.getcwd()


def getdstPath():
    # Epistrefei to teliko directory
    # return str(Path.home()/"Downloads")
    save_directory = filedialog.askdirectory()
    return save_directory
