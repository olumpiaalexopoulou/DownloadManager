from __future__ import unicode_literals
from pytube import YouTube
import pafy


def AudioDownloader(url):

    # Me me tin methodo new kai thn getbestaudio katebazoume thn kalhterh poothta ixoy apo to YouTube
    pafy.new(url).getbestaudio().download()


print("Welcome to our download manager!!!")
AudioDownloader(url=input("Please enter the url:"))
