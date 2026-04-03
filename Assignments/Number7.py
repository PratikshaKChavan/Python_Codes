
def CheckDivision(No1, No2):
    if No1 % No2 == 0:
        return True
    else:
        return False
    
def main():
    Value1 = 0
    Value2 = 0
    bRet = False

    print("Enter first number:  ")
    Value1 = int(input())

    print("Enter first number:  ")
    Value2 = int(input())

    bRet = CheckDivision(Value1, Value2)

    if bRet == True:
        print("Number is completely divisible")
    else:
        print("Number is not completely divisible")

if __name__ == "__main__":
    main()