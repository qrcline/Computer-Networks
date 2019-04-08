from socket import *
from select import *
import _thread
import sys

from sys import *

def getUserInput(clientSocket):
    while(1):
        clientMessage = input()
        message = bytes(clientMessage, 'utf-8')
        clientSocket.send(message)

if len(sys.argv) !=3:
    print("Requires 1 command line argument of the port number")
    sys.exit(-1)
# setup socket to connect to server

serverName = sys.argv[1]
serverPort = sys.argv[2]
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
clientSocket.connect((serverName, int(serverPort)))

# receive message from server, print it, close connection
serverMessage = ''
clientMessage = ''

#This gets confirmation from the server
serverMessage = clientSocket.recv(1024).decode('utf-8')
print(serverMessage)

#This creates the thread for user input
_thread.start_new_thread(getUserInput,(clientSocket,))

#Receeives messages from the server
while 1:
    serverMessage = clientSocket.recv(1024).decode('utf-8')
    print(serverMessage)





clientSocket.close()
input('Press any key to exit')
