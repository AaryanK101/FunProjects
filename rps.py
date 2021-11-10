import random

def rps():
    choices = ["rock", "paper", "scissors", "exit"]
    while True:
        playerChoice = input("Rock, paper, or scissors?: ").lower()
        gameChoice = random.randint(1, 3)
        try:
            playerChoice = choices.index(playerChoice) + 1
        except ValueError:
            print("hey that's not rock, paper or scissors")
            continue
        if playerChoice == 4: return
        elif gameChoice == playerChoice: print("Draw!")
        elif gameChoice == playerChoice + 1: print("Bot wins!")
        elif gameChoice == playerChoice - 2: print("Bot wins!")
        else: print("You win!")
        print("The bot played " + choices[gameChoice - 1] + ".")
        continue
rps()