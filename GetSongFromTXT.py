from SearchSong import GetSongUrl
from pathlib import Path
import os


def SongList(user_input):
    # Psaxnei mesa sto current directory gia to arxeio txt, to diabazei
    # kai stin sinexeia kalei tin GetURLS i opoia epistrefei ta urls ton video
    os.chdir(user_input)
    content = os.listdir()
    print(content)
    
    for file in content:
        if file.endswith(".txt"):
            with open(file) as f:
                songs = f.readlines()
                urls = GetURLS(songs)
            return urls
    


def GetURLS(songlist):
    urls = [GetSongUrl(song) for song in songlist]
    return urls
