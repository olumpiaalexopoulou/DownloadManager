from pytube import YouTube


def VideoDownloader(url):

    url = YouTube(url)
    mp4 = url.streams.first()
    mp4.download()
