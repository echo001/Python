#url:http://api.89ip.cn/tqdl.html?api=1&num=9999&port=&address=&isp=
import requests
import re
import string
import time
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)
def ip_port(url):
    s = requests.session()
    s.keep_alive = False    #防止http连接过多
    response = requests.get(url)
    text = response.text
    data = re.findall('</script>[.\n]*(.*?)<br>',text)  #[.\n]* 匹配换行符
    data = data + re.findall('<br>(.*?)<br>',text)
    return data

if __name__ == '__main__':
    url = 'http://api.89ip.cn/tqdl.html?api=1&num=9999&port=&address=&isp='
    f = open('D:/test/Code/exercise/reptile/data/reptile3.txt','w')
    data = ip_port(url)
    for line in data:
        print(line)
        f.write(line+'\n')
    f.close()
