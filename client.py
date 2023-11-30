import socket
import types
import os
import sys
import time

def client():
    while True:
        try:
            clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            port = 5000
            
            clientSock.connect((host, port))
            
            message = clientSock.recv(1024).decode()
            print(f"Message: {message}")
            clientSock.close()
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    client()