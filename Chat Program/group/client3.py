
from socket import *
import sys, select





#setup socket to connect to server
serverName = str(sys.argv[1])
serverPort = str(sys.argv[2])
serverPort=int(serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))
#receive message from server, print it, close connection
message = ' '
#recieves client number
clientNum=clientSocket.recv(1024).decode('utf-8')
#receives the numver of clients
numClients=int(clientSocket.recv(1024).decode('utf-8'))

# let the user know what client number it is
print("You are client ",clientNum)
clientNum=int(clientNum)
while 1:
    #gets who's turn it is from the server
    currentClient=clientSocket.recv(1).decode('utf-8')
    print(currentClient)
    currentClient=int(currentClient)
    #if the turn is this client then input is asked for by user
    # the message is then sent to server
    if currentClient is clientNum:
        newMessage=input('input:')
        clientSocket.sendall(newMessage.encode('utf-8'))
    #decodes the message and prints it
    message = clientSocket.recv(1024).decode('utf-8')
    print(message)
clientSocket.close()