import socket,_thread,sys
import _thread
import sys
import random
import


jokes=[]
jokes.append("Server Star Wars Joke:\nJabba the Hut is fat.\nHow fat is he?\nSo fat, Obi Wan took a closer look and said, “That’s no moon.”")
jokes.append("Server Star Wars Joke:\nWhat kind of car does a Jedi drive?\nA Toy Yoda.")
jokes.append("Server Star Wars Joke:\nWhich program do Jedi use to open PDF files in Star Wars?\nAdobe-Wan Kenobi!")
jokes.append("Server Star Wars Joke:\nWhy was the droid angry?\nPeople kept pushing its buttons.")
jokes.append("Server Star Wars Joke:\nWhat is Jabba the Hutt’s middle name?\nI don’t remember.\nThe.\n")

def newClientConnection(socketInput):
    socketInput.send(bytes('Connected to server \n', 'utf-8'))
    while(1):
        receivedMessage = socketInput.recv(1024).decode('utf-8')

        ############################
        ##### BOT SECTION  #########
        ############################
        if receivedMessage == "!bot joke":
            jokeNum = random.randrange(0, 5, 1)
            newMessage = jokes[jokeNum]
        elif receivedMessage == "!bot tell me the time":
            newMessage = str(datetime.datetime.now())
        elif receivedMessage == "!bot show me Dingler's Bio":
            newMessage = dinglerBio
            # if not a bot message then the new message is set to be sent out
        else:


        receivedMessage = 'From Server:'  + (receivedMessage)
        print(receivedMessage)
        for client in clients:
            if client[0] is not socketInput: #Don't send message back to the same person
                client[0].send(bytes(receivedMessage, 'utf-8'))

#Get the server port as command line argument
#check if sys.argv is 2
#sys.exit(-1)
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
print('IP: '+socket.gethostbyname(socket.gethostname())+' Port: '+str(sys.argv[1]))

clients = []

#This loop is looking for new connections
#If there is a new connection a socket is created and added to the clients array
while 1:
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))
    # This creates the thread for user input
    _thread.start_new_thread(newClientConnection, (connectionSocket,))

