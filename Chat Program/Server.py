#Author: Quinton Cline
#This is a TCP Chat Server
#The server wates for clients to connect and creates a port and thread for each client
#The server does not have a set number for max connections
#There is bot responses in the bot section


import socket,_thread,sys,random,datetime



#The jokes
jokes=[]
jokes.append("Server Joke:\nJWhat do you call a spaceship with a broken air-conditioning unit?\nA frying saucer.")
jokes.append("Server Joke:\nWhy was the broom late?\n It overswept.")

#Function: newClientConnection
#Return:void
#Parameters: socketInput <- the socket that the client is connected to
#Effect: this function is called when a new client connects and a thread is
#         created. The function waits for user input on the given socket and
#         responds if !bot is found or sends the message to all other clients.
def newClientConnection(socketInput):
    socketInput.send(bytes('Connected to server \n', 'utf-8'))
    while(1):
        receivedMessage = socketInput.recv(1024).decode('utf-8')

        ############################
        ##### BOT SECTION  #########
        ############################
        if receivedMessage == "!bot joke":
            botMessage = jokes[random.randrange(0, 2, 1)]
            socketInput.send(bytes(botMessage, 'utf-8'))
        elif receivedMessage == "!bot time":
            botMessage = str(datetime.datetime.now())
            socketInput.send(bytes(botMessage, 'utf-8'))
        else:
            #Sends the received message out to the other clients
            receivedMessage = 'From Server:'  + (receivedMessage)
            print(receivedMessage)
            for client in clients:
                if client[0] is not socketInput: #Don't send message back to the same person
                    client[0].send(bytes(receivedMessage, 'utf-8'))

#Get the server port as command line argument
#Checks if there is the corrrect number of arguments
if len(sys.argv) !=2:
    print("Requires 1 command line argument of the port number")
    sys.exit(-1)

#setup server socket to wait for connections
serverPort = sys.argv[1]# gets the socket from the command line argument
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', int(serverPort)))
serverSocket.listen(1)
print('The server is ready to accept clients')
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print('IP: '+str(IPAddr)+' Port: '+str(sys.argv[1]))

clients = []

#This loop is looking for new connections
#If there is a new connection a socket is created and added to the clients array
while 1:
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))
    #Prints when a new client connects and the ip and port
    print('New Client IP: ' + str(addr) + ' Port: ' + str(sys.argv[1]))
    # This creates the thread for user input
    _thread.start_new_thread(newClientConnection, (connectionSocket,))

