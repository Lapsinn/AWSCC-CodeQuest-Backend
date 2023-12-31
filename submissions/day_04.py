from sys import exit

game = ["rock", "scissors", "paper"]

def main():
    one = rps_input("Player1: ")
    two = rps_input("Player2: ")

    winner = rps_game(one, two)
    print(winner)
    exit(0)

def rps_input(prompt, attempts = 3):
    count = 0
    while True:
        pick = input(prompt).strip().lower()
        if pick in game:
            return pick
        else:
            count += 1
            if count > attempts:
                print("Too_many_errors:exit_code(1)")
                exit(1)


def rps_game(p1 ,p2):

    if p1 == p2:
        return "Tie!"
    elif ((p1 == game[0] and p2 == game[1]) or
        (p1 == game[1] and p2 == game[2]) or
        (p1 == game[2] and p2 == game[0])):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


if __name__=="__main__":
    main()








