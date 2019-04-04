from socket import *

MAX_CLIENTS = 2






#setup socket to wait for connections
serverPort = 43500
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to accept clients')

clients = []
#accept up to two connections from clients, which
# must connect before we can move on
for i in range(0, MAX_CLIENTS):
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))

#Sends each of the clients the ID number and the connected to server
for i in range(0, MAX_CLIENTS):
    clients[i][0].send(bytes(str(i), 'utf-8'))
    clients[i][0].send(bytes('Connected to server \n','utf-8'))


#omitting while loop means the server will run once!
while 1:
    for i in range(0, MAX_CLIENTS):

       # if i % 2:
       #     clients[i][0].send(b'there!\n')
       # else:
       #     clients[i][0].send(b'Hello \n')

       receivedMessage=''
       receivedMessage= clients[i][0].recv(1024).decode('utf-8')
       receivedMessage= 'From Client'+str(i)+': '+(receivedMessage)
       print(receivedMessage)
       for j in range(0, MAX_CLIENTS):
           if(j!=i):
               clients[j][0].send(bytes(receivedMessage, 'utf-8'))

