def CalculatePercentage(Total,Obtained):
    output=((Obtained/Total)*100)
    return output

def main():
    print("Enter total no: ")
    value1=int(input())

    print("Enter obtained no: ")
    value2=int(input())

    result= CalculatePercentage(Obtained=value2,Total=value1) #keyword argument
    print("Percentage is : ",result)
    
    if __name__=="__main__":
        main() 