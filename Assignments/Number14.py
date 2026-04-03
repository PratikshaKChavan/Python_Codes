def CountFactorsNonFactors(No):
    iCount1 = 0
    iCount2 = 0

    if No < 0:
        No = -No
        
    for i in range(1,No+1,1):     
        if No % i == 0:
            iCount1 = iCount1 + 1
        else:
            iCount2 = iCount2 + 1 
    
    print("Number of Factors are : ",iCount1)
    print("Number of Non factors are : ",iCount2)

def main():
    Value = 0

    print("Enter the number: ")
    Value = int(input())

    CountFactorsNonFactors(Value)

if __name__ == "__main__":
    main()