import json
import socket

PORT = 4536
IP = 'localHost'
webcamData = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(2048)
    print(data, addr)
    data.decode()
    print(data)
    webcamData.append(data)

    message = input('What would you like to respond?') + str(webcamData)

    sock.send(message.encode())

