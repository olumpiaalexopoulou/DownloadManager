from __future__ import unicode_literals
import urllib.request
import urllib.parse
import re


def GetSongUrl(songname):
    # Allazei ta kena me kato pavles gia na dexetai ton titlo o parakato algorithmos
    search_keyword = songname.replace(" ", "_")

    # Ginetai concatination tou Youtube link me to kathe search_keyword
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)
    # Psaxnei na brei to katallilo video
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # Ginetai ksana concatination tou Youtube link me to id tou protou se seira video
    # sthn selida tou Youtube
    url = "https://www.youtube.com/watch?v=" + video_ids[0]

    return url
