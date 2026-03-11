# take input from user

import os

def DirectoryWatcher(DirectoryName):
    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub Folder Name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)

def main():
    print("Enter the input of directory that you want to travel : ")
    Dirname = input()

    DirectoryWatcher(Dirname)

if __name__=="__main__":
    main()