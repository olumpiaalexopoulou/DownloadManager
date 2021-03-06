from __future__ import unicode_literals
from Downloadmp3 import mp3Downloader
from Downloadm4a import m4aDownloader
from Move_Song import moveSongs
from pathlib import Path
import time
import os


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")
    time.sleep(2)
    url = 'https://www.youtube.com/watch?v=2UKTSEUL5kQ'
    #url = input("Enter the video url:")

    # Getting the user's choise
    choice = input("Choose .mp3 or .m4a [1] or [2]:")

    if choice == "1":
        mp3Downloader(url)
    else:
        m4aDownloader(url)

    # Getting curent directory and future directory to move the song
    sourcePath = os.getcwd()
    destinationPath = str(Path.home() / "Downloads")

    moveSongs(sourcePath, destinationPath)
    print("Your file is at:", destinationPath)
