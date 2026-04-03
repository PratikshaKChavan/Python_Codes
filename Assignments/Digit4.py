def main():
    No = 0
    Digit = 0

    print("Enter the number : ")
    No = int(input())

    print("Original number is : ", No)
    print("------------------------------------")
    
    while No != 0:
        Digit = No % 10
        print("Digit is : ",Digit)
        No = No // 10
        print("Number is : ",No)
    
        print("------------------------------------")

if __name__ == "__main__":
    main()