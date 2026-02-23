import Arithmatic
def Multiplication(value1,value2):
    result=value1*value2
    return result


def main():
    print("Enter first no: ")
    no1=int(input())

    print("Enter second no: ")
    no2=int(input())

    ans=Arithmatic.Multiplication(no1,no2)
    print("Multiplication is: ",ans)

if __name__=="__main__":
    main()
