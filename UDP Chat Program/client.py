#importing the socket
from socket import *

#setup socket to connect to server
server_address = ('localhost', 43500) #setting the server adress
clientSocket = socket(AF_INET, SOCK_DGRAM) #UDP socket

#gather and send message to server
sentence = input('Input lowercase sentence: ')
clientSocket.sendto(sentence.encode('utf-8'), server_address)

#receive message from server, print it
modifiedSentence = clientSocket.recv(1024).decode('utf-8')
#Print the message from the server
print('From Server:', modifiedSentence)
#Close the connection
clientSocket.close()
