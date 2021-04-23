import shutil
import os


def moveSongs(source, destination, choice):
    os.chdir(source)  # Cahing to current direcotry
    content = os.listdir()  # Listign all files in current directory
    for file in content:

        # Looking for audio/video files and tranfers them to new directory
        if file.endswith('.mp4'):
            oldfile = file
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)

        if (file.endswith('.m4a')) or (file.endswith('.webm') or (file.endswith('.3gp'))):
            oldfile = file
            if (choice == "mp3"):
                file = os.path.splitext(file)[0] + ".mp3"
            if (choice == "m4a"):
                file = os.path.splitext(file)[0]+".m4a"
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)
