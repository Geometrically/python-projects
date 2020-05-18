def EncodeCaesar(message, shift):
    shift %= 26

    encodedMessage = list(message)

    for index, letter in enumerate(message):
        if letter.islower():
            encodedASCII = ord(encodedMessage[index]) + shift - ord("a")
            encodedMessage[index] = chr(encodedASCII % 26 + ord("a"))
        elif letter.isupper():
            encodedASCII = ord(encodedMessage[index]) + shift - ord("A")
            encodedMessage[index] = chr(encodedASCII % 26 + ord("A"))

    return "".join(encodedMessage)


def DecodeCaesar(encodedMessage, knownWord):
    message = "Not found"

    for char in encodedMessage:
        if not char.isalpha() and char != " ":
            encodedMessage.replace(char, "")

    encodedWords = encodedMessage.lower().split()

    for i in range(1, 26):
        for word in encodedWords:
            testWord = EncodeCaesar(word, i)

            if knownWord.lower() == testWord:
                print("Shift:", 26 - i)
                message = EncodeCaesar(encodedMessage, i)

    return message

def EncodeVigenere(message, key):
    keys = list(key.lower())
    encodedMessage = list(message)

    offset = 0

    for index, letter in enumerate(message):
        if letter.islower():
            encodedASCII = ord(encodedMessage[index]) - ord("a")
            encodedASCIIKey = ord(keys[(index - offset) % len(keys)]) - ord("a")

            encodedMessage[index] = chr((encodedASCII + encodedASCIIKey) % 26 + ord("a"))
        elif letter.isupper():
            encodedASCII = ord(encodedMessage[index]) - ord("A")
            encodedASCIIKey = ord(keys[(index - offset) % len(keys)]) - ord("a")

            encodedMessage[index] = chr((encodedASCII + encodedASCIIKey) % 26 + ord("A"))
        else:
             offset += 1

    return "".join(encodedMessage)


def DecodeVigenere(message, key):
    keys = list(key.lower())
    encodedMessage = list(message)

    offset = 0

    for index, letter in enumerate(message):
        if letter.islower():
            encodedASCII = ord(encodedMessage[index]) - ord("a")
            encodedASCIIKey = ord(keys[(index - offset) % len(keys)]) - ord("a")

            encodedMessage[index] = chr((encodedASCII - encodedASCIIKey) % 26 + ord("a"))
        elif letter.isupper():
            encodedASCII = ord(encodedMessage[index]) - ord("A")
            encodedASCIIKey = ord(keys[(index - offset) % len(keys)]) - ord("a")

            encodedMessage[index] = chr((encodedASCII - encodedASCIIKey) % 26 + ord("A"))
        else:
             offset += 1

    return "".join(encodedMessage)


action = ""

while action != "q":
    action = input("Would you like to quit, encode, or decode? (q, e, d): ")

    if action == "e":
        cipher = input("What cipher would you like to use? (c for caesar, v for vigenere): ")
        message = input("Enter the message you would like to encode: ")

        if cipher == "c":
            shift = int(input("Enter the shift of the cipher: "))
            print("Encoded Message:", EncodeCaesar(message, shift))
        elif cipher == "v":
            key = input("Enter the key you would like to use: ")
            print("Encoded Message:", EncodeVigenere(message, key))

    elif action == "d":
        cipher = input("What cipher would you like to use? (c for caesar, v for vigenere): ")
        encoded_message = input("Enter the encoded message: ")

        if cipher == "c":
            knownWord = input("Enter a known word: ")
            print("Decoded Message:", DecodeCaesar(encoded_message, knownWord))
        elif cipher == "v":
            key = input("Enter the key of the cipher: ")
            print("Decoded Message:", DecodeVigenere(encoded_message, key))


