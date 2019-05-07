 #Author: Karl Mazur and Quinton Cline
#This is a FTP Client
#This file contains code for interfacing with a ftp server
#Allows the user to list, RETR and STOR files to ftp server



from socket import *
from select import *
import _thread
import sys
command=""
serverMessage=""

#Server name and port to connect to
serverName='72.233.138.35'
serverPort=24601

#connect to the server using a tcp socket
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


#loop that allows input of commands
while 1:
    #get a command from the user and send it to the server
    command=input("FTP Command:")
    commandSend=command + "\r\n" #must add \r\n to the message before it is sent
    message = bytes(commandSend, 'utf-8')
    commandSocket.send(message)
    serverMessage = commandSocket.recv(1024).decode('utf-8') #Receive a message from the server
    serverMessage=str(serverMessage) #Convert to a string
    print(serverMessage) #Print the message

    #If the command is PASV send PASV command to put the server into pasv mode
    if(command=="PASV"):
        print("Entering PASV code")
        #This gets the new port number that is returned from the server
        #when put into pasv mode
        portReturns=serverMessage[45:]
        portReturns=serverMessage[-7:]
        actualPortReturns=portReturns[:3]
        actualPortReturn= (169*256)+int(actualPortReturns)


        command=input("FTP Command:")#Get another command
        #user inputs "RETR <file name> to be returned
        if(command[:4]=="RETR"): #RETR command returns a file from the server
            commandSend=command + "\r\n"
            message = bytes(commandSend, 'utf-8') #Send the RETR command
            commandSocket.send(message)
            dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET
            dataSocket.connect((serverName, actualPortReturn))
            serverMessage = commandSocket.recv(1024).decode('utf-8')
            print(serverMessage)

            # save the returned file to file.txt on local machine
            with open('file.txt', 'wb') as f:
                print("file opened")
                while True:
                    print('receiving data...')
                    data = dataSocket.recv(1024) #receive the returned file on the data socket
                    print('data=%s', (data))
                    if not data:
                        break
                    f.write(data) # write data to a file

            dataSocket.close() #Close the data socket
            serverMessage = commandSocket.recv(1024).decode('utf-8') #Receive message on command socket
            print(serverMessage)

            print("-------------")
            f.close()

            #if user inputs LIST printout the files and directories
        elif(command[:4]=="LIST"):
            commandSend=command + "\r\n" #Format the command
            message = bytes(commandSend, 'utf-8')
            commandSocket.send(message) #send it
            dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET #open the data socket
            dataSocket.connect((serverName, actualPortReturn))
            serverMessage = commandSocket.recv(1024).decode('utf-8') #Receive message on command socket
            print(serverMessage)
            serverMessage = dataSocket.recv(1024).decode('utf-8') #Receive the return of LIST on data socket
            print(serverMessage)
            dataSocket.close()
            serverMessage = commandSocket.recv(1024).decode('utf-8') #Receive second message on commandsocket
            print(serverMessage)
            print("-------------")



        # User inputs "STOR <file name>" of the file they want to add to the server
        # Note the first file name will be the name of the file on the ftp server
        elif (command[:4] == "STOR"):
            print("in STOR")
            commandSend = command + "\r\n"
            message = bytes(commandSend, 'utf-8')
            commandSocket.send(message) #Send the STOR command


            dataSocket = socket(AF_INET, SOCK_STREAM)  # TCP SOCKET, opens the data socket
            dataSocket.connect((serverName, actualPortReturn))
            fileDirectory=input("File to send: ")   #Get the filename of the file on local machine to send to server
            #open the file from computer and send to the server
            f = open(fileDirectory, "r")
            for content in f:
                dataSocket.send(content.encode()) #Send the file to the ftp server on the data socket
                print(content)
            f.close()
            dataSocket.close() #Close the data socket
            serverMessage = commandSocket.recv(1024).decode('utf-8')
            print(serverMessage)
            print("in STOR send")
            serverMessage = commandSocket.recv(1024).decode('utf-8')
            print(serverMessage)
            dataSocket.close()
            print("-------------")
        #If in PASV code and command not recognized
        else:
            print("nonValid command in PASV")






temp=input("Press enter to exit")
