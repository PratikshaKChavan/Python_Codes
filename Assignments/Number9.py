def DisplayFactors(No):
    if No < 0:
        No = -No
        
    for i in range(1,No,1):
        if No % i == 0:
            print(i)
            
def main():
    Value = 0

    print("Enter the number: ")
    Value = int(input())

    DisplayFactors(Value)


if __name__ == "__main__":
    main()