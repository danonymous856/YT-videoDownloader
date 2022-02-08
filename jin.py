import os
import jenny
from jenny import progress_function
from pytube import YouTube
yt= YouTube(input("link:"))

list=(272, 298, 299, 302, 303, 308, 315, 398, 399, 400, 401, 402,330, 331, 332, 333, 334, 335, 336, 337)

for i in range(0, len(list)):
    print(yt.streams.get_by_itag(list[i]))

video = yt.streams.get_by_itag(input("itag :"))

Vide = jenny.main(print("\nENTER THE DIRECTORY for VIDEO : "))


def main(path=f"{Vide}/{video.title}.mp4"):
    for filename in os.listdir(path):
        if (filename.endswith(".mp4")):  # or .avi, .mpeg, whatever.
            os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
        else:
            continue
