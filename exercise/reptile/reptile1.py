#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
import string
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)

url = 'https://proxy.ip3366.net/free/?action=china&page=1'
def ip_port(url):
    s = requests.session()
    s.keep_alive = False    #防止http连接过多
    response = requests.get(url)
    text = response.text

    IP = re.findall('.IP">(.*?)</td>',text)
    PORT = re.findall('.PORT">(.*?)</td>',text)
    doc = []
    for i in range(0,len(IP)):
        doc.append(IP[i]+':'+PORT[i])
    return doc

if __name__ == '__main__':
    url = 'https://proxy.ip3366.net/free/?action=china&page=1'
    urlsplit = url.split('=')
    f = open('D:/test/Code/exercise/reptile/data/reptile1.txt','w')
    while True:
        doc = ip_port(url)
        for line in doc:
            f.write(line+'\n')
        if len(doc) == 0:
            break
        urlsplit[2] = int(urlsplit[2])
        urlsplit[2] += 1
        url = urlsplit[0] + urlsplit[1] + '=' + str(urlsplit[2])
        print(url)
    f.close()
