from tkinter import *
import threading
import keyboard
from time import sleep

def anim():
    global root
    global lbl
    while True:
        
        root.config(bg="black")
        lbl.config(fg="white",bg="black")
        sleep(0.5)
        root.config(bg="white")
        lbl.config(fg="black",bg="white")
        sleep(0.5)

root = Tk()
root.title("You are an idiot!")
lbl = Label(root,text="You are an idiot!\n☺☺☺",font=("Consolas",48,"bold"))
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.wm_attributes("-topmost",True)
root.attributes("-fullscreen",True)
def d():
    pass
root.protocol('WM_DELETE_WINDOW',d)
root.config(cursor="none")
t = threading.Thread(target=anim)
t.start()
keyboard.add_hotkey('ctrl+alt+shift+q',root.destroy)
root.mainloop()