from pytube import YouTube
from sys import argv
from pytube import Playlist

link = argv[1]
pls = Playlist(link)
path = 'E:\ytd'
a = 0
for i in pls.video_urls:
    yt = YouTube(f'"{i}"')
    print(f"Views: {yt.views}")
    print(f"Title: {yt.title}")
    print(f"Total videos: {len(pls.video_urls)}")
    yd =yt.streams.get_highest_resolution()
    yd.download(f"{path}\{pls.title}")
    a+= 1
    print(f"{a} out of {len(pls.video_urls)} Completed...")

    
#|/\/\/\/\| Made By Raj |\/\/\/\/|#













# print("views :" + str(yt.views))
# print("Title: " + Name)

# ytd = yt.streams.get_highest_resolution()

# ytd.download(path)
# print(f"Video Downloded\nLink: {link}")

