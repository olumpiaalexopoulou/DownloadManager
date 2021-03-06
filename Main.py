from __future__ import unicode_literals
from Downloadmp3 import mp3Downloader
from Downloadm4a import m4aDownloader
from Move_Song import moveSongs
from getPath import *
import time


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")
    # time.sleep(1)

    #url = input("Enter the video url:")

    # Getting the user's choise
    choice = input("Choose .mp3 or .m4a [1] or [2]:")
    url = 'https://www.youtube.com/watch?v=2UKTSEUL5kQ'

    if choice == "1":
        mp3Downloader(url)
    else:
        m4aDownloader(url)

    # Getting curent directory and future directory to move the song
    sourcePath = getsrcPath()
    destinationPath = getdstPAth()

    moveSongs(sourcePath, destinationPath)
    print("Your file is at:", destinationPath)
