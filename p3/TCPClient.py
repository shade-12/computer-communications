"""
Problem 3

TCP Client Requirements:

(1) Collects a string variable from the keyboard input
(2) Send the string variable to the TCP server
(3) Receive the response from the TCP server over the TCP connection

"""

from socket import *

serverName = gethostname()  # Use local server name
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# (1) Collects a string variable from the keyboard input
sentence = input('Enter your input: \n')

# (2) Send the string variable to the TCP server
clientSocket.send(sentence.encode())

# (3) Receive the response from the TCP server over the TCP connection
reward = clientSocket.recv(1024)
print('Reward received: ', reward.decode())

clientSocket.close()