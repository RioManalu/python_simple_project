import tkinter
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

root = Tk()
video_link = StringVar()
root.config(background="#99a4aa")
download_path = StringVar()
resolution = StringVar(root)
resolution.set('144p')

def myfunc():
    link_label = Label(root, text="Youtube Link : ")
    link_label.grid(row=0, column=0, padx=5, pady=5)

    link_text = Entry(root, width=60, border=3, textvariable=video_link)
    link_text.grid(row=0, column=1, padx=5, pady=5)

    destination_label = Label(root, text="Location : ")
    destination_label.grid(row=1, column=0, padx=5, pady=5)

    destination_text = Entry(root, width=60, border=3, textvariable=download_path)
    destination_text.grid(row=1, column=1, padx=5, pady=5)

    browse_button = Button(root, text="Browse", command=browse, border=3)
    browse_button.grid(row=1, column=2, padx=5, pady=5)

    video_button = Button(root, text="Video Download", command=download_video, border=3)
    video_button.grid(row=2, column=1, padx=5, pady=5)

    audio_button = Button(root, text="Audio Download", command=download_audio, border=3)
    audio_button.grid(row=2, column=2, padx=5, pady=5)

    resolution_opt = OptionMenu(root, resolution, "720p", "480p", "360p", "240p", "144p")
    resolution_opt.grid(row=3, column=1, padx=5, pady=5)


def browse():
    download_dir = filedialog.askdirectory(initialdir="Directory Path")
    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()

    yt_video = YouTube(url)
    option = resolution.get()
    print(option)
    print(url)
    get_video = yt_video.streams.filter(res=option).first()

    get_video.download(folder)

    messagebox.showinfo("Success", "Download Successfull")


def download_audio():
    url = video_link.get()
    folder = download_path.get()

    yt_video = YouTube(url)
    get_audio = yt_video.streams.filter(only_audio=True).first()
    out_file = get_audio.download(folder)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


myfunc()
root.mainloop()