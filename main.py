import os
import time
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
                        print(f"{file} not deleted")



deleter()
def main():
    time=time.sleep(172800)
    choice=input("It's been two days since the temperorary files were last deleted, Delete files again? Yes/No ")
    if choice.lower()=="yes":
        deleter()
    else:
        main()
        
    

main()
