
import sys,  select,random,datetime
from socket import *


     




MAX_CLIENTS = str(sys.argv[1])

MAX_CLIENTS=int(MAX_CLIENTS)
print(MAX_CLIENTS)
#setup socket to wait for connections
serverPort = str(sys.argv[2])
serverPort=int(serverPort)
print(serverPort)
serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(MAX_CLIENTS)
#just to make sure that the server is ready
print('The server is ready to accept clients')


clients = []
#these are all the Star Wars Jokes that will be in a list for the servr to choose from when a client asks for a joke
starWarsJokes=[]
starWarsJokes.append("Server Star Wars Joke:\nJabba the Hut is fat.\nHow fat is he?\nSo fat, Obi Wan took a closer look and said, “That’s no moon.”")
starWarsJokes.append("Server Star Wars Joke:\nWhat kind of car does a Jedi drive?\nA Toy Yoda.")
starWarsJokes.append("Server Star Wars Joke:\nWhich program do Jedi use to open PDF files in Star Wars?\nAdobe-Wan Kenobi!")
starWarsJokes.append("Server Star Wars Joke:\nWhy was the droid angry?\nPeople kept pushing its buttons.")
starWarsJokes.append("Server Star Wars Joke:\nWhat is Jabba the Hutt’s middle name?\nI don’t remember.\nThe.\n")
#this is the string then client asks for Dingler's bio 
dinglerBio= "Server Dingler Bio:\nDr Dingler born as dark now as light\nTo this day he lives under Yoda's bed\n"
dinglerBio= dinglerBio+"His favorite fruit is Naboo Floating Pears.\nHis favorite catch phrase is,\"skfjs totally wizard!\"\nHe also hates Sand"
#accept up to two connections from clients, which
# must connect before we can move on
masssage=' '
newMessage=' '

#this for loop will be getting the number of clients set connected to the server, which is specified by user
# for i in range(0,MAX_CLIENTS):
#     connectionSocket, addr = serverSocket.accept()
#     clients.append((connectionSocket,addr))
#     num=str(i)

#
for i in range(0, MAX_CLIENTS):
    clients[i][0].send(bytes(str(i), 'utf-8'))

#########################################
####this sends the number of clients ####
#########################################
for i in range(0, MAX_CLIENTS):
    clients[i][0].send(bytes(str(MAX_CLIENTS), 'utf-8'))


while 1:
    #loops through each client
    for i in range(MAX_CLIENTS):
        currClient=str(i)
        #loops to all the clients who's turn it is
        p=0
        for p in range(0,MAX_CLIENTS):
            print(currClient)
            print(p)
            clients[p][0].sendall(currClient.encode('utf-8'))
        #recieves a message from the current client
        message=clients[i][0].recv(1024).decode('utf-8')
        
        #checks to see if the message is a bot message 
        #bot message then the new message is set accordingly
        if message == "!bot tell me a Star Wars joke":
            jokeNum=random.randrange(0,5,1)
            newMessage=starWarsJokes[jokeNum]
        elif message=="!bot tell me the time":
            newMessage=str(datetime.datetime.now())
        elif message=="!bot show me Dingler's Bio":
            newMessage=dinglerBio
        #if not a bot message then the new message is set to be sent out 
        else:
           
            #withouth this the number is included with the number
            newMessage= "From client "+str(i)+": "+message
        #sends out the new 
     
        for k in range(0,MAX_CLIENTS):
            print(newMessage)
            clients[k][0].sendall(newMessage.encode('utf-8'))
    
    
           
    