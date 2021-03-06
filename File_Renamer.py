import re


def remove_unwanted_letters(filename):
    pattern = re.compile(r'''(
        (\S*)
        (\.mp3)
    )''', re.VERBOSE)
    matchObj = pattern.search(filename)

    if matchObj:
        toReplace = matchObj.group(2)
        filename = filename.replace(toReplace, '')
    return filename
