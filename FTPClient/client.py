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

command=""
serverMessage=""
#Gets the user input that goes into the command socket
def getUserInput(commandSocket):
    while(1):
        #global command
        command = input()
        commandSend = command + "\r\n"
        message = bytes(commandSend, 'utf-8')
        commandSocket.send(message)


#Waits for a response on the command socket and prints it
def getCommandResponse(commandSocket):
    while(1):
        serverMessage = commandSocket.recv(1024).decode('utf-8')
        serverMessage = str(serverMessage)
        serverMessage="Command Port Message: "+serverMessage
        print(serverMessage)




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


#This creates the thread for user input
#_thread.start_new_thread(getUserInput,(commandSocket,))

#This creates the thread for server command port response
#_thread.start_new_thread(getCommandResponse,(commandSocket,))

#This gets confirmation from the server




#Receeives messages from the server
#waiting for a message from the server and prints it
while 1:
    command=input("FTP Command:")
    commandSend=command + "\r\n"
    message = bytes(commandSend, 'utf-8')
    commandSocket.send(message)
    serverMessage = commandSocket.recv(1024).decode('utf-8')
    serverMessage=str(serverMessage)
    print(serverMessage)


    if(command=="PASV"):
        print("Entering PASV code")
    #     portReturns=serverMessage[45:]
    #     portReturns=serverMessage[-7:]
    #     actualPortReturns=portReturns[:3]
    #     actualPortReturns= (169*256)+int(actualPortReturns)
    #     print(actualPortReturns)
    #     dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET
    #     dataSocket.connect((serverName, actualPortReturns))
    #     serverMessage = dataSocket.recv(1024).decode('utf-8')
    #     print(serverMessage)

        portReturns=serverMessage[45:]
        portReturns=serverMessage[-7:]
        actualPortReturns=portReturns[:3]
        actualPortReturn= (169*256)+int(actualPortReturns)
        #print(actualPortReturns)

        command=input("FTP Command:")
        if(command[:4]=="RETR"):
            commandSend=command + "\r\n"
            message = bytes(commandSend, 'utf-8')
            commandSocket.send(message)
            dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET
            dataSocket.connect((serverName, actualPortReturn))

            print(serverMessage)

            with open('received_file.txt', 'wb') as f:
                print("file opened")
                while True:
                    print('receiving data...')
                    data = dataSocket.recv(1024)
                    print('data=%s', (data))
                    if not data:
                        break
                        # write data to a file
                    f.write(data)
            dataSocket.close()
            f.close()
        elif(command[:4]=="list"):
            commandSend=command + "\r\n"
            message = bytes(commandSend, 'utf-8')
            commandSocket.send(message)
            dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET
            dataSocket.connect((serverName, actualPortReturn))
            serverMessage = dataSocket.recv(1024).decode('utf-8')
            print(serverMessage)
        # with open('received_file.txt', 'wb') as f:
        #     print("file opened")
        #     while True:
        #         print('receiving data...')
        #         data = commandSocket.recv(1024)
        #         print('data=%s', (data))
        #         if not data:
        #             break
        #             # write data to a file
        #         f.write(data)

        # f.close()
            dataSocket.close()
        print("-------------")

temp=input("Press enter to exit")
