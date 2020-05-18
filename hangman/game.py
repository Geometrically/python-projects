from random import randint
import time

hangmanImage = open("hangman.txt", 'r')
hangmans = hangmanImage.read().split(',')
hangmanImage.close()

assetsFile = open("assets.txt", 'r')
assets = assetsFile.read().split(',')
assetsFile.close()

wordBank = open("wordbank.txt", 'r').readlines()
    
frequencies = {
    "a": "8.167",
    "b": "1.492",
    "c": "2.782",
    "d": "4.253",
    "e": "12.702",
    "f": "2.228",
    "g": "2.015",
    "h": "6.094",
    "i": "6.966",
    "j": "0.153",
    "k": "0.772",
    "l": "4.025",
    "m": "6.749",
    "n": "6.749",
    "o": "7.507",
    "p": "1.929",
    "q": "0.095",
    "r": "5.987",
    "s": "6.327",
    "t": "9.056",
    "u": "2.758",
    "v": "0.978",
    "w": "2.360",
    "x": "0.150",
    "y": "1.974",
    "z": "0.074"
}

def FilterByDifficulty(words, minDifficulty, maxDifficulty):
    difficultList = []
    for word in words:
        totalDifficulty = 0
        
        loweredWord = word.lower()
        
        for letter in loweredWord:
            if(letter.isalpha()):
                totalDifficulty += 100 - float(frequencies[letter])
            
        averageDifficulty = totalDifficulty/len(word)
        
        if(averageDifficulty >= minDifficulty and averageDifficulty <= maxDifficulty):
            difficultList.append(word)
    
    return difficultList

easyList = FilterByDifficulty(wordBank, 0, 80)
mediumList = FilterByDifficulty(wordBank, 80, 90)
hardList = FilterByDifficulty(wordBank, 90, 100)

def GetWord():
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ").lower().strip()[0]
    
    if(difficulty == "e"):
        return easyList[randint(0, len(easyList))].strip()
    elif (difficulty == "m"):
        return mediumList[randint(0, len(mediumList))].strip()
    elif (difficulty == "h"):
        return hardList[randint(0, len(hardList))].strip()
    else:
        print("Not a valid difficulty!")
        return GetWord()
            

playAgain = True

print(assets[0])
print("Welcome to hangman, the classic paper and pencil game now on computer!  \n Guess a pre-made word or pick a word for yourself. Made by Jai. Enjoy!")

name = input("What is your name? ")
while playAgain:
    correctWord = ""
    chooseWord = input("Would you like to pick your word from a wordbank (y/n)? ").lower().strip()[0]
    
    if chooseWord == "n":
        correctWord = input("Okay, what would you like to guess? ").lower()
    else:
        correctWord = GetWord().lower()
        
    correctGuesses = []
    incorrectGuesses = []
    
    for dash in correctWord:
        if(dash == " "):
            correctGuesses.append(" ")
        else:
            correctGuesses.append("_ ")
            
    startTime = time.time()
    
    while ''.join(correctGuesses) != correctWord and len(incorrectGuesses) < 7:
        print("\n"*120)
        
        print(hangmans[len(incorrectGuesses)])
        print("Incorrect Guesses:", incorrectGuesses)
        print(''.join(correctGuesses))

        guess = input("Enter a letter or the word you think it is: ").lower().strip()
        
        if(guess not in incorrectGuesses):
            if(guess == correctWord):
                correctGuesses = list(guess)
             
            correct = False
            for index,value in enumerate(correctWord):
                if(value == guess):
                    correctGuesses[index] = value
                    correct = True
                             
            if not correct:
                incorrectGuesses.append(guess)
        else:
            print("You already guessed this")
    
    if(len(incorrectGuesses) >= 7):
        print("The correct word was " + correctWord + "! Nice try!")
    else:
        endTime = time.time()
        
        score = round((endTime - startTime)/len(incorrectGuesses), 2) if len(incorrectGuesses) != 0 else round((endTime - startTime), 2)
        
        print(correctWord)
        print("Nice job! Your score was", score)
        
    askPlayAgain = input("Want to play again? (y/n): ").lower().strip()[0]
    
    if (askPlayAgain == "n"):
        print(assets[1])
        playAgain = False