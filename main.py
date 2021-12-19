from imageio.plugins import ffmpeg
from pytube import YouTube
from pytube.cli import on_progress

yt=YouTube(input("enter the LInk:"))

"""THIS PART IS FOR THE audio PURPOSE"""
for i in yt.streams.filter(type="audio"):
    print(i)

print("Please Enter The Audio ITAG:")
audio=yt.streams.get_by_itag(input())
print('Downloading Audio......')
APath = "C:\DSA Bootcamp\Aud"
print(f"\nDownloading {audio.title}")
audio.download(APath)
print("Audio Downloaded ")
print(audio.get_file_path(None,None,None))


"""THIS PART IS FOR THE video PURPOSE"""

ls=(None,"140p","240p","360p","480p","720p","1080p","1440p","2160p")
for i in range(1,9):
    print(yt.streams.filter(res=ls[i]))


print(yt.streams.filter(progressive=False,type='video'))
print("Please Enter The Video ITAG:")
video=yt.streams.get_by_itag(input())
print('Downloading Video......')
Vpath = "C:\DSA Bootcamp\Vid"
print(f"\nDownloading {video.title}")
print(video.filesize)
video.download(Vpath)
print("Video Downloaded")
print(video.get_file_path(None,None,None))


# input_video = ffmpeg.input('./test/test_video.webm')
#https://youtu.be/BFW2JvTJfFIhttps://youtu.be/BFW2JvTJfFI
# input_audio = ffmpeg.input('./test/test_audio.webm')
#
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()

# Merging code giving some error due to which we have to work with ffmpeg on the terminal
# just to right click ffmpeg(.exe) inside "C:\Users\Donald\Desktop\YT-VID\ffmpeg\bin\"
# and type "ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4"