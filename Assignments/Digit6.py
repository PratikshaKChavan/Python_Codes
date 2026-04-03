def CountDigits(No):
    Digit = 0
    iCount = 0

    print("Original number is : ", No)
    print("------------------------------------")

    while No != 0:

        Digit = No % 10 
        No = No // 10 
        iCount = iCount + 1

    return iCount

def main():
    Value = 0
    iRet = 0
    
    print("Enter the number : ")
    Value = int(input())

    iRet = CountDigits(Value)   

    print("Number of digits are : ",iRet) 

if __name__ == "__main__":
    main()