from SearchSong import GetSongUrl
from pathlib import Path
import os


def SongList(user_input):
    # Getting the urls from the txt file provided by the user
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
