def CountNonFactors(No):
    iCount = 0

    if No < 0:
        No = -No
        
    for i in range(1,No+1,1):     
        if No % i != 0:
            iCount = iCount + 1
    
    return iCount

def main():
    Value = 0
    iRet = 0

    print("Enter the number: ")
    Value = int(input())

    iRet = CountNonFactors(Value)

    print("Non factors count is : ",iRet)


if __name__ == "__main__":
    main()