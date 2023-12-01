import sys
import socket

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a Socket
    host = sys.argv[1] # Asks for IP Address
    port = 1000
    
    sock.bind((host, port)) # Binds the sockets
    sock.listen(5) # Maximum of Connections
    
    while True:
        connection, address = sock.accept() # Accept Connection
        buffer = connection.recv(1024)
        print(str(buffer, "utf-8"))
        word = str(buffer, "utf-8")
        break
    
    print(word)


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
    server()