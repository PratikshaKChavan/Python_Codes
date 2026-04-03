def SumDigits(No):
    Digit = 0
    iSum = 0

    if No < 0:
        No = -No

    print("------------------------------------")

    while No != 0:

        Digit = No % 10 
        No = No // 10 
        iSum = iSum + Digit

    return iSum

def main():
    Value = 0
    iRet = 0
    
    print("Enter the number : ")
    Value = int(input())

    iRet = SumDigits(Value)   

    print("The sum of digits is : ",iRet) 

if __name__ == "__main__":
    main()



    