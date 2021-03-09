import youtube_dl


def mp3Downloader(url):
    # Setting the format options for the song
    ydl_opts = {

    }
    # A function to download the .mp3 file
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


'''
    'format': 'bestaudio/best',
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '320',
    }],
'''
