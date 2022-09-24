from pytube import YouTube
url = input("Enter the url: ")
video = YouTube(url)
stream = video.streams("720")
stream.download()

#https://youtu.be/qkTUVOLGeJg