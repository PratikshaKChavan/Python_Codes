
def Display(No):
    for i in range(No, 0, -1):
        print(i, end=" ")

def main():
    Value = 0

    print("Enter number: ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()