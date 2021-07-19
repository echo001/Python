#Exercise 3     Use urllib to replicate the previous exercise of () retrieving the
#               document from a URL, () displaying up to 3000 characters, and ()
#               counting the overall number of characters in the document. Don’t worry
#               about the headers for this exercise, simply show the first 3000
#               characters of the document contents.
import urllib.request, urllib.parse, urllib.error
userUrl = input('Enter a url: ')
try:
    fhand = urllib.request.urlopen(userUrl).read()
except:
    print('Can not connect this URL,please try agin.')
    exit()
doc = ''
count = 0
for line in fhand:
    if line is None:
        break
    count = count + line
    doc = doc + line
pos = doc.find('\r\n\r\n')
print(doc[pos+4:3005])
print(count)
