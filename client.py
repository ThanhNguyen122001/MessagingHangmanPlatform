import socket
import sys

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
    host = sys.argv[1] # Asks for IP Address
    port = 1000
    
    sock.connect((host, port)) # Connects to Server
    
    userInput = input()
    sock.send(bytes(userInput, 'UTF-8'))
    print("Message Sent")
    
if __name__ == "__main__":
    client()