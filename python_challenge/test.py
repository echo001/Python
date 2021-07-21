from PIL import Image
import re

im = Image.open('D:/test/Code/python_challenge/data/oxygen.png')
y = 45
row = im.crop(box)
#you will get x-coordinate which are 9 numbers .
getpix_x = gameaddr = ''
for i in range( 0, 608, 7):
    getpix = im.getpixel((i,y))
    getpix_x = getpix_x + chr(getpix[0])
print(getpix_x)

getpix_x = re.findall('the next level is \[(.*)\]',getpix_x)
getpix_x = ''.join(getpix_x)
getpix_x = getpix_x.split(',')
for x in getpix_x:
    gameaddr = gameaddr + chr(int(x))
    y = y + 1
print(gameaddr)
im.close()
