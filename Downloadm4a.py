import pafy


def m4aDownloader(url):

    # calling the 'new' method of pafy and downloading the best audio quality song
    result = pafy.new(url).getbestaudio().download()
