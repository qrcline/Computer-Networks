from socket import *

#Server port and IP
serverPort = 43500
clientIp='127.0.0.1'
#Setup the socket
serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind((clientIp, serverPort))
print('The server is ready to receive')
#omitting while loop means the server will run once!
while 1:
    #receive message from client, print it, close socket
    data, addr = serverSock.recvfrom(1024)
    #print "Message: ", data
    print(data.decode('utf-8'))
    #capitalize message from client, send back, close connection
    capitalizedSentence = data.upper()
    serverSock.sendto(capitalizedSentence,addr)

