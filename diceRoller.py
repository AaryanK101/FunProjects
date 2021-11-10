import random

print("\nTo roll the dice, type 1")
print("To leave the roller, press 2")
while True:
    gameChoice = random.randint(1, 16)
    print("\n1. Roll Dice (1) or 2. Exit (2)")
    choice = int(input("What do choose?: "))
    if choice == 1:
        print("The dice rolled.... " + str(gameChoice))
    else:
        exit()
