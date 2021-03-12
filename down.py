from __future__ import unicode_literals
from DownloadAudio import AudioDownloader
from DownloadVideo import VideoDownloader
from GetPath import getsrcPath,getdstPath
from GetSongFromTXT import SongList
from SearchSong import GetSongUrl
from FileMover import moveSongs




# Main program function
def down(dm,video_type,user_input):

    url = []  # initialize url list

    sourcePath = getsrcPath()  # kanei initialize to directory tis efarmogis

    # dm = download method,menu sto opoio o xristis apofasizei ton tropo me ton opoio yhelei na katebasei ta arxeia tou
    #dm = input(
    #    "Please select download method:\n[1] Download via search\n[2] Download via link\n[3] Download via songlist\nEnter method number:")

    # Menu poy o xristis epilegei ton tipo arxeioy pou thelei
    #video_type = input(
    #    "PLease select file format\n[1] .mp3\n[2] .m4a\n[3] .mp4\nEnter the number of your prefered file format:")

    if dm == "1":
        # O xristis briskei to tragoudi pou thelei basei titlou kai sthn synexeia kaleitai i sinartisi GetSongUrl gia na brethei
        # to link tou epilegmenoy tragoydiou
        songname = user_input  #input("Enter the song's name:")
        url.append(GetSongUrl(songname))

    elif dm == "2":
        # O xristis bazei kateutheian to link apo to tragoudi poy epithimei na katebasei
        url.append(user_input)

    else:
        # To programma fortonei automata ta tragoudia apo thn playlist poy exei ftiaksei o idios o xristis
        url = (SongList())

    print("Where do you want to save your file?")
    # rotaei ton xristi gia to directory pou thelei na apothikeusei to arxeio
    destinationPath = getdstPath()
    #print(destinationPath, " is selected as download directory")

    if (video_type == "1") or (video_type == "2"):
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia ixou
        AudioDownloader(url)

    else:
        # Kaleitai i sinartisi me to url gia na kateboun ta arxeia video
        VideoDownloader(url)

    # Metafora ton arxeion sto katallilo directory
    moveSongs(sourcePath, destinationPath, video_type)
    # Emfanizei sto xristi se poion fakelo briskontai ta arxeia tou
    print("Your file is at:", destinationPath)
