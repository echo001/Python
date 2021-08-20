import socket

IP = '127.0.0.1'
port = 9998

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((IP,port))
title = 'GET / HTTP/1.0\r\nHost: 127.0.0.1:9998\r\n\r\n'
mysock.send(title.encode())
#receive data
data = mysock.recv(1024)
print(data.decode())
mysock.close()
