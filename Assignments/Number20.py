
def CheckPerfect(No):
    iSum = 0

    for i in range(1,int(No/2) + 1):
        if No % i == 0:
            iSum = iSum + i

            if iSum > No:
                break

    return iSum == No

def main():
    Value = 0
    bRet = False

    print("Enter number : ")
    Value = int(input())

    bRet = CheckPerfect(Value)

    if bRet == True:
        print(Value,"is a perfect number")
    else:
        print(Value,"is not a perfect number")

if __name__ == "__main__":
    main()