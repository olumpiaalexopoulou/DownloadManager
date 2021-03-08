import os
import shutil
from Rename_Song import remove_unwanted_letters


def moveSongs(source, destination):
    os.chdir(source)
    content = os.listdir()  # list all files in current directory
    for file in content:

        # Searching for the .mp3 file, renaming it and moving it to the new directory
        if file.endswith('.mp3'):
            oldfile = file
            file = remove_unwanted_letters(file)
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)

        # Searching for the .m4a file then moving it to the new directory
        if (file.endswith('.m4a')) or (file.endswith('.mp4')):
            oldfile = file
            file = os.path.splitext(file)[0]+".mp3"
            #file.replace('.m4a', '.mp3')
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)
