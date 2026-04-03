def DisplayDigits(No):
    Digit = 0

    print("Original number is : ", No)
    print("------------------------------------")

    while No != 0:

        Digit = No % 10
        print("Digit is : ",Digit)
        No = No // 10
        print("Number is : ",No)
        print("------------------------------------")

def main():
    Value = 0
    
    print("Enter the number : ")
    Value = int(input())

    DisplayDigits(Value)    

if __name__ == "__main__":
    main()