from imageio.plugins import ffmpeg
from pytube import YouTube

print("enter the LInk:")
link=input()

yt=YouTube(link)

print(yt.streams.filter(type='audio'))
audio=yt.streams.get_by_itag(input())
print('Downloading Audio......')
APath = "C:\DSA Bootcamp\Aud/"

audio_filename=audio.title
print(audio_filename)
audio.download(APath)
print("Audio Downloaded \n\n")

print(yt.streams.filter(progressive=False,type='video'))
print('Enter the itag:')
video=yt.streams.get_by_itag(input())
print('Downloading Video......')
Vpath = "C:\DSA Bootcamp\Vid/"
video_filename=video.title
print(video_filename)
print(video.filesize)
print(video.on_progress())
video.download(Vpath)
print("Video Downloaded")


# input_video = ffmpeg.input('./test/test_video.webm')
#
# input_audio = ffmpeg.input('./test/test_audio.webm')
#
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()

# Merging code giving some error due to which we have to work with ffmpeg on the terminal
# just to right click ffmpeg(.exe) inside "C:\Users\Donald\Desktop\YT-VID\ffmpeg\bin\"
# and type "ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4"7