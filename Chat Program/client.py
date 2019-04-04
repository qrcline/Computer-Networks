from socket import *
from select import *
from threading import *

from sys import *

# setup socket to connect to server

serverName = 'localhost'
serverPort = 43500
# serverName = input('Please input server address/name?')
# serverPort = input('Please input server port?')
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
clientSocket.connect((serverName, int(serverPort)))
# print('Connected to server\n')

# receive message from server, print it, close connection
serverMessage = ''
clientMessage = ''

#This gets the client number
clientNumber = clientSocket.recv(1024).decode('utf-8')
print('Client number ' + clientNumber)

#This gets confirmation from the server
serverMessage = clientSocket.recv(1024).decode('utf-8')
print(serverMessage)

#Sets the initial state
print(clientNumber)
if (int(clientNumber))%2:
    state=0
else:
    state=1
print(state)

while 1:
    if state==1:
        clientMessage = input('Self:')
        message = bytes(clientMessage, 'utf-8')
        clientSocket.send(message)
        state=0
    else:
        serverMessage = clientSocket.recv(1024).decode('utf-8')
        print(serverMessage)
        state=1








    # for sockets in read_sockets:
    #     if sockets == clientSocket:
    #         serverMessage = clientSocket.recv(1024).decode('utf-8')
    #         print(serverMessage)
    #     else:
    #         clientMessage = input('Self:')
    #         message = bytes(clientMessage, 'utf-8')
    #         clientSocket.send(message)



clientSocket.close()
input('Press any key to exit')
