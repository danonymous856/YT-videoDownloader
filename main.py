from imageio.plugins import ffmpeg
from pytube import YouTube
from pytube.cli import on_progress

print("enter the LInk:")

yt=YouTube(input())

print(yt.streams.filter(type='audio'))
audio=yt.streams.get_by_itag(input())
print('Downloading Audio......')
APath = "F:\DSA Bootcamp\Aud/"

audio_filename=audio.title
print(audio_filename)
audio.download(APath)
print("Audio Downloaded \n\n")

print(yt.streams.filter(progressive=False,type='video'))
print('Enter the itag:')
video=yt.streams.get_by_itag(input())
print('Downloading Video......')
Vpath = "F:\DSA Bootcamp\Vid/"
print(video.title)
print(video.filesize)
video.download(Vpath)
print("Video Downloaded")


# input_video = ffmpeg.input('./test/test_video.webm')
#https://youtu.be/BFW2JvTJfFIhttps://youtu.be/BFW2JvTJfFI
# input_audio = ffmpeg.input('./test/test_audio.webm')
#
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()

# Merging code giving some error due to which we have to work with ffmpeg on the terminal
# just to right click ffmpeg(.exe) inside "C:\Users\Donald\Desktop\YT-VID\ffmpeg\bin\"
# and type "ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4"