def CountFactors(No):
    iCount = 0

    if No < 0:
        No = -No
        
    for i in range(1,int(No/2)+ 1,1):      # TypeCasting
        if No % i == 0:
            iCount = iCount + 1
    
    return iCount

def main():
    Value = 0
    iRet = 0

    print("Enter the number: ")
    Value = int(input())

    iRet = CountFactors(Value)

    print("Number of factors are : ",iRet)


if __name__ == "__main__":
    main()