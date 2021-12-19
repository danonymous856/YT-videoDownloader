import os
import tkinter as tk
from tkinter import Tk,filedialog
from PySimpleGUI import FolderBrowse
import ffmpeg
import PySimpleGUI as sg
from pytube import YouTube

path = "C:\Users\Donald\Videos\Jujutsu.mp4"


for filename in os.listdir(path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    else:
        continue
