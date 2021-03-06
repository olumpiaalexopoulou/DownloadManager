import pafy
# url of the video
url = "https://www.youtube.com/watch?v=cr3-J5wDLsM"
# calling the new method of pafy
result = pafy.new(url)
# getting the best quality of video from the 'result' using the getbest()
best_quality_audio = result.getbestaudio()
# you can print it to see the quality of the video
print(best_quality_audio)
# download it using the download()
song = best_quality_audio.download()
