import socket
import json
import threading

serverPort = 55772
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind(('', serverPort))
ServerSocket.listen(1)

def Handle_Client(connectionSocket, addr):
    print(addr)
    print('Server is ready to listen')
    Communicate = True
    while Communicate:
        jsonSentence = connectionSocket.recv(1024).decode()
        webcams = json.loads(jsonSentence)
        print(webcams)
        print("Is the webcam in 16/9 format?")
        if int(webcams["Height"])/9 == int(webcams["Width"])/16:
            message = "Is 16/9"
            connectionSocket.send(message.encode())
        else:
            message = "Is Not 16/9"
            connectionSocket.send(message.encode())

while True:
    connectionSocket, addr = ServerSocket.accept()
    threading.Thread(target=Handle_Client, args=(connectionSocket, addr)).start()

#{"Id":1, "Brand": "Logitech", "Height": 1080, "Width":1920 }


