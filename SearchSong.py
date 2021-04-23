from __future__ import unicode_literals
import urllib.request
import urllib.parse
import re


def GetSongUrl(songname):

    search_keyword = songname.replace(" ", "_")

    # Concatinating the YouTube link with every search_keyword
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)

    # Looking for video based on "html" value
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    # Concatinanting the Youtube link with the link id of the first video in order
    url = "https://www.youtube.com/watch?v=" + video_ids[0]

    return url
