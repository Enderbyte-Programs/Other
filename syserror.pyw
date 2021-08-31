from tkinter import Tk, messagebox
import random
from os import scandir
from time import sleep
x = scandir('C:\\Windows\\System32')
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