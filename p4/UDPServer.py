# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Generate randome number in the range of 0 and 49
    rand = random.randint(0, 49)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()

    # If rand is less than 18, we consider the packet lost and do not respond
    if rand < 18:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)