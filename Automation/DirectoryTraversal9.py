#program to check size of file

import sys
import os

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag==False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag==False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but the target is not a directory")
        exit()

    print("Absolute path is : "+DirectoryName)

    TotalCount = 0
    EmptyCount = 0

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            TotalCount = TotalCount+1
            
            if(os.path.getsize(os.path.join(FolderName,fname))==0):
                EmptyCount = EmptyCount+1
                print("File name is : "+fname)
                
                os.remove(os.path.join(FolderName,fname))

    print("Total number of files scanned : ",TotalCount)
    print("Total number of files deleted : ",EmptyCount)


def main():
    #header
    Border = "-"*54
    print(Border)
    print("---------------Marvellous Automation--------------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")

        else:
            DirectoryWatcher(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : used to display the usage")

#footer
    print(Border)
    print("--------------Thank you for using our script--------------")
    print("--------------Marvellous Infosystem---------------------")
    print(Border)

    

if __name__=="__main__":
    main()