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
#Parameters: commandSocket
#Effect: this function is used in called by the thread
#        it waits for user input and sends the user
#        input to the server

def getUserInput(commandSocket):
    while(1):
        clientMessage = input()
        message = bytes(clientMessage, 'utf-8')
        commandSocket.send(message)


# #Checks if correct number of command line arguments
# if len(sys.argv) !=3:
#     print("Requires 1 command line argument of the port number")
#     sys.exit(-1)

# setup socket to connect to server
# serverName = sys.argv[1]
# serverPort = sys.argv[2]
serverName='72.233.138.35'
serverPort=24601
commandSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
commandSocket.connect((serverName, int(serverPort)))

serverMessage = ''
clientMessage = ''
#Gets feedback from the server
serverMessage = commandSocket.recv(1024).decode('utf-8')
print(serverMessage)

#send username
clientMessage="USER clineq\r\n"
message = bytes(clientMessage, 'utf-8')
commandSocket.send(message)
serverMessage = commandSocket.recv(1024).decode('utf-8')
print(serverMessage)

#send password
clientMessage="PASS waterski1\r\n"
message = bytes(clientMessage, 'utf-8')

commandSocket.send(message)
serverMessage = commandSocket.recv(1024).decode('utf-8')
print(serverMessage)


#This gets confirmation from the server




#Receeives messages from the server
#waiting for a message from the server and prints it
while 1:
    command=input("FTP Command:")
    commandSend=command + "\r\n"
    message = bytes(commandSend, 'utf-8')
    commandSocket.send(message)
    serverMessage = commandSocket.recv(1024).decode('utf-8')
    portReturn=serverMessage[-2:]
    print(serverMessage)
    if(command=="PASV"):
        dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET
        dataSocket.connect((serverName, 240))
        serverMessage = dataSocket.recv(1024).decode('utf-8')
        print(serverMessage)
temp=input("Press enter to exit")
