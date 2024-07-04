import os
import time
tempfiledirectory=[r"C:\Windows\Temp", r"C:\Users\mg15d\AppData\Local\Temp" ]
#basic function to traverse the directories provided and delete the files of the given directories
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



def main(tempfiledirectory):
    #puts the program to sleep for another two days
    time.sleep(172800)
    #prompts the user after two days if they want to delete the files
    while True:
        choice=input("It's been two days since the temperorary files were last deleted, Delete files again? Yes/No ")
        if choice.lower()=="yes":
            deleter(tempfiledirectory)
            main()
        elif choice.lower()=="no":
            main()
        else:
            print("Invalid input, please try again")
        
#Runs the program vroom vroom :p
if __name__=="__main__":
    deleter(tempfiledirectory)
    main(tempfiledirectory)
