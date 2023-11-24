from area import m_input, circle
import sys

def main():
    radius = m_input("Radius: ")
    area = circle(float(radius[0]))

    if len(sys.argv) == 2:
        try:
            area = round(area, int(sys.argv[1]))
        except ValueError:
            print("Invalid int for rounf off.")

    if len(radius) == 2:
        print(area, radius[1])
    else:
        print(area)

    sys.exit(0)


if __name__ == "__main__":
    main()
