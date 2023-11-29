import socket
import selectors
import os 
import sys
import types

def server():
    host = sys.argv[1]
    port = int(sys.argv[2])
    select = selectors.DefaultSelector()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    #Checking the Host and Port number
    print(f"Host: {(host)}")
    print(f"Port: {(port)}")
    sock.setblocking(False)
    select.register(sock, selectors.EVENT_READ, data=None)
    
    try:
        while True:
            event = select.select(timeout=None)
            
    finally:
        sock.close()

def game():
    inputLetter = 'i' #This is the input from the players.
    mainWord = 'Main' #The word the players are guessing
    blankWord = 
    index = 0
    
    if mainWord.__contains__(inputLetter):
        for character in mainWord:
            if(character == inputLetter):
                #append to the outputword
                print(index) #This will print out the index of the character that we are looking for.
            index = index + 1
            

game()