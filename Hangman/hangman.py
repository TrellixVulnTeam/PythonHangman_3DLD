import random

HangmanStages = ['''

     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
  
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

alphabet = ''

guessWords = 'hackathon program computer science language editor python android studio visual basic paradigm imperative functional java'.split()

# getGuessWord takes in a list of strings and returns a random word from the list
def getGuessWord(words):
    wordsIndex = random.randint(0, len(guessWords) - 1)
    return words[wordsIndex]

# setupBoard takes in a list of ASCII art for various stages of hangman, a list of all the wrongly guessed letters,
# a list of the letters guessed correctly, and the word being guessed
def setUpBoard(HangmanPic, wrongLetters, correctLetters, guessWord):
    print(HangmanPic[len(wrongLetters)])
    print()

    print('Wrong letters:', end= ' ')
    for letter in wrongLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(guessWord)

    # blanks are replaced with the correct letters if guessed by user
    for i in range(len(guessWord)):
        if guessWord[i] in correctLetters:
            blanks = blanks[:i] + guessWord[i] + blanks[i+1:]

    # adding spaces in between each letter of guessWord
    for letter in blanks:
        print(letter, end=' ')

    print()

# getGuess takes in the letters already guessed by user to verify the user's guess is not a repeat
# and that their guess is valid (i.e. one letter)
def getGuess(alreadyGuessed):
    while True:
        print()
        guessLetter = input('Guess a letter.')
        guessLetter = guessLetter.lower()
        if len(guessLetter) > 1:
            print('Please guess a single letter.')
        elif guessLetter in alreadyGuessed:
            print('You have already guessed this letter. Guess again.')
        elif not guessLetter.isalpha():
            print('Please enter a letter only.')
        else:
            return guessLetter

# newGame returns True if the user wants to start a new game and False otherwise
def newGame():
    print('Do you want to play again? (yes or no)')
    userResponse = input()
    if userResponse == 'yes':
        return True;

print('H A N G M A N')
wrongLetters = ''
correctLetters = ''
guessWord = getGuessWord(guessWords)
gameOver = False

while True:
    setUpBoard(HangmanStages, wrongLetters, correctLetters, guessWord)

    alreadyGuessedLetters = wrongLetters + correctLetters

    userGuess = getGuess(alreadyGuessedLetters)

    if userGuess in guessWord:
        correctLetters = correctLetters + userGuess

        # Checking if user has won
        foundAllLetters = True
        for i in range(len(guessWord)):
            if guessWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Congrats! You guessed the word ' + guessWord + '!')

            gameOver = True

    else:

        wrongLetters = wrongLetters + userGuess

        # Checking if user has exceeded maximum number of guesses
        if len(wrongLetters) == len(HangmanStages) - 1:
            setUpBoard(HangmanStages, wrongLetters, correctLetters, guessWord)

            print('Game Over! You have run of guesses!\nThe word was ' + guessWord + '.')

            gameOver = True

    if gameOver:
        if newGame():
            missedLetters = ''
            correctLetters = ''
            gameOver = False
            guessWord = getGuessWord(guessWords)

        else:
            break









