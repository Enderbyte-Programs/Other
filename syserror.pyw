from tkinter import Tk
from tkinter import messagebox
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
    Tk().withdraw()
    messagebox.showerror('Error','Error '+str(random.randint(1,255))+' at file C:\\Windows\\System32\\'+random.choice(y))