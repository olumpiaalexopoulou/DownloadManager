from __future__ import unicode_literals
from pytube import YouTube
import youtube_dl
import pafy
from pydub import AudioSegment


#print("Audio or Video?")
#choice = input()
print("Insert the link:")
link = input()

#DOWNLOAD_FOLDER = '/home/nick/Downloads'


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

# if choice == '1':
#    # .mp3 section
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        ydl.download([link])
# else:
# .mp4 section
video = pafy.new(link)
song_name = video.title
audio = video.getbestaudio()
#stream = video.streams.get_highest_resolution()
song_name.replace("m4a", "mp3")
audio.download()


#m4a_audio = AudioSegment.from_file(song_name, format="m4a")
#m4a_audio.export(song_name, format="mp3")

s = open(song_name, "w")

#print("The name of the song is", ydl)
