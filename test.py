import os

tempfiledirectory=[r"C:\Windows\Temp", r"C:\Users\mg15d\AppData\Local\Temp" ]

for hehe in tempfiledirectory:
    if os.path.isdir(hehe):
        for path, subdir, files in os.walk(hehe):
            for file in files:
                x=os.path.join(path, file)
                try:
                    os.remove(x)
                except:
                    print(f"not deleted {file}")
