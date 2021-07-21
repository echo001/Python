#from the last one , will get word 'hockey',but this is not right word.
#when open 'http://www.pythonchallenge.com/pc/def/hockey.html',you should get
#   look at the letters. so coming back the last one will find 'hockey'
#   formulated by 'oxygen'

from PIL import Image
import re

im = Image.open('D:/test/Code/python_challenge/data/oxygen.png')
y = 45 # the number is from 43 to 51 ,all could get right answer
#you will get x-coordinate which are 9 numbers .
getpix_x = gameaddr = ''
step = 7 # the small block's gap is 7 pixel.
for i in range( 0, 608, step):
    getpix = im.getpixel((i,y))
    getpix_x = getpix_x + chr(getpix[0])
print(getpix_x)
#extract the 9 numbers ,and these are transforming to ascii string by using chr()
getpix_x = re.findall('the next level is \[(.*)\]',getpix_x)
getpix_x = ''.join(getpix_x)
getpix_x = getpix_x.split(',')
for x in getpix_x:
    gameaddr = gameaddr + chr(int(x))
print(gameaddr)
im.close()
