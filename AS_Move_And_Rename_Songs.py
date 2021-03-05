import re
import os
import shutil


def remove_unwanted_letters(filename):
    pattern = re.compile(r'''(
        (\S*)
        (\.mp3)
    )''', re.VERBOSE)
    matchObj = pattern.search(filename)
    # print(filename)

    if matchObj:
        # print(filename)
        toReplace = matchObj.group(2)
        filename = filename.replace(toReplace, '')
       # print(filename)
    return filename


def moveSongs(source, destination):
    os.chdir(source)
    content = os.listdir()
    # print(content)
    for file in content:
        if file.endswith('.mp3'):
            oldfile = file
            # print("found")
            file = remove_unwanted_letters(file)
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)


if __name__ == '__main__':

    sourcePath = r'/home/nick/VS Code/Python/Ergasia_Eksaminou/'
    destinationPath = r'/home/nick/Music/'

    moveSongs(sourcePath, destinationPath)
