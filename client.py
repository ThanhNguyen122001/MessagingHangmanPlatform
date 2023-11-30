from socket import *

def client():
    sock = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    port = 1000
    
    sock.connect((host, port))

if __name__ == "__main__":
    client()