'''
#import youtube_dl
#from pytube import YouTube


def mp3Downloader(url):
    # Setting the format options for the song
    
   # ydl_opts = {

    #}
    # A function to download the .mp3 file
    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     #   ydl.download([url])
    
    #audio = YouTube(url)
    #audio = audio.get_best_audio()
    # audio.download()



    'format': 'bestaudio/best',
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '320',
    }],

'''
