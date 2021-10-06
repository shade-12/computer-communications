"""
Problem 3

TCP Server Requirements:

(1) Create a connect socket when contacted by the TCP client
(2) Receive the string variable sent by the TCP client
(3) Generate a reward based on the string variable sent by the TCP client
(4) Inform the TCP client about the reward by sending a response over the 
    TCP connection to the TCP client

"""

from socket import *

serverName = gethostname()  # Use local server name
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print('The server is ready to receive ...')

while True:
    # (1) Create a connect socket when contacted by the TCP client
    connectionSocket, addr = serverSocket.accept()

    # (2) Receive the string variable sent by the TCP client
    sentence = connectionSocket.recv(1024).decode()

    # (3) Generate a reward based on the string variable sent by the TCP client
    rewardScore = {
        'A': 3,
        'B': 2,
        'C': 1
    }
    reward = rewardScore.get(sentence, -1)

    # (4) Inform the TCP client about the reward by sending a response over the 
    #     TCP connection to the TCP client
    connectionSocket.send(str(reward).encode())

    connectionSocket.close()