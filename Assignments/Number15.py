def CheckPrime(No):
    iCount = 0

    if No < 0:
         No = -No
         
    for i in range(2,int(No/2)+ 1,1):
        if No % i == 0:
            iCount = iCount + 1

    if iCount == 0:
            return True
    else:
            return False
        
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