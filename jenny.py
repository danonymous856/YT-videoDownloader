from tkinter import Tk, filedialog

def  main(path):

    root = Tk()  # pointing root to Tk() to use it as Tk() in program.
    root.withdraw()  # Hides small tkinter window.
    ''
    root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
    ''
    open_file = filedialog.askdirectory()  # Returns opened path as str
    return open_file

def progress_function(self,stream, chunk,file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print (str)(p)+'%'
        p = percent(bytes_remaining, size)

def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc



