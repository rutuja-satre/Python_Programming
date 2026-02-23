def CalculatePercentage(Total,Obtained):
    output=((Obtained/Total)*100)
    return output

def main():
    print("Enter total no: ")
    value1=int(input())

    print("Enter obtained no: ")
    value2=int(input())

    result= CalculatePercentage(value1,value2) # positional arguments
    print("Percentage is : ",result)
    
    if __name__=="__main__":
        main()