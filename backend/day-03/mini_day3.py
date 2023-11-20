def main():
    integer = int(input("Enter a number: "))

    if integer < 0:
        eval = "Negative number"
    elif integer > 0:
        eval = "Postive number"
    else:
        eval = "Zero"
        integer = "That number"

    print(f"{integer} is a {eval}!")

if __name__ == '__main__':
    main()
