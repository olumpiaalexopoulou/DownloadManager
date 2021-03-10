import pafy


def AudioDownloader(url):

    # calling the 'new' method of pafy and downloading the best audio quality song
    for u in url:
        result = pafy.new(u).getbestaudio().download()
