import pytube
from pytube import YouTube

print("Please enter the link : ")
yt=YouTube(input())

print("Actually you can choose with itag for which video you prefer the most :")

itag=(None,"160","133","18","135","22","299","400","401")
for i in range(1,len(itag)-1):
    print(i,itag[i],sep=":")

class HighResolution(object):
    def __init__(self,itag):
        self.itag=itag

    def Path(self,path_audio,path_video):
        print("Select the Directory :")
        self.path_audio=input()
        self.path_video=input()

    def Quality(self,quality):
        print("Regarding quality of the video : MP4 > WebM \n")
        self.quality=(None,"140p","240p","360p","480p","720p","1080p","1440p","2160p")

        for i in range(1,9):
            print(i,quality[i],sep=";")

        for i in {17,18,22,137,248,399,136,247,398,135,244,397,134,243,396,133,242,395,160,278,394}:
            print(yt.streams.get_by_itag(i))

        vid=yt.streams.get_by_itag(input())
        return vid

    def size(self):
        print("size of the video is in bytes",self.bytes,sep=":")
        self.bytes=bytes

    def AudDownload(self,path):
        print(yt.streams.filter(type='audio'))
        print("Enter the itag for audio:")
        audio = yt.streams.get_by_itag(input())
        audio.download(path)
        print('Downloading Audio......')
        print(audio.title)
        print("Audio Downloaded \n\n")
        pass

    def VidDownload(self,path,itag=input()):
        print(yt.streams.filter(progressive=False,type='video'))
        print('Enter the itag for video : ', itag)
        video = yt.streams.get_by_itag(itag)
        print('Downloading Video......')
        video.download(path)
        print(video.title)
        print(video.filesize)
        print("Video Downloaded\n")
        # print(audiopath,audio.title,'.mp4')
        pass

    def sepVid_Aud(self, audiopath,videopath):
        print("Enter the audio Directory:")
        self.AudDownload(audiopath)
        print("Enter the video Directory:")
        self.VidDownload(videopath)
        pass

    def Download(self):
        self.Path()
        vid = yt.streams.get_by_itag(self.Quality())
        if (vid.is_progressive) :
            try:
                ls=(None,"140p","240p","360p","480p","720p","1080p","1440p","2160p")
                for i in range(1,9):
                    print(yt.streams.filter(res=ls[i],mime_type="video/mp4",end="\n"))
            except:
                ls=(None,"140p","240p","360p","480p","720p","1080p","1440p","2160p")
                for j in range(1,9):
                    print(yt.streams.filter(mime_type="video/webm",res=ls[j]),end="\n")
                    print("NONE means not present")
        else:
            try:
                self.sepVid_Aud(input(),self.Path(self.path_audio),self.Path(self.path_video))
            except:
                print("Try another way.")
#             here is an exception as if progressive is False
    pass

class LowResolution(HighResolution):
    def __init__(self,type):
        super().__init__()
        self.type="video"
        print("These Low Resolution Class Has been created for only Downloading videos between 140p - 720p .\n","As mostly these are peogressively True no merging would be required .")


down=HighResolution(itag[i])
down.Download()

