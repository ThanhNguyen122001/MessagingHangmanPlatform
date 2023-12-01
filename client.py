import socket

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8089))
    userInput = input()
    sock.send(bytes(userInput, 'UTF-8'))
    print("Message Sent")
    
if __name__ == "__main__":
    client()