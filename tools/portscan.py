#scan port use tcp three hands protocal

import socket

mysock = socket.socket()
url = input('Enter a IP: ')
port = 1
for port in range(65535):
    print(port)
    mysock.connect((url,port))
    data = mysock.recv(1024)
    if len(data) < 1:
        mysock.close()
        port = port + 1
        print(port)
        continue
    print('%s port open ' % port)
    mysock.close()
    port = port + 1
    print(port)
