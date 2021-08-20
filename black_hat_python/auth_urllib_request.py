#authentication
#POST data

import urllib.request, urllib.error, urllib.parse

URL = 'https://www.nostarch.com'
info = {'user': 'test', 'passwd': 'helloworld'}

data = urllib.parse.urlencode(info).encode()

req = urllib.request.Request(URL, data)
with urllib.request.urlopen(req) as response:
    content = response.read()
print(content)
