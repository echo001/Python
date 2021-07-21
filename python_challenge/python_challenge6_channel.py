#the answer is from channel.zip,download and read readme file
#the readme file shows :collect the comments.
#must use zipfile.getinfo to collect comments which are not appearing by opening files directly
import re
import zipfile

the_zip = zipfile.ZipFile('D:/test/Code/python_challenge/data/channel.zip')
comments = []

def open_txt(filename):
    handle = the_zip.open(filename)
    data = handle.read().decode()
    comments.append(the_zip.getinfo(filename).comment.decode())
    if data.find('nothing') > 0:
        nextnum = re.findall('.*nothing is (.*)',data)
    else:
        nextnum = ''
        print(data)
    handle.close()
    return nextnum


nextnum = open_txt('90052.txt')
count = 0
while True:
    if nextnum == '':
        break
    nextnum = open_txt(''.join(nextnum) + '.txt')
    count += 1
'''
for comment in comments:
    print(comment)
'''
for comment in comments:
    print(comment,end="")
    #'\n' is always exited in comments,so should not wrap the output
