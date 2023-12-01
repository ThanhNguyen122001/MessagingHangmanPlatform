import sys
import socket

guessingLetter = ''

def server():
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


def game():
    inputLetter = '' #This is the input from the players.
    mainWord = '' #The word the players are guessing
    # blankWord = main
    index = 0
    wrongCount = 0
    indexArray = []
    gameStatus = True
    
    #Ask for Winning game input
    mainWord = input("Enter your Word: ")
    print(mainWord)
    
    #Print out the current drawing of hangman
    print(hangmanDrawing(wrongCount))
    
    while gameStatus:
        #print("Did we get here?")
        #Ask for inputLetter
        inputLetter = guessingLetter
        
        if wrongCount == 7:
            gameStatus = False
        
        if mainWord.__contains__(inputLetter):
            for character in mainWord:
                if(character == inputLetter):
                    #append to the outputword
                    #print(index) #This will print out the index of the character that we are looking for.
                    indexArray.append(index)
                index = index + 1
            index = 0
            #Now add in the word with blanks
        else:
            wrongCount = wrongCount + 1
            print(f"Total Wrongs: {wrongCount}")
        
        for char in mainWord:#printing out the word with spaces
            if(indexArray.__contains__(index)):
                print (inputLetter, end="")
            else:
                print("_", end="")
            index = index + 1
        print(hangmanDrawing(wrongCount))
        
           
            
def hangmanDrawing(index):
    drawings = ['''
        +---+
         |  |
            |
            |
            |
            |
        =========''', '''
        +---+
         |  |
         O  |
            |
            |
            |
        =========''', '''
        +---+
         |  |
         O  |
         |  |
            |
            |
        =========''', '''
        +---+
         |  |
         O  |
        /|  |
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
    return drawings[index]

if __name__ == "__main__":
    game()
    server()