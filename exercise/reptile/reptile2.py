#url:http://www.ip3366.net/free/?stype=1&page=1
import requests
import re
import string
from bs4 import BeautifulSoup
#list > table > tbody > tr:nth-child(1) > td:nth-child(1)
#list > table > tbody > tr:nth-child(2) > td:nth-child(1)

def ip_port(url):
    s = requests.session()
    s.keep_alive = False    #防止http连接过多
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    IP = soup.select('#list > table > tbody > tr > td:nth-child(1)')    #得到<td>IP</td>的list
    PORT = soup.select('#list > table > tbody > tr > td:nth-child(2)')  #得到<td>PORT</td>的list
    doc = []
    for (ip,port) in zip(IP,PORT):  #同时对两个list进行遍历，将IP，PORT两个list的内容一一对应
        ip = ip.get_text()
        port = port.get_text()
        doc.append(ip+':'+port)
    return doc

if __name__ == '__main__':
    url = 'http://www.ip3366.net/free/?stype=1&page=1'
    urlsplit = url.split('=')
    f = open('D:/test/Code/exercise/reptile/data/reptile2.txt','w')
    while True:
        doc = ip_port(url)
        for line in doc:
#            print(line)
            f.write(line+'\n')
        if int(urlsplit[2]) > 7:
            break
        urlsplit[2] = int(urlsplit[2])
        urlsplit[2] += 1
        url = urlsplit[0] + urlsplit[1] + '=' + str(urlsplit[2])
        print(url)
    f.close()
