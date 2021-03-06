import os
import shutil
from File_Renamer import remove_unwanted_letters


def moveSongs(source, destination):
    os.chdir(source)
    content = os.listdir()
    for file in content:
        if file.endswith('.mp3'):
            oldfile = file
            file = remove_unwanted_letters(file)
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)
