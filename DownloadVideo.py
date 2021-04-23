from pytube import YouTube


def VideoDownloader(url):
    # Using a loop in case there are more than one urls
    # Using the streams.first() function to download the best quality mp4
    for u in url:

        url = YouTube(u)
        mp4 = url.streams.first()
        mp4.download()
