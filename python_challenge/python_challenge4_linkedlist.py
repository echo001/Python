#This game is to extract the number after 'nothing=...' and then connect again by
#using the new number
import socket
import re

def nothing_num(url):
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    urlsplit = url.split('/')
    mysock.connect((urlsplit[2],80))
    title = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    mysock.send(title.encode())

    doc = ''
    data = mysock.recv(1024)
    doc = doc + data.decode()
    mysock.close()
    pos = doc.find('\r\n\r\n')
    doc = doc[pos+4:]
    #There are two format when connect to get the number after 'nothing=...'
    if doc.find('href') > 0:
        link = re.findall('href=".*?nothing=(.*)"><img.*',doc)
    elif (doc.find('nothing') > 0):
        link = re.findall('.*and the next nothing is (.*)',doc)
    else:
        link =''    #when get no number ,maybe the next gameaddr is here
        print(doc)
    return link

userUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
link = nothing_num(userUrl)
count = 0
while True:
    if (count > 400):
        break
    userUrl2 = userUrl + '?nothing=' + ''.join(link)
    link = nothing_num(userUrl2)
    count += 1

#    print(link)
