#GET data
import urllib.request, urllib.parse

URL = 'https://www.nostarch.com'
'''
headers = {'User-Agent': "Googlebot"}

request = urllib.request.Request(URL, headers=headers)
response = urllib.request.urlopen(request)

print(response.read())
response.close()
'''
with urllib.request.urlopen(URL) as response:
    content = response.read()
print(content)
