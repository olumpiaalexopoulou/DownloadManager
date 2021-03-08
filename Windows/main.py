from __future__ import unicode_literals
import pafy
from pathlib import Path
import youtube_dl
from pytube import YouTube
import os
import shutil
import re


def getsrcPath():
    # Returning the current directory
    return os.getcwd()


def getdstPath():
    # Returning the destination directory
    return str(Path.home()/"Downloads")


def mp3Downloader(url):
    # Setting the format options for the song
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    # A function to download the .mp3 file
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def m4aDownloader(url):

    # calling the 'new' method of pafy and downloading the best audio quality song
    pafy.new(url).getbestaudio().download()


def mp4Downloader(url):

    url = YouTube(url)
    mp4 = url.streams.first()
    mp4.download()
    print("Your video is ready")

def moveSongs(source, destination):
    os.chdir(source)
    content = os.listdir()  # list all files in current directory
    for file in content:

        # Searching for the .mp3 file, renaming it and moving it to the new directory
        if file.endswith('.mp3'):
            oldfile = file
            file = remove_unwanted_letters(file)
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)

        # Searching for the .m4a file thenn moving it to the new directory
        if (file.endswith('.m4a')) or (file.endswith('.mp4')):
            oldfile = file
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)


def remove_unwanted_letters(filename):

    # Searching for the wrong letters at the end of the .mp3 file
    pattern = re.compile(r'''(
        (\S*)
        (\.mp3)
    )''', re.VERBOSE)
    matchObj = pattern.search(filename)

    # Removing the wrong letters from the end of the .mp3 file
    if matchObj:
        toReplace = matchObj.group(2)
        filename = filename.replace(toReplace, '')
    return filename


# Main program function
if __name__ == '__main__':

    print("Welcome!!!")
    # time.sleep(1)

    #url = input("Enter the video url:")

    # Getting the user's choise
    choice = input("Choose .mp3, .m4a or .mp4 [1] or [2] or [3]:")
    url = 'https://www.youtube.com/watch?v=2UKTSEUL5kQ'

    if choice == "1":
        mp3Downloader(url)
    elif choice == "2":
        m4aDownloader(url)
    else:
        mp4Downloader(url)

    # Getting curent directory and future directory to move the song
    sourcePath = getsrcPath()
    destinationPath = getdstPath()

    moveSongs(sourcePath, destinationPath)
    print("Your file is at:", destinationPath)
    exit=input()
