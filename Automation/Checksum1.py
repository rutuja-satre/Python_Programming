import os
import hashlib   #to check checksum

def main():
    print("Enter file name : ")
    filename = input()

    fobj = open(filename,'rb')  #rb = reading binary mode

    hobj = hashlib.md5()        #md5 = class

    buffer = fobj.read(1024)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    print("Checksum of file is : ",hobj.hexdigest())

if __name__=="__main__":
    main()
