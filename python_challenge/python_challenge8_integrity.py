# Hint: 'BZh91AY&SY' means bz2 compress file
import bz2
import socket
import codecs
import re

def decrypt_word(words):
    #translate list to string and then translate to bytes
    words = ''.join(words).encode('utf-8')
    #forbid to escape slash character,like '\\' to '\'
    words = codecs.escape_decode(words,'hex-escape')
    words = bz2.decompress(words[0]).decode()
    return words

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
urlsplit = url.split('/')
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((urlsplit[2],80))
title = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
mysock.send(title.encode())

doc = ''
while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        mysock.close()
        break
    doc = doc + data.decode()
un = re.findall(".*un: '(.*)'",doc)
pw = re.findall(".*pw: '(.*)'",doc)
un = decrypt_word(un)
pw = decrypt_word(pw)
print(un)  
print(pw)
