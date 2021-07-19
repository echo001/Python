#Exercise 5     (Advanced) Change the socket program so that it only shows data after
#               the headers and a blank line have been received. Remember that recv is
#               receiving characters (newlines and all), not lines.
import socket
import ssl

userUrl = input('Enter a URL : ')
try:
    urlsplit = userUrl.split('/')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((urlsplit[2], 80))
    title = 'GET ' + userUrl + ' HTTP/1.0\r\n\r\n'
    print(title)
    cmd = title.encode()
    mysock.send(cmd)
except:
    print(' url connect error. please check and try again')
    exit()
doc = ''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    doc = doc + data.decode()
mysock.close()
pos = doc.find('\r\n\r\n')
print(doc[pos+4:])
