from __future__ import unicode_literals
from File_Mover import moveSongs
from mp3Download import mp3Download
import os
from pathlib import Path


if __name__ == '__main__':

    url = 'https://www.youtube.com/watch?v=2UKTSEUL5kQ'
    #url = input("Enter the video url:")
    mp3Download(url)

    sourcePath = os.getcwd()
    destinationPath = str(Path.home() / "Downloads")

    moveSongs(sourcePath, destinationPath)
