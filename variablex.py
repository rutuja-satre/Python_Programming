def Display(*A):
    print(type(A))
    print("Inside the display: ",A)

def main():
    Display(11)
    Display()

if __name__=="__main__":
    main()