def main():
    result = starter_adv()
    print(result)

def starter_adv():
    choice1 = yes_or_no("A Man is asking for shelter.\n"
                        "Do you let him in or not? ")
    if choice1 == True:
        choice2 = yes_or_no("Police arrived and asked whether thief is inside.\n"
                            "Will you rat him out? ")
    else:
        choice2 = yes_or_no("He attacked on you.\nWill you knock him down? ")

    if choice2 == True:
        return "WIN"
    else:
        return "Game Over"

def yes_or_no(prompt):
    while True:
        choice = input(prompt).strip()
        if match_yes(choice) == True:
            return True
        elif match_no(choice) == True:
            return False
        else:
            print("Invalid input")
            continue


def match_yes(choice):
    choice = choice.capitalize()
    match choice:
        case "Yes":
            return True
        case "Y":
            return True
        case _:
            return False

def match_no(choice):
    choice = choice.capitalize()
    match choice:
        case "No":
            return True
        case "N":
            return True
        case _:
            return False

if __name__ == "__main__":
    main()


