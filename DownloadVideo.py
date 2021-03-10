from pytube import YouTube


def VideoDownloader(url):
    # Xrisimopoioyme to loop se periptosi poy yparxoun perissotera apo ena video
    # Me me tin methodo streams.first katebazoume thn kalhterh poothta video apo to YouTube
    for u in url:

        url = YouTube(u)
        mp4 = url.streams.first()
        mp4.download()
