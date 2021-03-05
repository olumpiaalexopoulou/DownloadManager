from __future__ import unicode_literals
import youtube_dl
import urllib.request
import urllib.parse
import AS_Move_And_Rename_Songs as rename

# url=''


def mp3Download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':

    url = 'https://www.youtube.com/watch?v=2UKTSEUL5kQ'
    #url = input("Enter the video url:")
    mp3Download(url)
    #sourcePath = r'/home/nick/VS Code/Python/Ergasia_Eksaminou/'
    #destinationPath = r'/home/nick/Music/'

    # rename.moveSongs(sourcePath)
