#program to check size of file

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
    print("Enter the input of directory that you want to travel : ")
    Dirname = input()

    DirectoryWatcher(Dirname)

if __name__=="__main__":
    main()