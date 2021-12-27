import os
from tkinter import filedialog

ftypes = [
    ("jar executables","*.jar")
]
print("please select the file to run")
m = filedialog.askopenfilename(filetypes=ftypes)
print("=====")
os.system(f"java -jar {m}")

print("=====")
input("Finished. Press enter to close program.")