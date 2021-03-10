from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from SearchSong import GetSongUrl
from FileMover import moveSongs
from GetSongFromTXT import *
from GetPath import *


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")

    dm = input(
        "Please select download method:\n[1] Download via search\n[2] Download via link\n[3] Download via songlist\nEnter method number:")

    # Getting the user's choise
    choice = input(
        "PLease select file format\n[1] .mp3\n[2] .m4a\n[3] .mp4\nEnter your prefered format number:")
    if dm == "1":
        songname = input("Enter the song's name:")
        url = GetSongUrl(songname)
    elif dm == "2":
        url = input("Enter the video's url:")
    else:
        url = SongList()

    if (choice == "1") or (choice == "2"):
        AudioDownloader(url)
    else:
        VideoDownloader(url)

    # Getting current directory and destination directory to move the song
    sourcePath = getsrcPath()
    destinationPath = getdstPath()

    moveSongs(sourcePath, destinationPath, choice)
    print("Your file is at:", destinationPath)
