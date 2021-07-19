#Exercise 4     Change the urllinks.py program to extract and count paragraph (p)
#               tags from the retrieved HTML document and display the count of the
#               paragraphs as the output of your program. Do not display the paragraph
#               text, only count them. Test your program on several small web pages as
#               well as some larger web pages.
import urllib.request, urllib.parse, urllib.error
import bs4
from bs4 import BeautifulSoup
import ssl

#Ignore SSL cetificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL you want to count : ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
count = 0
for tag in tags:
    count += 1
print('The p tags in this html appears %d times. ' % count)
