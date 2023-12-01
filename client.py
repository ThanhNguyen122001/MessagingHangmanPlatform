import socket
import sys

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
    host = 'localhost' # Asks for IP Address
    port = 1234
    
    sock.connect((host, port)) # Connects to Server
    
    try:
        while True:
            userInput = input()
            sock.send(bytes(userInput, 'UTF-8'))
            print("Message Sent")
    except KeyboardInterrupt:
        sock.close()
        
if __name__ == "__main__":
    client()