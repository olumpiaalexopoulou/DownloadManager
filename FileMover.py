import os
import shutil
#from Rename_Song import remove_unwanted_letters


def moveSongs(source, destination, choice):
    os.chdir(source)
    content = os.listdir()  # list all files in current directory
    for file in content:

        # Searching for the .mp4 file and moving it to the new directory
        if file.endswith('.mp4'):
            oldfile = file
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)

        # Searching for audio file, converting it and then moving it to the new directory
        if (file.endswith('.m4a')) or (file.endswith('.webm') or (file.endswith('.3gp'))):
            oldfile = file
            if (choice == "1"):
                file = os.path.splitext(file)[0] + ".mp3"
            if (choice == "2"):
                file = os.path.splitext(file)[0]+".m4a"
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)
