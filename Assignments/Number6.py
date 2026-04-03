

def main():
    Value1 = 0
    Value2 = 0

    print("Enter first number:  ")
    Value1 = int(input())

    print("Enter first number:  ")
    Value2 = int(input())

    if Value1 % Value2 == 0:
        print("Number is completely divisible")
    else:
        print("Number is not completely divisible")

if __name__ == "__main__":
    main()