import socket
import sys

#Client Implementation
csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
host = 'localhost' # Asks for IP Address
port = 1234
    
csock.connect((host, port)) # Connects to Server

while True:
    userInput = input("Enter your guessing letter: ")
    csock.send(bytes(userInput, 'UTF-8'))
    print("Message Sent")