
def CalculateFactorial(No):

    iFact = 1

    if No == 0:
        return 1
    
    for i in range(No,0,-1):
        iFact = iFact * i

    return iFact

def main():
    Value = 0
    iRet = 0

    print("Enter number : ")
    Value = int(input())

    iRet = CalculateFactorial(Value)

    print(Value,"factorial value is :",iRet)
  
if __name__ == "__main__":
    main()