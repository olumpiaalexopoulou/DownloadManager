import re


def remove_unwanted_letters(filename):

    # Searching for the wrong letters at the end of the .mp3 file
    pattern = re.compile(r'''(
        (\S*)
        (\.mp3)
    )''', re.VERBOSE)
    matchObj = pattern.search(filename)

    # Removing the wrong letters from the end of the .mp3 file
    if matchObj:
        toReplace = matchObj.group(2)
        filename = filename.replace(toReplace, '')
    return filename
