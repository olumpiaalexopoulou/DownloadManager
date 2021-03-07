from pytube import YouTube


def mp4Downloader(url):

    url = YouTube(url)
    mp4 = url.streams.first()
    mp4.download()
    print("Your video is ready")
