import sys
import socket

#Server Implementation 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
host = 'localhost' # Asks for IP Address
port = 1234
    
sock.bind((host, port)) # Binds the sockets
sock.listen(5) # Maximum of Connections
    
while True:
    connection, address = sock.accept() # Accept Connection
    buffer = connection.recv(1024)
    print(str(buffer, "utf-8"))
    guessingLetter = str(buffer, "utf-8")
    break
    
print(guessingLetter)

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
    indexArray = [] #This will hold the index values of the 
    
    emptyLetters = '_' * len(mainWord) # Prints '_' how many times depends on the length of the 'mainWord"
    
    # Filling the empty Letters
    for c in range(len(mainWord)):
        if mainWord[c] in correctLetters:
            emptyLetters = emptyLetters[:c] + mainWord[c] + emptyLetters[c+1:]
            
    # Printing out the work
    for let in emptyLetters:
        print(let, end='')
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

mainWord = input("Enter your secret word: ") #The word the players are guessing
print(mainWord) #Printing "mainWord" to server terminal to check if it working
inputLetter = '' #This is the input from the players.
missLetters = '' #All the letter that the user missed.
correctLetters = '' #All the letters that the usermgot correct.
gameStatus = True # Current Game Status
while True:
    #Displaying the game board
    board(drawings, missLetters, correctLetters, mainWord)
    
    # Obtaining the input  
    inputLetter = input("Enter your guessing letter: ")
    inputLetter = inputLetter.lower() # Make any letter is lowercase
    inputLetter = letterChecker(inputLetter, missLetters + correctLetters)
        
    if inputLetter in mainWord:
        correctLetters = correctLetters + inputLetter
        completeWord = True # Status if word has been found
        
        #If player hasn't found all of the letters
        for c in range(len(mainWord)):
            if mainWord[c] not in correctLetters:
                correctLetters = False
                break
        
        # If player found all of the letters 
        if completeWord == True:
            print("All the Letters has been found!!")
            print("You Win")
            gameStatus = True
            break
        
    else:
        missLetters = missLetters + inputLetter
        # No more guesses are  possible 
        if len(missLetters) == len(drawings) - 1:
            board(drawings, missLetters, correctLetters, mainWord) #Print out the final board
            print("No more guesses\n")
            print("Game Over, You Lose")
            gameStatus = False
            break
    

#Finish with the game close the server
sock.close()