# Extract URL from website
import urllib.request, urllib.parse, urllib.error
import re

userUrl = input('Enter a URL: ')
urlsplit = userUrl.split('/')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
req = urllib.request.Request(url=userUrl, headers=headers)
fhand = urllib.request.urlopen(req).read()
#except:
#    print('Can not connect this URL,please try again. ')
#    exit()
docUrl = dict()
count = 0
#links = re.findall(b'href="(http://.*?)"',fhand)
links = re.findall(b'"(https://.*?)"',fhand)
links = links + re.findall(b'"(/.*?)"',fhand)
for line in links:
    line = line.decode()
    if line.startswith('http'):
        docUrl[line] = docUrl.get(line,0) + 1
    else:
        line = urlsplit[0] + '//' + urlsplit[2] + line
        docUrl[line] = docUrl.get(line,0) + 1
for url in docUrl:
    print(url)
