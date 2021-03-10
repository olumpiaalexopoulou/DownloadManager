def SongList(filepath='/home/nick/VS Code/Python/DownloadManager/DownloadManager/songlist.txt'):
    with open(filepath) as f:
        data = f.readlines()
    return data
