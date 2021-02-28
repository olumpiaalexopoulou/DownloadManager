from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=2UKTSEUL5kQ')
stream = video.streams.get_highest_resolution()
stream.download()
