import pafy


def AudioDownloader(url):
    # Using a loop in case there are more than one urls
    for u in url:
        pafy.new(u).getbestaudio().download()
