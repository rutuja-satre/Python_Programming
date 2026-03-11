# to delete 

import time
import sys
import os
import hashlib   #to check checksum
import schedule

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path ,'rb')  

    hobj = hashlib.md5()       
    buffer = fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

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

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           fname = os.path.join(FolderName,fname)
           checksum = CalculateChecksum(fname)
           print("File name : ",fname)
           print("Checksum : ",checksum)
           print()

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)   #show timestamp in filename
    filename = filename.replace(" ","_")   #replace space by underscore
    filename = filename.replace(":","_") 

    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a directory cleaner Script\n")

    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("Tis is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n") 

def FindDuplicate(DirectoryName = "Marvellous"):

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

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
               Duplicate[checksum].append(fname)        
            else:
               Duplicate[checksum] = [fname]
    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x: len(x)>1, MyDict.values()))

    Count = 0
    for value in Result:
        for subvalue in value:
            Count = Count+1
            print(subvalue)

        print("---------------------------")
        print("Value of count is : ",Count)
        print("---------------------------")

        Count = 0
def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x: len(x)>1, MyDict.values()))

    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count+1
            if (Count > 1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                cnt = cnt+1
        Count = 0

    print("Total deleted file : ",cnt)

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
            #Result = FindDuplicate(sys.argv[1])
            #DeleteDuplicate(Result)

            schedule.every(1).minute.do(DeleteDuplicate)
            while True:
                schedule.run_pending()
                time.sleep(1)

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