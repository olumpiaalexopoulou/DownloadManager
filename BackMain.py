from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from GetPath import getsrcPath, getdstPath
from GetSongFromTXT import SongList
from SearchSong import GetSongUrl
from FileMover import moveSongs


# Main program function
def download_files(download_method, video_type, user_input):

    url = []  # initialize url list

    sourcePath = getsrcPath()  # kanei initialize to directory tis efarmogis

    if download_method == "1":
        # O xristis briskei to tragoudi pou thelei basei titlou kai sthn synexeia kaleitai i sinartisi GetSongUrl() gia na brethei
        # to link tou epilegmenoy tragoydiou
        songname = user_input  # input("Enter the song's name:")
        url.append(GetSongUrl(songname))

    elif download_method == "2":
        # O xristis bazei kateutheian to link apo to tragoudi poy epithimei na katebasei
        url.append(user_input)

    else:
        # To programma fortonei automata ta tragoudia apo thn playlist poy exei ftiaksei o idios o xristis
        url = (SongList(user_input))
        sourcePath = user_input

    # rotaei ton xristi gia to directory pou thelei na apothikeusei to arxeio
    destinationPath = getdstPath()

    if (video_type == "mp3") or (video_type == "m4a"):
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia ixou
        AudioDownloader(url)

    else:
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia video
        VideoDownloader(url)

    # Metafora ton arxeion sto katallilo directory
    moveSongs(sourcePath, destinationPath, video_type)
    # Emfanizei sto xristi se poion fakelo briskontai ta arxeia tou
    print("Your file is at:", destinationPath)
