from tkinter import filedialog
from pathlib import Path
import os


def getsrcPath():
    # Returns current directoy
    return os.getcwd()


def getdstPath():
    # Returns "save" directory
    save_directory = filedialog.askdirectory()
    return save_directory
