import socket
import re

userUrl = 'www.pythonchallenge.com'

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((userUrl,80))
title = 'GET http://www.pythonchallenge.com/pc/def/equality.html HTTP/1.0\r\n\r\n'
mysock.send(title.encode())

doc = ''
while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        mysock.close()
        break
    doc = doc + data.decode()

pos = doc.find('<!--')
doc = doc[pos+4:-4]
gameaddr = re.findall('.*[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z].*',doc)
#find the character which left is just three upper character,and the right is the same
gameaddr = ''.join(gameaddr)
print(gameaddr)
