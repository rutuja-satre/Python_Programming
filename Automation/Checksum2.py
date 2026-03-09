import os
import hashlib   #to check checksum

def CalculateChecksum(path):
    fobj = open(path,'rb')  #rb = reading binary mode

    hobj = hashlib.md5()        #md5 = class

    buffer = fobj.read(100)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(100)

    fobj.close()

    return hobj.hexdigest()
def main():
    print("Enter file name : ")
    filename = input()

    ret = CalculateChecksum(filename)
    print("CheckSum of file is : ",ret)

    

if __name__=="__main__":
    main()