
import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user_input = raw_input('Enter URL : ')
url = user_input.split('/')		#use split to break the url

try:
	mysock.connect((url[2],80))		#extract the host name for the socket connect call
	mysock.send('GET ' + user_input + ' HTTP/1.0\n\n')

	while True:
		data = mysock.recv(512)
		if (len(data) < 1 ):
			break
		print(data)

	mysock.close()
except:
	print('Error input,please check the url')
