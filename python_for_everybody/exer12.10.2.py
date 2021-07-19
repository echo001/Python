#Exercise 2     Change your socket program so that it counts the number of characters
#               it has received and stops displaying any text after it has shown 3000
#               characters. The program should retrieve the entire document and count
#               the total number of characters and display the count of the number of
#               characters at the end of the document
import socket
userUrl = input('Enter a URL: ')
try:
    urlsplit = userUrl.split('/')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(urlsplit[2])
    mysock.connect((urlsplit[2],80))
    title = 'GET ' + userUrl + ' HTTP/1.0\r\n\r\n'
    print(title)
    cmd = title.encode()
    mysock.send(cmd)
except:
    print('URL input is wrong,please input right url like http://...')
    exit()
count = 0
doc = ''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    doc = doc + data.decode()
    count = count + len(data)
pos = doc.find("\r\n\r\n")  #pos+4 shows delete response title (HTTP 200 OK ..)
#print(doc[pos+4:3001])
print(doc[pos+4:3005])

print(count)
