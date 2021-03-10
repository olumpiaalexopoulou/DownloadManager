from pytube import YouTube


def VideoDownloader(url):

    for u in url:

        url = YouTube(u)
        mp4 = url.streams.first()
        mp4.download()
