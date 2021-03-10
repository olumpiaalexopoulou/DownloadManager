import os
from pathlib import Path


def getsrcPath():
    # Returning the current directory
    return os.getcwd()


def getdstPath():
    # Returning the destination directory
    return str(Path.home()/"Downloads")
