#use lxml or beautifulsoap

from io import BytesIO
from lxml import etree
import requests

url = 'https://nostarch.com'
response = requests.get(url)
content = response.content  #get bytes

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)
#BytesIO is used to read bytes in memory
for link in content.findall('//a'): #all a anchor
#    print(link)
    print(f"{link.get('href')} -> {link.text}")
    #print a anchor contents like <a href="...">text</a>
