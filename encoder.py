def split(word):
    return [char for char in word]


# split function from stackoverflow

def encoder():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    inputArray = split(input("Enter a message to encode: ").lower())

    encoderShift = 10

    output = ""

    for y in inputArray:
        try:
            y = alphabet[(alphabet.index(y) + encoderShift)]
        except IndexError:
            y = alphabet[(alphabet.index(y) + encoderShift) - 26]
        except ValueError:
            y = y

        output += y

    print("\nMorphed message: " + output)