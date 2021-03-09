from __future__ import unicode_literals
from Downloadmp3 import mp3Downloader
from Downloadm4a import m4aDownloader
from Downloadmp4 import mp4Downloader
from File_Mover import moveSongs
from getPath import *
#import time


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")
    # time.sleep(1)

    #url = input("Enter the video url:")

    # Getting the user's choise
    choice = input("Choose .mp3, .m4a or .mp4 [1] or [2] or [3]:")
    url = 'https://www.youtube.com/watch?v=_cKHn_tMukg'  # no copyright song

    if choice == "1":
        mp3Downloader(url)
    elif choice == "2":
        m4aDownloader(url)
    else:
        mp4Downloader(url)

    # Getting curent directory and destination directory to move the song
    sourcePath = getsrcPath()
    destinationPath = getdstPath()

    moveSongs(sourcePath, destinationPath)
    print("Your file is at:", destinationPath)
