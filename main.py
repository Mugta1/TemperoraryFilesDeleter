import os
import time
time=time.time()
def deleter():
    tempfiledirectory=[r"C:\Windows\Temp", r"C:\Users\mg15d\AppData\Local\Temp" ]

    for hehe in tempfiledirectory:
        if os.path.isdir(hehe):
            for path, subdir, files in os.walk(hehe):
                for file in files:
                    x=os.path.join(path, file)
                try:
                    os.remove(x)
                except:
                    continue
while True:
    time2=time.time()
    x=time-time2
    if x >=172800:
        choice=input("It's been two days since the temperorary files were last deleted, Delete files again? Yes/No ")
        if choice.lower()=="yes":
            deleter()

