#it can automatically handle cookies
import requests
url = 'http://boodelyboo.com'
response = requests.get(url)   #get

data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data)
print(response.text)   #receive string
 # if get byte string ,should use response.content
print(response.content)
