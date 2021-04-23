from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from GetPath import getsrcPath, getdstPath
from GetSongFromTXT import SongList
from SearchSong import GetSongUrl
from FileMover import moveSongs
from message import display


# Main program function
def download_files(download_method, video_type, user_input):

    url = []  # initialize the url list

    sourcePath = getsrcPath()  # initialize program directory

    if download_method == "1":
        # Getting the video's url via the GetSongUrl function
        songname = user_input
        url.append(GetSongUrl(songname))

    elif download_method == "2":

        url.append(user_input)

    else:
        # Loading songs from the .txt file
        url = (SongList(user_input))
        sourcePath = user_input

    # Asking where to save the files
    destinationPath = getdstPath()

    if (video_type == "mp3") or (video_type == "m4a"):
        AudioDownloader(url)

    else:
        VideoDownloader(url)

    # Moving files to "save" directory
    moveSongs(sourcePath, destinationPath, video_type)

    # Display "save" directory
    display(destinationPath)
