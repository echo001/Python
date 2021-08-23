#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
import time
import xlwt #输出到xlsx文件
import pandas as pd
from lxml import etree
from io import BytesIO
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)

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
    time.sleep(5)   #延迟访问，该站访问频率过高将不返回查询结果
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
            business = None
#    print(addr,business)
    return addr,business

def ip_port(url):   #爬取代理IP
    content = url_request(url)
    doc = dict()
    for (ip,port) in zip(content.findall('//td[1]'),content.findall('//td[2]')): #同时对ip，port遍历，list类型
        IP = ip.text
        PORT = port.text
        (addr,business) = verify(IP)
        print(IP)
        doc = {'IP': IP, 'Port': PORT, '地址': addr, '运营商': business}
        print(doc)
        export_excel(doc)
    return 0

def export_excel(doc):
    pf = pd.DataFrame(doc)
    order = ['IP', 'Port', '地址', '运营商'] #指定输出字段顺序
    pf = pf[order]
    columns = {
    'IP':'IP',
    'Port':'端口',
    '地址':'地址',
    '运营商':'运营商'
    }
    pf.rename(columns=columns)
    file_path = pd.ExcelWriter('D:/test/Code/exercise/reptile/data/reptile_verify.xlsx')
    pf.fillna(' ', inplace=True)    #替换空单元格
    pf.to_excel(file_path, encoding='utf-8', index=False)
    file_path.save()

if __name__ == '__main__':
    url = 'https://proxy.ip3366.net/free/?action=china&page=1'
    data = ip_port(url)
