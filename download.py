from pytube import YouTube, StreamQuery

print("Enter the Link:")
link=input()
yt=YouTube(link)
# print(yt.streams.filter())
def sepVid_Aud(itag, audiopath=input(), videopath=input()):
    print("Going to download the audio and video seperately:")
    print(yt.streams.filter(type='audio'))
    print("Enter the itag for audio:")
    audio = yt.streams.get_by_itag(input())

    print("Verify the path at which you want to save/Copy the Path here :")
    audio.download(audiopath)
    print('Downloading Audio......')
    audio_filename = audio.title
    print(audio_filename)
    print("Audio Downloaded \n\n")

    print(yt.streams.filter(progressive=False, type='video'))
    print('Enter the itag for video : ',itag)
    video = yt.streams.get_by_itag(itag)
    print("Verify the path at which you want to save/Copy the Path :")
    print('Downloading Video......')
    video.download(videopath)
    print(video.title)
    print(video.filesize)
    print("Video Downloaded\n")
    # print(audiopath,audio.title,'.mp4')
    pass
def Vid(itag):
    print("Going to download the whole video:")
    print(yt.streams.filter(progressive=True, type='video'))
    print('Enter the  new itag:')
    video = yt.streams.get_by_itag(itag)
    print("Verify the path at which you want to save/Copy the Path:\n")
    video.download(input())
    print(video.title)
    print(video.filesize)
    print('Downloading Video......')
    print("Video Downloaded")
    pass
def main():
    print(yt.streams.filter())

    print('Enter the itag:')
    itag = input()

    vid= yt.streams.get_by_itag(itag)
    resolut_n=vid.resolution

    if (resolut_n >= '1080p'):
        print("Please enter the PAth directory separately for audio and video respectively:")
        print("AUdio directory:")
        aud = input()
        print("Video directory:")
        Vide = input()
        sepVid_Aud(itag,audiopath=aud,videopath=Vide)
    else:
        Vid(itag)
    pass
print(main())







