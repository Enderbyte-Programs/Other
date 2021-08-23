# I hope for this to be compiled into .pyc
'''
list of exit codes:
0: Proper stop via closing window or using exit button
1: Failed to write data
2: Could not open data file
3: Could not read data file
'''
import os
import sys
from tkinter import messagebox
from tkinter import *
import datetime
cwd = os.getcwd()
def log(stuff_to_log):
    f = open('credits.log','a+')
    f.write('['+str(datetime.datetime.now())+'] '+str(stuff_to_log)+'\n')
    f.close()
def error(error):
    Tk().withdraw()
    messagebox.showerror('Credits',error)
try:
    log('Program started')
except:
    error('Could not write log file')
    sys.exit()
ads = os.path.isfile('credata.dat')
if ads == False:
    
    log('could not find data file, will make new one')
    try:
        f = open('credata.dat','w+')
        f.write(str(0))
        f.close()
    except:
        log('Could not write data file')
        error('Could not write data')
        log('Process crashed with exit code 1')
        sys.exit()
def addOne():
    global lbl
    global data
    data += 1
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Added 1 credit')
def addTen():
    global lbl
    global data
    data += 10
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Added 10 credits')
def addHundred():
    global lbl
    global data
    data += 100
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Added 100 credits')
def remOne():
    global lbl
    global data
    data -= 1
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Removed 1 credit')

def remTen():
    global lbl
    global data
    data -= 10
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Removed 10 credits')

def remHundred():
    global lbl
    global data
    data -= 100
    try:
        f = open('credata.dat','w+')
        f.write(str(data))
        f.close()
    except:
        log('Could not write credits to data file')
        error('could not write data file')
    else:
        lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
        log('Removed 100 credits')

def clrall():
    m = messagebox.askyesno('Credits','Are you sure you want to remove all credits?')
    if m == True:
        global lbl
        global data
        data = 0
        try:
            f = open('credata.dat','w+')
            f.write(str(data))
            f.close()
        except:
            log('Could not write credits to data file')
            error('could not write data file')
        else:
            lbl.configure(text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
            log('Removed all credits')
        

def clrdat():
    m = messagebox.askyesno('Credits','Are you sure you want to clear all data?')
    if m == True:
        try:
            os.remove('credata.dat')
            os.remove('credits.log')
        except:
            a = 0
        log('Cleared all data')
        messagebox.showinfo('Credits','Data clear complete. Will now restart')
        sys.exit()

root = Tk()
root.title('Credits')
root.geometry('700x150')
try:
    f = open('credata.dat')
except:
    log('Could not open data file')
    error('Could not read data')
    log('Process crashed with exit code 2')
    sys.exit()
else:
    try:
        data = int(f.read())
    except:
        log('Error: Data file contains unreadable data')
        error('Error when reading data file')
        log('Process crashed with exit code 3')
        sys.exit()
    else:
        f.close()
        log('Data file read sucessfully')
lbl = Label(root,text='You have '+str(data)+' Credits.',font=('Helvetica','18','bold'))
lbl.pack()
btn = Button(root,text='Exit',command=root.destroy,bg='red')
btn.pack(side=TOP)
btn2 = Button(root,text='Add 1 Credit',bg='lime green',command=addOne)
btn2.pack(side=LEFT)
btn3 = Button(root,text='Add 10 Credits',bg='lime green',command=addTen)
btn3.pack(side=LEFT)
btn4 = Button(root,text='Add 100 Credits',bg='lime green',command=addHundred)
btn4.pack(side=LEFT)
btn5 = Button(root,text='Remove 1 Credit',bg='yellow',command=remOne)
btn5.pack(side=RIGHT)
btn6 = Button(root,text='Remove 10 Credits',bg='yellow',command=remTen)
btn6.pack(side=RIGHT)
btn7 = Button(root,text='Remove 100 Credits',bg='yellow',command=remHundred)
btn7.pack(side=RIGHT)
btn8 = Button(root,text='Remove All',bg='red',command=clrall)
btn8.pack(side=BOTTOM)
btn9 = Button(root,text='Clear All Data',bg='red',command=clrdat)
btn9.pack(side=BOTTOM)

root.mainloop()
log('Process ended with exit code 0')
sys.exit()