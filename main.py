import os
import time
time=time.time()
def deleter():
    tempfiledirectory=["C:\Windows\Temp", "C:\Users\mg15d\AppData\Local\Temp" ]

    for hehe in tempfiledirectory:
        if os.path.isdir(hehe):
            for path, subdir, files in os.walk(hehe):
                try:
                    os.remove(file in files)
                except:
                    continue
while True:
    time2=time.time()
    x=time-time2
    if x >=172800:
        choice=input("It's been two days since the temperorary files were last deleted, Delete files again? Yes/No ")
        if choice.lower()=="yes":
            deleter()

