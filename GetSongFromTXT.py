from SearchSong import *
import os
from pathlib import Path


def SongList():
    content = os.listdir()
    for file in content:
        if file.endswith(".txt"):
            with open(file) as f:
                songs = f.readlines()
                urls = GetURLS(songs)
            return urls


def GetURLS(songlist):
    urls = [GetSongUrl(song) for song in songlist]
    return urls


#urls = SongList()
#songs = list(map(lambda song: song.replace("\n", " "), songs))
# print(songs)
#urls = GetURLS(songs)
# print(urls)
