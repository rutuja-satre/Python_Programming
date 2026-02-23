def CalculatePercentage(obtained,total=500):
    output=((obtained/total)*100)
    return output

def main():

    print("Enter obtained no: ")
    value2=int(input())

    result= CalculatePercentage(value2) #default argument
    print("Percentage is : ",result)
    
    if __name__=="__main__":
        main()