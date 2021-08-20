import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    stdin, stdout, stderr = client.exec_command(cmd)
    output = stout.readlines() + stderr.radlines()

    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()  #enter a password will not be echoed

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port: ') or 22
    cmd = input('Enter command: ')
    ssh_command(ip, port, user, password, cmd)
