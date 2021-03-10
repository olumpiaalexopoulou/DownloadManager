import os
from pathlib import Path


def getsrcPath():
    # Epistrefei to current directoy
    return os.getcwd()


def getdstPath():
    # Epistrefei to teliko directory
    return str(Path.home()/"Downloads")
