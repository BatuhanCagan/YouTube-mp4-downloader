from pytube import YouTube

link = input("Please paste YouTube link here.\n")

def download(vidUrl):
    url = YouTube(str(vidUrl))
    video = url.streams[1]
    return video.download()

download(link)