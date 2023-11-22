import day_04
from random import choice

def main():
    pick = day_04.rps_input("Rock, Paper, Scissor, Shoot!: ", attempts = 5)
    pick2 = choice(day_04.game)
    winner = day_04.rps_game(pick, pick2)
    if winner == "Tie!":
        print(winner)
    elif winner == "Player 1 wins!":
        print("You win!")
    else:
        print(f"Computer chose {pick2}. You lost.")
    day_04.exit(0)

if __name__ == '__main__':
    main()
