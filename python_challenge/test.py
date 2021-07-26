#Hint: odd even
#Hint: cave.jpg
#Hint: two picture are overlapped,so separate can get right answer
from PIL import Image, ImageDraw
im = Image.open('D:/test/Code/python_challenge/data/cave.jpg')
#print(im.size) (640,480)
im_new = Image.new('RGB',(640,480))

for x in range(im.size[0]):
    for y in range(im.size[1]):
        im_pixel = im.getpixel((x,y))
        im_new.putpixel((x//2,y//2),im_pixel)
im_new.save('D:/test/Code/python_challenge/data/cave1.jpg','JPEG')
