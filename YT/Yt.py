from pytube import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)
Name = yt.title
path = 'E:\ytd'

print("views :" + str(yt.views))
print("Title: " + Name)

ytd = yt.streams.get_highest_resolution()

ytd.download(path)
print(f"Video Downloded\nLink: {link}")

