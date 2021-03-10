from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from FileMover import moveSongs
from GetPath import *


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")

    #url = input("Enter the video url:")

    # Getting the user's choise
    choice = input("Choose .mp3, .m4a or .mp4 [1] or [2] or [3]:")
    url = 'https://www.youtube.com/watch?v=_cKHn_tMukg'  # no copyright song

    if (choice == "1") or (choice == "2"):
        AudioDownloader(url)
    else:
        VideoDownloader(url)

    # Getting current directory and destination directory to move the song
    sourcePath = getsrcPath()
    destinationPath = getdstPath()

    moveSongs(sourcePath, destinationPath, choice)
    print("Your file is at:", destinationPath)
