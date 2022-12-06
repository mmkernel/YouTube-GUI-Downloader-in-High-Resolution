import io
import tkinter
from pytube import YouTube
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen


def download():
    yt = YouTube(link.get())
    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()
    # Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")

def info():
    # Showing details
    yt = YouTube(link.get())
    Label(text="Title: " + yt.title).place(x=10,y=70)
    Label(text="Views: " + str('{:,}'.format(yt.views))).place(x=10,y=90)
    if yt.length//60 < 59:
        Label(text="Length: " + str(yt.length//60)+"m "+str(yt.length%60)+"s").place(x=10,y=110)
    else: Label(text="Length: " + str(yt.length//60//60)+"h "+str(yt.length//60%60)+"m "+str(yt.length%60)+"s").place(x=10,y=110)
    Label(text="Rating: " + str(yt.rating)).place(x=10,y=130)
    url = yt.thumbnail_url
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    im = Image.open(io.BytesIO(raw_data))
    resized_img = im.resize((130,80))
    photo = ImageTk.PhotoImage(resized_img)
    thumb = tkinter.Label(image=photo, width=130)
    thumb.image = photo
    thumb.place(x=10,y=150)

    #Label(text="Thumbnail", image=thumb_final).place(x=10,y=150)
    print("Rating of video: ", yt.rating)

def clear():
    link.delete(0,END)

def close():
   #window.destroy()
   window.quit()

window = Tk()
window.geometry("645x235")

window.title("mmkernel.com YouTube Downloader")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

label = Label(text="YouTube Link: ")
label.grid(row=0, column=0, sticky=N)

link = Entry(window,font=('Arial',22), width=40 )
link.grid(row=1, column=0, sticky=E)

# Buttons
clear = Button(window, text='X', command=clear, padx=15, height=2)
clear.grid(row=1, column=0, sticky=E)

download = Button(window, text='Download Video', command=download, padx=15, width=25, height=5)
download.grid(row=3, column=0, sticky=E)

info = Button(window, text='Get Info', command=info, padx=15, width=25, height=5)
info.grid(row=2, column=0, sticky=E)

window.mainloop()
