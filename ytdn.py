import subprocess
import pytube
import glob
import sys
import os
from awesome_progress_bar import ProgressBar
import random

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

_dlv = True
if _dlv:# Only downloading when conditional. Downloading takes over an hour.
    c = pytube.Channel("https://www.youtube.com/c/TheHorizonMC")
    inc = 0
    bar = ProgressBar(len(c.video_urls)*2,prefix="Downloading",suffix="Preparing",bar_length=200,spinner_type="s")
    for video in c.video_urls:
        bar.iter()
        try:
            y = pytube.YouTube(video)
            bar.suffix = y.title
            bar.iter()
            st = y.streams.get_highest_resolution()
            st.download(filename=f"vid_{inc}.mp4")
        except:
            bar.iter()
            try:
                os.remove(f"vid_{inc}.mp4")
            except:
                pass
            continue
        inc += 1
    bar.wait()
    bar.stop()
_exv = True
if _exv:
    g = glob.glob("*.mp4")
    bar = ProgressBar(int(len(g)*2),prefix="Extracting",suffix="Preparing",bar_length=200,spinner_type="s")
    for v in g:
        bar.iter()
        _len = int(get_length(v) // 1)# Rounding down
        if _len > 2:
            slt = random.randint(0,_len)
            bar.suffix = str(v)
            rmn = subprocess.run(["ffmpeg","-ss",str(slt),"-i",os.getcwd()+"/"+v,"-t","1",os.getcwd()+"/"+v.split(".")[0]+"s.mp4"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            bar.iter()
            rmn2 = subprocess.run(["ffmpeg","-i",os.getcwd()+"/"+v.split(".")[0]+"s.mp4","-filter_complex","[0:v]pad=1280:720:-1:-1,fps=30000/1001[v];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a]","-map","[a]","-map","[v]",os.getcwd()+"/"+v.split(".")[0]+"x.mp4"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        else:
            bar.iter()

    bar.wait()
    bar.stop()

#Removing empty files to prevent glitvhes
fls = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f))]
for file in fls:
    if os.path.getsize(file) == 0:
        try:
            os.remove(file)
        except:
            print("Failed to remove corrupt file")

lg = glob.glob("*x.mp4")#Filtering split videos only
data = ""
for vid in lg:
    data += "file '"
    data += os.getcwd()
    data += "/"
    data += vid
    data += "'\n"
with open("mylist.txt","w+") as f:
    f.write(data)

rmn2 = subprocess.run(["ffmpeg","-f","concat","-safe","0","-i","mylist.txt","output.mp4"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
