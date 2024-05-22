import json
import socket

ServerPort = 55772

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', ServerPort))
webcamDict = {"Id": int(input('Id: ')), "Brand": input('Brand Name: '), "Height": int(input('Height: ')),
              "Width": int(input('Width: '))}

webcamJson = json.dumps(webcamDict)
sock.send(webcamJson.encode())
returned_message = sock.recv(1024).decode()
print(returned_message)