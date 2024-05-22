import socket

serverName = "localhost"
serverPort = 4536

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message_to_send = input('What would you like to say?: ')
    clientSocket.sendto(message_to_send.encode())
    if message_to_send == 'stop':
        clientSocket.close()
