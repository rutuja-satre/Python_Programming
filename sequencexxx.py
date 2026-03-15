def CircleArea(Rad,PI=3.14):
    Area=PI*Rad*Rad
    return Area

def main():
    print("Enter radius of circle: ")
    radius=float(input())

    result=CircleArea(radius)
    print("Area of circle: ",result)

if __name__=="__main__":
    main()
