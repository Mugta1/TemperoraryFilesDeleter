import os
import time
tempfiledirectory=[r"C:\Windows\Temp", r"C:\Users\mg15d\AppData\Local\Temp" ]
def deleter(listofpath):
    

    for hehe in listofpath:
        if os.path.isdir(hehe):
            for path, subdir, files in os.walk(hehe):
                for file in files:
                    x=os.path.join(path, file)
                    try:
                        os.remove(x)
                    except:
                        print(f"{file} not deleted")



deleter(tempfiledirectory)
def main(tempfiledirectory):
    time.sleep(172800)
    choice=input("It's been two days since the temperorary files were last deleted, Delete files again? Yes/No ")
    if choice.lower()=="yes":
        deleter(tempfiledirectory)
    else:
        main()
        
    

main(tempfiledirectory)
