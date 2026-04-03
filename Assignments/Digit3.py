def main():
    No = 7234
    Digit = 0

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