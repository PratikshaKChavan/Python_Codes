def DisplayFactors(No):
    if No < 0:
        No = -No
        
    for i in range(1,int(No/2)+ 1,1):      # TypeCasting
        if No % i == 0:
            print(i)
            
def main():
    Value = 0

    print("Enter the number: ")
    Value = int(input())

    DisplayFactors(Value)


if __name__ == "__main__":
    main()