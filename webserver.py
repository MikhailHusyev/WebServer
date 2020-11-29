#import socket module
from socket import *
import sys # In order to terminate the program
import threading #For multi threading
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 7080
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection print('Ready to serve...') connectionSocket, addr = try:
    #Fill in start
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    #Added try portion down here
    try:
        #Fill in end
        message = connectionSocket.recv(1024) 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        header_OK = 'HTTP/1.1 200 OK \n'
        header_content_type = 'Content-Type: text/html \n'
        header_length = 'Content-Length: %d\n\n' % (len(outputdata))
        header = header_OK + header_content_type + header_length 
        connectionSocket.send(header)
        #Fill in end
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close() 
    except IOError:
        #Send response message for file not found
        #Fill in start

        connectionSocket.send("HTTP/1.1 404 Not Found ")
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data