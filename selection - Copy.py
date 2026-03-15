def main():
    print("Enter your age: ")
    age=int(input())
    
    if(age<18):
        print("You can't participate in voting")
    else:
        print("You can participate in voting")

if __name__=="__main__":
    main()
    