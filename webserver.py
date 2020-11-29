# Project: WebServer
# Group: Wednesday Group 2
# Group Members: Mikhail Husyev, Victoria Kondratenko, Andriy Usyk
# Bonus Points: We did multithreading portion for bonus

#import socket module
from socket import *
from _thread import *
import sys # In order to terminate the program
import threading #For threading 
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 7090
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
#Fill in end

# Threading Start
lock = threading.Lock()
# Threading End
lock.acquire

def multi_threading(connectionSocket, outputdata):
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.send("\r\n".encode())
    connectionSocket.close() 

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
        # Threading Start
        start_new_thread(multi_threading, (connectionSocket, outputdata))
        # Threading End
    except IOError:
        #Send response message for file not found
        #Fill in start
        header_not_found = 'HTTP/1.1 404 Not Found \n'
        header_content_type = 'Content-Type: text/html \n'
        header_content = '<html><body><h1>Sorry we were unable to find your request.</h1></body></html>'
        header_length = 'Content-Length: %d\n\n' % (len(header_content))
        header = header_not_found + header_content_type + header_length + header_content
        connectionSocket.send(header)
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
        # Threading release lock

lock.release()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data