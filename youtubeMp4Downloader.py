from pytube import YouTube
import os

def downloader(videourl,path):
    youtube = YouTube(videourl)
    youtube = youtube.streams.filter(progressive=True, file_extension= 'mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
        youtube.download(path)
    else:
        print("path available")
downloader("https://youtu.be/o4cOlrnSErk?si=3zFCpkQ9kNHzhHDs","youtubedownloader")
