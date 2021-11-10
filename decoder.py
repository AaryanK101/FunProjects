import encoder
import copy

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def keyEncoder():
    keywordArray = encoder.split(input("What is the keyword?: ").lower())
    decodeEncode = input("Are you encoding or decoding?: ")
    messageArray = encoder.split(input("Enter a message to morph: ").lower())

    encodedArray = []
    keyLength = len(keywordArray)
    outputArray = []
    specialCharArray = copy.copy(messageArray)
    output = ""

    # Removes all special chars so the message can be correctly encoded
    for k in messageArray:
        try:
            k = alphabet.index(k)
        except ValueError:
            kNext = messageArray.index(k)
            messageArray.remove(k)
            # ignore this
            while True:
                try:
                    if not messageArray[kNext] in alphabet:
                        del messageArray[kNext]
                    else:
                        break
                except IndexError:
                    break

    # Makes the keywordArray into their alphabetical indexes (relative to the alphabet array)
    for y in keywordArray:
        z = alphabet.index(y)
        keywordArray[keywordArray.index(y)] = z

    # Creates the encoded array
    for x in messageArray:
        try:
            msgIndex = messageArray.index(x)
            x = alphabet.index(x)
            if decodeEncode == "encoding":
                c = x + keywordArray[messageArray.index(alphabet[x]) % keyLength]
            if decodeEncode == "decoding":
                c = x - keywordArray[messageArray.index(alphabet[x]) % keyLength]
            messageArray[msgIndex] = 0
            encodedArray.append(alphabet[c])
        except IndexError:
            encodedArray.append(alphabet[c - 26])

    # Creates the output array from adding special chars to the encoded array in the right spots
    for u in encodedArray:
        if specialCharArray[0] in alphabet:
            outputArray.append(u)
            del specialCharArray[0]
        else:
            outputArray.append(specialCharArray[0])
            del specialCharArray[0]
            while True:
                if not specialCharArray[0] in alphabet:
                    outputArray.append(specialCharArray[0])
                    del specialCharArray[0]
                else:
                    break
            outputArray.append(u)
            del specialCharArray[0]

    # Appends any extra special characters to the end of the output, if there are any
    if len(specialCharArray) > 0:
        for q in specialCharArray:
            outputArray.append(q)

    # Combines elements of the output array into a single string to be printed
    for p in outputArray:
        output += p

    print(output)

keyEncoder()