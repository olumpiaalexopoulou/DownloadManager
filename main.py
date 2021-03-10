from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from SearchSong import GetSongUrl
from FileMover import moveSongs
from GetSongFromTXT import *
from GetPath import *


# Main program function
if __name__ == '__main__':

    print("Welcome to OcEAN's desktop youtube downloader!!!")

    # dm = download method,menu sto opoio o xristis apofasizei ton tropo me ton opoio yhelei na katebasei ta arxeia tou
    dm = input(
        "Please select download method:\n[1] Download via search\n[2] Download via link\n[3] Download via songlist\nEnter method number:")

    # Menu poy o xristis epilegei ton tipo arxeioy pou thelei
    choice = input(
        "PLease select file format\n[1] .mp3\n[2] .m4a\n[3] .mp4\nEnter the number of your prefered file format:")

    if dm == "1":
        # O xristis briskei to tragoudi pou thelei basei titlou kai sthn synexeia kaleitai i sinartisi GetSongUrl gia na brethei
        # to link tou epilegmenoy tragoydiou
        songname = input("Enter the song's name:")
        url = GetSongUrl(songname)

    elif dm == "2":
        # O xristis bazei kateutheian to link apo to tragoudi poy epithimei na katebasei
        url = input("Enter the video's url:")

    else:
        # To programma fortonei automata ta tragoudia apo thn playlist poy exei ftiaksei o idios o xristis
        url = SongList()

    if (choice == "1") or (choice == "2"):
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia ixou
        AudioDownloader(url)

    else:
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia video
        VideoDownloader(url)

    # Oi dio parakato sinartisis einai upethines gia ta directories tis efarmogis
    sourcePath = getsrcPath()
    destinationPath = getdstPath()

    # Metafora ton arxeion sto katallilo directory
    moveSongs(sourcePath, destinationPath, choice)
    # Emfanizei sto xristi se poion fakelo briskontai ta arxeia tou
    print("Your file is at:", destinationPath)
