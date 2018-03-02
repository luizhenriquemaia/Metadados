import os
from mutagen.easyid3 import EasyID3

folderD = "C:/Users/User/Documents/Python/Download Youtube/Downloads"

def main():
    listFil = os.listdir(folderD)
    listShow = []

    for i in range(len(listFil)):
        listShow.append("{} - {}".format(str(i), listFil[i]))
        print(listShow[i])

    selFil = input("Select the File: ")
    selFil = listFil[int(selFil)]
    print(selFil)
    setMetD(selFil)
    return

def setMetD(file):
    song = input("Enter the Name of Song: ")
    artist = input("Enter the Artist: ")
    album = input("Enter the Name of Album: ")
    newFil = EasyID3("{}/{}".format(folderD, file))
    newFil["title"] = song
    newFil["artist"] = artist
    newFil["album"] = album
    newFil.save()
    os.rename("{}/{}".format(folderD, file),
              "{}/{} - {}.mp3".format(folderD, artist, song))
    return 
    
while True:
    main()
