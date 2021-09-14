#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
import time
import pandas as pd
import peewee
from io import BytesIO
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)
#数据库设定
settings = {'host':'localhost', 'password':'Zpepc001@', 'port':3306, 'user':'root'}
db = peewee.MySQLDatabase("test", **settings)

class Person(Model):
    ip = charField(verbost_name='IP', max_length=20, null=False, index=True)
    port = charField(verbose_name='Port', max_length=10, null=False)
    address = charField(verbose_name='地址', max_length=20)
    business = charField(verbose_name='运营商', max_length=20)
    class Meta:
        database = db   #建立数据库链接
        table_name = 'proxyip'
db.connect()    #数据库连接
print(db.is_closed())   #判断数据库是不是链接好


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

def ip_port(url, count):   #爬取代理IP,count是条数计数，便于excel数据行插入
    content = url_request(url)
    doc = []
    for (ip,port) in zip(content.findall('//td[1]'),content.findall('//td[2]')): #同时对ip，port遍历，list类型
        IP = ip.text
        PORT = port.text
        (addr,business) = verify(IP)    #查询地址以及运营商
#        print(IP)
        doc = [{'IP': IP, 'Port': PORT, '地址': addr, '运营商': business}]
        count += 1
        print(doc)
        export_excel(doc, count)
    return count

def export_excel(doc, i):   #输出到excel文件，i表示行
    file_path = 'D:/test/Code/exercise/reptile/data/reptile_verify.xlsx'
    ws = openpyxl.load_workbook(filename=file_path, data_only=True)
    excel_sheet = ws.worksheets[0]
    ws1 = ws.active
    for column in range(1,5):
        ws1.cell(column=1, row=i).value = doc[0]['IP']
        ws1.cell(column=2, row=i).value = doc[0]['Port']
        ws1.cell(column=3, row=i).value = ''.join(doc[0]['地址']) #数据列表转成字符串
        ws1.cell(column=4, row=i).value = ''.join(doc[0]['运营商'])
    ws.save(filename=file_path)

if __name__ == '__main__':
    url = 'https://proxy.ip3366.net/free/?action=china&page=140'
    urlsplit = url.split('=')
    count = 1180
    for i in range(140,481):  #代理页面有481页，循环481次读取
        count = ip_port(url, count)
        urlsplit[2] = int(urlsplit[2])
        urlsplit[2] += 1
        url = urlsplit[0] + urlsplit[1] + '=' + str(urlsplit[2])
        print(url)
