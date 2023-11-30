from socket import *
import os
import sys

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    port = 1000
    
    sock.bind((host, port))
    sock.listen(5)
    
    connection = sock.accept()
    address = sock.accept()
    
    return connection
    

def game():
    inputLetter = 'i' #This is the input from the players.
    mainWord = 'Main' #The word the players are guessing
    # blankWord = main
    index = 0
    
    if mainWord.__contains__(inputLetter):
        for character in mainWord:
            if(character == inputLetter):
                #append to the outputword
                print(index) #This will print out the index of the character that we are looking for.
            index = index + 1
            
if __name__ == "__main__":
    connection = server()