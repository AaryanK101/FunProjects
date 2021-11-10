import random

while True:
    bot = random.randint(1, 2)
    option = str(input("\nFlip the coin? (y/n): "))
    if option == "n":
        optionN = str(input("Press q to exit flipper: "))
        if optionN == "q":
            quit()
    if option == "y" and bot == 1:
        print("...")
        print("..")
        print(".")
        print("Heads")
    elif bot == 2:
        print("...")
        print("..")
        print(".")
        print("Tails")
