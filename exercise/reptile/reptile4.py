#url:http://proxylist.fatezero.org/proxy.list
import requests
import re
import string
import time

def ip_port(url):
    s = requests.session()
    s.keep_alive = False    #防止http连接过多
    response = requests.get(url)
    text = response.text
    IP = re.findall('"host": "(.*?)".*',text)
    PORT = re.findall('"port": ([0-9.]*)',text)
    doc = []
    for (ip,port) in zip(IP,PORT):  #同时对两个list进行遍历，且一一对应关系
        doc.append(ip + ':' + port)
    return doc

if __name__ == '__main__':
    url = 'http://proxylist.fatezero.org/proxy.list'
    f = open('D:/test/Code/exercise/reptile/data/reptile4.txt','w')
    doc = ip_port(url)
    for line in doc:
        f.write(line+'\n')
        print(line)
    f.close()
