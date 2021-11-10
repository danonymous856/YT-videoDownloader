from pytube import YouTube

print("enter the link :")

yt = YouTube(input())


def sepVid_Aud():
    print("Going to download the audio and video seperately:")
    print(yt.streams.filter(type='audio'))
    print("Enter the itag for audio:")
    audio = yt.streams.get_by_itag(input())
    print('Downloading Audio......')
    APath = "F:\DSA Bootcamp\Aud/"

    audio_filename = audio.title
    print(audio_filename)
    audio.download(APath)
    print("Audio Downloaded \n\n")

    print(yt.streams.filter(progressive=False, type='video'))
    print('Enter the itag:')
    video = yt.streams.get_by_itag(input())
    print('Downloading Video......')
    Vpath = "F:\DSA Bootcamp\Vid/"
    video_filename = video.title
    print(video_filename)
    print(video.filesize)
    video.download(Vpath)
    print("Video Downloaded")
    pass


def Vid():
    print("Going to download the whole video:")
    print(yt.streams.filter(progressive=True, type='video'))
    print('Enter the  new itag:')
    video = yt.streams.get_by_itag(input())
    print('Downloading Video......')
    Vpath = "F:\DSA Bootcamp\Vid/"
    print(video.title)
    print(video.filesize)
    video.download(Vpath)
    print("Video Downloaded")
    pass

def main():
    print(yt.streams.filter())
    print('Enter the itag:')
    itag = input()
    vid= yt.streams.get_by_itag(itag)

    yourNeed = (vid.filesize > 300000000)

    if yourNeed:
        sepVid_Aud()
    elif yourNeed & (vid.resolution > '480p') :
        vid()
    else:
        Vid()

print(main())