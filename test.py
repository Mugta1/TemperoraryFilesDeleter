import os

tempfiledirectory=["C:\Windows\Temp", "C:\Users\mg15d\AppData\Local\Temp" ]

for hehe in tempfiledirectory:
    if os.path.isdir(hehe):
        for path, subdir, files in os.walk(hehe):
            try:
                os.remove(file in files)
            except:
                continue