import sys
import socket

#Server Implementation 
ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
host = 'localhost' # Asks for IP Address
port = 1234
    
ssock.bind((host, port)) # Binds the sockets
ssock.listen(5) # Maximum of Connections
    
while True:
    connection, address = ssock.accept() # Accept Connection
    buffer = connection.recv(1024)
    word = str(buffer, "utf-8")
    break
    
# Hangman Drawings
drawings = ['''
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

def board(drawings, missLetters, correctLetters, mainWord):
    print(drawings[len(missLetters)]) # Printing the drawing depends how many letters are missed 
    print() # Prints a new line
    
    print('All Missed Letters: ', end='')
    for l in missLetters:
        print(l, end='')
    print()
    
    print('All Corrected Letters: ', end='')
    for p in correctLetters:
        print(p, end='')
    print()
    
    
    for char in range(len(mainWord)):
        if mainWord[char] in correctLetters:
            print(mainWord[char], end='')
        else:
            print("_", end='')
    print()
    
#def guess(alreadyGuess, gameStatus):
#    while gameStatus:
#        #print("Did we get here?")
#        #Ask for inputLetter
#        inputLetter = guessingLetter
#        index = 0       
#        if mainWord.__contains__(inputLetter):
#            for character in mainWord:
#                if(character == inputLetter):
#                    #append to the outputword
#                    #print(index) #This will print out the index of the character that we are looking for.
#                    indexArray.append(index)
#                index = index + 1
            #Now add in the word with blanks
#        else:
#            wrongCount = wrongCount + 1
#            print(f"Total Wrongs: {wrongCount}")
        
def letterChecker(guess, guessedLetters):
    if guess.isalpha():
        # input checks
        if len(guess) != 1: # Checks Size of String
            guess = input("Enter your guessing letter: ")
            guess = guess.lower() 
        elif inputLetter in guessedLetters: # Checks if Letter have been guessed or not
            guess = input("Enter a letter that hasn't been guessed: ")
            guess = guess.lower()
    else:
        guess = input("Please enter an actual Letter: ")
        guess = guess.lower()
        
    return guess

#mainWord = input("Enter your answer:") #The word the players are guessing
mainWord = 'game'
inputLetter = '' #This is the input from the players.
missLetters = '' #All the letter that the user missed.
correctLetters = '' #All the letters that the usermgot correct.
gameStatus = True # Current Game Status
print(f"The answer is: {mainWord}") # Print out the winning word
completeWord = False

while True:
    
    #Displaying the game board
    board(drawings, missLetters, correctLetters, mainWord)
    
    # Obtaining the input  
    #inputLetter = input("Enter your guessing letter: ")
    inputLetter = connection.recv(1024)
    inputLetter = str(inputLetter, "utf-8")
    inputLetter = inputLetter.lower() # Make any letter is lowercase
    #inputLetter = letterChecker(inputLetter, missLetters + correctLetters)
    print(f"Guessed Letter: {inputLetter}")
    print(completeWord)
    
    if inputLetter in mainWord:
        if set(mainWord) == (set(correctLetters)):
            completeWord = True
        else:
            completeWord = False
        
        correctLetters = correctLetters + inputLetter
        print(set(correctLetters))
        print(set(mainWord))
        #completeWord = True # Status if word has been found
        
        #If player hasn't found all of the letters
        #for c in range(len(mainWord)):
        #    if mainWord[c] not in correctLetters:
        #        correctLetters = False
        #        break
        
        # If player found all of the letters 
        if completeWord == True:
            print("All the Letters has been found!!")
            print("Client Win")
            gameStatus = False
            break
        
    else:
        missLetters = missLetters + inputLetter
        # No more guesses are possible 
        if len(missLetters) == len(drawings) - 1:
            board(drawings, missLetters, correctLetters, mainWord) #Print out the final board
            print("No more guesses\n")
            print("Game Over, Server Lose")
            gameStatus = False
            break
    

#Finish with the game close the server
ssock.close()