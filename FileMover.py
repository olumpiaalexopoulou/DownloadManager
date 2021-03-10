import os
import shutil
#from Rename_Song import remove_unwanted_letters


def moveSongs(source, destination, choice):
    os.chdir(source)  # Allazei to directory se ayto pou briskonte ta arxeia
    content = os.listdir()  # Deixnei ola ta arxeia sto current directory
    for file in content:

        # Psaxnei gia mp4 arxeia kai ta metaferei se neo directory
        if file.endswith('.mp4'):
            oldfile = file
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)

        # Psaxnei gia arxeia ixou, ta metaonomazei otan einai aparaitito kai ta metaferei se neo directory
        if (file.endswith('.m4a')) or (file.endswith('.webm') or (file.endswith('.3gp'))):
            oldfile = file
            if (choice == "1"):
                file = os.path.splitext(file)[0] + ".mp3"
            if (choice == "2"):
                file = os.path.splitext(file)[0]+".m4a"
            src = os.path.join(source, oldfile)
            dst = os.path.join(destination, file)
            shutil.move(src, dst)
