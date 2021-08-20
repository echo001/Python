#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
from lxml import etree
from io import BytesIO
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)

url = 'https://proxy.ip3366.net/free/?action=china&page=1'

s = requests.session()
s.keep_alive = False    #防止http连接过多
response = requests.get(url)
content = response.content

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)
doc = dict()
for ip in content.findall('//td[1]'):
    IP = ip.text
for port in content.findall('//td[2]'):
    PORT = port.text
