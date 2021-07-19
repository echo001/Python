#download source data and find the rare characters
import socket
import string

url = 'www.pythonchallenge.com'

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((url,80))
title = 'GET http://www.pythonchallenge.com/pc/def/ocr.html HTTP/1.0\r\n\r\n'
cmd = title.encode()
mysock.send(cmd)

doc = gameaddr = ''
count = dict()
while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        break
    doc = doc + data.decode()

pos = doc.find('%%')
doc = doc[pos:]
for character in doc:
    count[character] = count.get(character,0) + 1

for character in count:
    if count[character] == 1 and character >= 'a' and character <= 'z':
        gameaddr = gameaddr + character
print(gameaddr)
