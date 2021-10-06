"""
Problem 4(b)

UDP Client Requirements:

(1) Send 20 ping ping messages using UDP to the server
(2) Wait up to 2s for a reply; if no reply is received within 2s, assume that the packet was lost
    and print "Request timed out"
(3) Print the response message from server, if any
(4) Calculate and print the round trip time (RTT), in seconds, of each packet, if server responses

"""

from socket import *
import time

serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

# (1) Send 20 ping ping messages using UDP to the server
for i in range(1, 21):

    start = time.time()
    message = f"Ping {str(i)} {time.ctime(start)}"
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    try:
        # (2) Wait up to 2s for a reply; if no reply is received within 2s, assume 
        #     that the packet was lost and print "Request timed out"
        clientSocket.settimeout(2.0)

        receivedMessage, serverAddress = clientSocket.recvfrom(1024)
        end = time.time()

        if len(receivedMessage) is not None:
            # (3) Print the response message from server, if any
            print(f"Received Message: {receivedMessage.decode()}")
            # Calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
            print(f"RTT: {end - start}\n")
        else:
            print("Request timed out\n")

    except:
        print("Request timed out\n")

clientSocket.close()