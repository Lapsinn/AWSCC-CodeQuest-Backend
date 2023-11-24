from area import m_input, circle
import sys
from random import randint

def main():
    radius = m_input("Radius: ")
    area = circle(float(radius[0]))

    if len(sys.argv) == 2:
        try:
            area = round(area, int(sys.argv[1]))
        except ValueError:
            print("Invalid int for round off.")

    if len(radius) == 2:
        print(area, radius[1])
    else:
        print(area)

    random = randint(1, 10)
    if random == 7 and len(sys.argv) != 2:
        print("You can round off the decimal to your preferred number of digits\n by inserting "
              "a single int command-line argument which uses the round() function")

    sys.exit(0)


if __name__ == "__main__":
    main()
