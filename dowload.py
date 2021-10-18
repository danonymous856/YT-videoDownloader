from  pytube import YouTube

print("Enter the link:")
link=input()

yt=YouTube(link)

#for audio
print(yt.streams.filter(type='audio'))
audio=yt.streams.get_by_itag(input())  #Recommended 139
print('Downloading Audio.....')
APATH ="E:\Bootcamp\Aud/"    #to_do for audio
audio_filename=audio.title
print(audio_filename)
audio.download(APATH)
print("Audio Downloaded")

# for video
print(yt.streams.filter(progressive=False,type='video'))
print('Enter the itag:')
video=yt.streams.get_by_itag(input())
print('Downloading Video.....')
VPATH = 'E:\Bootcamp\Vid/'     #to_do for video
video_filename=video.title
print(video_filename)
video.download(VPATH)
print("Video Downloaded")


# Merging code giving some error due to which we have to work with ffmpeg on the terminal
# just to right click ffmpeg(.exe) inside "C:\Users\____\Desktop\YT-VID\ffmpeg\bin\"
# and type "ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4"
