Author:Quinton Cline
Files: server.py, client.py


Note: The server must be run before the client


INSTRUCTIONS:

##########################
##### 	 SERVER	  ########
##########################
	1.Run the server using the command line with "python server.py [port number] "
	2.The server must have the port number as a command line argument
	

##########################
##### 	 CLIENT   ########
##########################
	1. Run the client using the command line with "python client.py [server ip] [server port]"
	2. The client will get a response from the server that it is connected.
	3. The user can input a message at any time and hit enter to send the message to the other clients.
	4. The message from other clients will appear automatically.
	6. Get a response from the bot using "!bot joke" and "!bot time".

FEATURES:
	Client:
		- User input of the server ip and port
			Acomplished using command line arguments and grabing those with the sys.argv
		- User can receive messages or send message at any time	
			Accomplished using a thread for getting user input and sending to server
		- User can use !bot to talk to different bots
			Accomplished on server side, see below
	
	Server:
		-Allow any number of clients to connect at any time	
			Acomplished using a while loop that waits for new clients to connect
			A new thread is created for each client socket that connects
			This thread allows all the clients to talk to the server at any time
		-Process desired server port at startup and display port and ip when server is running
			Accomplished by printing input server port and by using socket.gethostbyname()
		-Server side bot
			Accomplished by looking for !bot [keyword] then outputing the client that sent the message 
		-Displays the connected users ip adress on server console
			Accomplished by printing out the created sockets ip adress

TESTING:
	Tested on Windows 10 using python 3.7 through the command promt. The server was firtst run as shown above.
	Then three clients were launched using the instructions. The clients were able to talk to eachother at any time.
	The clients were also able to get a response from the bot using "!bot joke" and "!bot time". 
	
	
