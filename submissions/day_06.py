from sys import exit

def main():
    limit = int(input("Limit: "))
    for i in range(limit):
        fzbz_game(i + 1)
    exit(0)

def fzbz_game(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz!")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

if __name__ == "__main__":
    main()
