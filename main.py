import os
import time
time=time.time()
while True:
    time2=time.time()
    for time-time2==

tempfiledirectory=["C:\Windows\Temp", "C:\Users\mg15d\AppData\Local\Temp"]

for directory in tempfiledirectory:
    if os.path.isdir(directory):
        for path, subdir, files in os.walk(direcotry):
            try:
                os.remove(file in files)
            except:
                continue