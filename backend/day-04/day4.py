import sys

game = ["rock", "scissors", "paper"]

def main():
    one = rps_input("Player1: ")
    two = rps_input("Player2: ")

    winner = rps_game(one, two)
    if isinstance(winner, bool):
        print("Player1 wins!") if winner else print("Player2 wins!")
    else:
        print(winner)
    sys.exit(0)

def rps_input(prompt):
    count = 0
    while True:
        pick = input(prompt)
        if pick in game:
            return pick
        else:
            count += 1
            if count > 3:
                print("Too_many_errors:exit_code(1)")
                sys.exit(1)


def rps_game(p1 ,p2):
    p1 = p1.strip().lower()
    p2 = p2.strip().lower()

    if p1 == p2:
        return "Tie!"
    else:
        for i in range(len(game) - 1):
            try:
                if game[i] == p1:
                    return p2 == game[i+1]
            except IndexError:
                return p2 == game[0]
        print("Too_many_errors:exit_code(2)")
        sys.exit(2)

if __name__=="__main__":
    main()








