import math

def m_input(prompt = "Input: "):
    while True:
        measure = input(prompt).split(" ")
        length = len(measure)
        if length == 1:
            measure = measure[0]
            break
        elif length == 2:
            unit = measure[1]
            measure = measure[0]
            break
        else:
            print("Insert only an integer and a unit(if preferred)")

    try:
        return [measure, unit]
    except NameError:
        return [measure]

def circle(radius):
    try:
        return math.pi*(radius**2)
    except ValueError as ve:
        return ve

def square(side):
    try:
        return side**2
    except ValueError as ve:
        return ve

def rectangle(width, length):
    try:
        return width * length
    except ValueError as ve:
        return ve

def triangle(base, height):
    try:
        return base * height / 2
    except ValueError as ve:
        return ve

