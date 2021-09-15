#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
import time
import peewee
from peewee import *
from lxml import etree
from io import BytesIO
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)
#数据库设定，reptile数据库名，如果没有，需要进入mysql自建一个
db = MySQLDatabase('reptile', host='127.0.0.1', user='root', passwd='Zpepc001@', port=3306)
db.connect()    #数据库连接
print(db.is_closed())   #判断数据库是不是链接好

class BaseModel(Model):
    class Meta:
        database = db
class Person(BaseModel):
    IP = CharField(verbose_name='IP', max_length=20, null=False, index=True)
    Port = CharField(verbose_name='Port', max_length=10, null=False)
    Address = CharField(verbose_name='地址', max_length=20)
    Business = CharField(verbose_name='运营商', max_length=20)
    class Meta:
        primary_key = CompositeKey('IP', 'Port')
#db.create_tables([Person]) 只需运行一次，已经创建好名为person的表

def store_data(data):   #存储数据到mysql数据库
    try:    #联合主键设置，IP,Port数据一样时，插入数据产生报错
        Person.insert_many(data).execute()  #插入数据
    except:
        print('------data repetition------')

def url_request(url, headers=None): #连接
    s = requests.session()
    s.keep_alive = False    #防止http连接过多
    response = requests.get(url, headers=headers)
    content = response.content
    parser = etree.HTMLParser() #网页处理
    content = etree.parse(BytesIO(content), parser=parser)
    return content

def verify(ip): #查询地址及运营商
    url = 'http://www.cip.cc/' + ip
    headers = {
    'Host': 'www.cip.cc',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    time.sleep(6)   #延迟访问，该站访问频率过高将不返回查询结果
    content = url_request(url, headers=headers)    #没有headers会报502网关错误
    data = ''
    addr = business = ''
    for address in content.findall('//pre'):
        data = address.text
        if re.findall('运营商',data):
            addr = re.findall(r'\s*地址\s*: (.*?)[.\n]*运营商',data)
            business = re.findall(r'\s*运营商\s*: (.*?)[.\n]*数据二',data)
        else:
            addr = re.findall(r'\s*地址\s*: (.*?)[.\n]*数据二',data)
            business = ''
#    print(addr,business)
    return addr,business

def ip_port(url):   #爬取代理IP,count是条数计数，便于excel数据行插入
    content = url_request(url)
    doc = []
    for (ip,port) in zip(content.findall('//td[1]'),content.findall('//td[2]')): #同时对ip，port遍历，list类型
        IP = ip.text
        PORT = port.text
        (addr,business) = verify(IP)    #查询地址以及运营商
#        print(IP)
        doc = [{'IP': IP, 'Port': PORT, 'Address': addr, 'Business': business}]
#        count += 1
        print(doc)
        store_data(doc)
#    return count

if __name__ == '__main__':
    url = 'https://proxy.ip3366.net/free/?action=china&page=1'
    urlsplit = url.split('=')
    for i in range(0,481):  #代理页面有481页，循环481次读取
        ip_port(url)
        urlsplit[2] = int(urlsplit[2])
        urlsplit[2] += 1
        url = urlsplit[0] + urlsplit[1] + '=' + str(urlsplit[2])
        print(url)
