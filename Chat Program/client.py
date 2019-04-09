#Author: Quinton Cline
#This is a TCP Chat Client
#The client must first get a connection confirmation before user input accepted.
#This file contains code for sending and receiving messages from a tcp chat server.



from socket import *
from select import *
import _thread
import sys

#Function: getUserInput
#Return:void
#Parameters: clientSocket
#Effect: this function is used in called by the thread
#        it waits for user input and sends the user
#        input to the server

def getUserInput(clientSocket):
    while(1):
        clientMessage = input()
        message = bytes(clientMessage, 'utf-8')
        clientSocket.send(message)


#Checks if correct number of command line arguments
if len(sys.argv) !=3:
    print("Requires 1 command line argument of the port number")
    sys.exit(-1)

# setup socket to connect to server
serverName = sys.argv[1]
serverPort = sys.argv[2]
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
clientSocket.connect((serverName, int(serverPort)))

serverMessage = ''
clientMessage = ''

#This gets confirmation from the server
serverMessage = clientSocket.recv(1024).decode('utf-8')
print(serverMessage)

#This creates the thread for user input
_thread.start_new_thread(getUserInput,(clientSocket,))

#Receeives messages from the server
#waiting for a message from the server and prints it
while 1:
    serverMessage = clientSocket.recv(1024).decode('utf-8')
    print(serverMessage)






