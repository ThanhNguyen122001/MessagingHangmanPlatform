from tkinter import *

def userInterface(): # Creating an User Interface
    GUI = Tk() # Initalize Object
    GUI.title("Hangman Game") # Setting Title of User Interface
    GUI.geometry("400x400") # Size of User Interface
    
    guessHistory = Text(GUI, bg='white', width='50', height='8') # Creates a box for the history of Guesses made
    guessHistory.config(state=DISABLED)
    
    sendButton = Button(GUI, bg='red', width='50', height='8') # Creates a button to send the guess
    
    GuessBox = Text(GUI, bg='white', width='50', height='8')
    
    GUI.mainloop() # Loops the User Interface
    

def game():
    inputLetter = 'i' #This is the input from the players.
    mainWord = 'Main' #The word the players are guessing
    blankWord = main
    index = 0
    
    if mainWord.__contains__(inputLetter):
        for character in mainWord:
            if(character == inputLetter):
                #append to the outputword
                print(index) #This will print out the index of the character that we are looking for.
            index = index + 1
            
if __name__ == "__main__":
    userInterface()