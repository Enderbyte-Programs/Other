#Youtube Downloader GUI
import tkinter as tk
from tkinter import messagebox
import sys
import pytube
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from traceback import format_tb
import os

def toplevelerror(message,title='Error'):
    title = str(title)
    message = str(message)
    root = tk.Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showerror(title,message)

def handle_exception(type,value,traceback):

    if issubclass(type, KeyboardInterrupt):
        pass
    else:
        
        toplevelerror('A fatal exception occured. ERROR:\n'+str(type)+'\n'+str(value)+'\n'+str(format_tb(traceback)[0]))
        
        sys.exit()

sys.excepthook = handle_exception

def download_video():
    global ent
    if os.system('ping youtube.com -n 1') == 0:
        try:
            yt = pytube.YouTube(ent.get())
            yt.check_availability()
        except:
            tk.Tk().withdraw()
            messagebox.showerror('Error','Invalid Video URL!')
        else:
            x = yt.streams.get_highest_resolution()
            files = [('mp4 video',"*.mp4")]
            p = asksaveasfile(filetypes = files, defaultextension = files,title='Please choose save file')
            if p == None:
                pass
            else:
                
                x.download(filename=str(p.name))
                file_size = os.path.getsize(p.name)
                tk.Tk().withdraw()
                messagebox.showinfo('Info','Finished downloading video '+str(yt.watch_url)+' to\n'+str(p.name)+'\nfilesize: '+str(file_size)+'Bytes')

def download_audio():
    global ent
    if os.system('ping youtube.com -n 1') == 0:
        try:
            yt = pytube.YouTube(ent.get())
            yt.check_availability()
        except:
            tk.Tk().withdraw()
            messagebox.showerror('Error','Invalid Video URL!')
        else:
            x = yt.streams.get_audio_only()
            files = [('mp3 audio',"*.mp3")]
            p = asksaveasfile(filetypes = files, defaultextension = files,title='Please choose save file')
            if p == None:
                pass
            else:
                
                x.download(filename=str(p.name))
                file_size = os.path.getsize(p.name)
                tk.Tk().withdraw()
                messagebox.showinfo('Info','Finished downloading audio for video'+str(yt.watch_url)+' to\n'+str(p.name)+'\nfilesize: '+str(file_size)+'Bytes')
                
    else:
        tk.Tk().withdraw()
        messagebox.showerror('Error','Could not connect to Youtube. Check your internet connection?')

root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('400x150')
style = ttk.Style(root)
style.theme_use('vista')
lbl = ttk.Label(root,text='Please input the full URL to the video you want to download here.')
lbl.pack()
ent = ttk.Entry(root,width=50)
ent.pack()
btn0 = ttk.Button(root,text='Download Video',command=download_video)
btn0.pack()
btn2 = ttk.Button(root,text='Download Audio',command=download_audio)
btn2.pack()
btn1 = ttk.Button(root,text='Exit',command=sys.exit)
btn1.pack()
root.mainloop()