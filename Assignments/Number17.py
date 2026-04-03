def CheckPrime(No):
    iCount = 0
    bFlag = True

    if No < 0:
         No = -No
         
    for i in range(2,int(No/2)+ 1,1):
        if No % i == 0:
            bFlag = False
            break                    # Optimization

    return bFlag
        
def main():
    Value = 0
    bRet = False

    print("Enter number : ")
    Value = int(input())

    bRet = CheckPrime(Value)

    if bRet == True:
        print(Value,"is prime number")

    else:
        print(Value, "is not a prime number")

if __name__ == "__main__":
    main()