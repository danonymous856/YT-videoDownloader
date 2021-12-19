import ffmpeg
from tkinter import Tk,filedialog
from pytube import YouTube, StreamQuery
import jenny
from jenny import progress_function

yt = YouTube(input("Enter the Link:"))
print("it's gonna take a while!","\n Have patience Pls .")


def main():
    print(yt.streams.filter(resolution="4320p\n"))

    ls = (None, "140p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p","4320p")
    for i in range(1, len(ls)-1):
        print(yt.streams.filter(resolution=ls[i]))

    itag = input('Enter the itag:')

    vid= yt.streams.get_by_itag(itag)
    resolut_n=vid.resolution

    if (resolut_n >= '1080p'):
        print("Please enter the PAth directory separately for audio and video respectively:")
        DoYouWntToChooseManually = input('Do you want to choose the directory manually ? [y/n]\n')

        if DoYouWntToChooseManually == "y":
            aud = jenny.main(print("\nENTER THE DIRECTORY for AUDIO : "))

            Vide = jenny.main(print("\nENTER THE DIRECTORY for VIDEO : "))

        elif DoYouWntToChooseManually == "n":
            print("null and void !")

        """sepVid_Aud(itag,audiopath=aud,videopath=Vide)  """

        print("\n Going to download the audio and video seperately:")
        print(yt.streams.filter(type='audio'))
        print("Enter the itag for audio:")
        audio = yt.streams.get_by_itag(input())

        print("Verify the path at which you want to save/Copy the Path here :")
        audio.download(aud)
        print('Downloading Audio......')
        audio_filename = audio.title
        print(audio_filename,"\n")
        print(f"{aud}/{audio.title}.mp4") #this part is for the use in CLI version of the ffmpeg merging operation !!!!!!!!!!!!!!!!!!!!!!
        print("\nAudio Downloaded \n")


        print('Enter the itag for video : ', itag)
        video = yt.streams.get_by_itag(itag)
        print("Verify the path at which you want to save/Copy the Path :")
        print('Downloading Video......')
        video.download(Vide)
        print(video.title)
        print(video.filesize,"\n")
        print(f"{Vide}/{video.title}.mp4")  # this part is for the use in CLI version of the ffmpeg merging operation !!!!!!!!!!!!!!!!!!!!!!
        print("\nVideo Downloaded\n")
        # print(audiopath,audio.title,'.mp4')
    else:
        """ Vid(itag) """
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

call = main()
print(call)

def nothin():
    """
    :Topic: To directly use it in the terminal itself
    :return: ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4"
    """

