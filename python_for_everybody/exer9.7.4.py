#Exercise 4     Add code to the above program to figure out who has the most messages
#               in the file.After all the data has been read and the dictionary has
#               been created, look through the dictionary using a maximum loop
#               (see Section [maximumloop]) to find who has the most messages and
#               print how many messages the person has.

fname = input('Enter a file name : ')
try:
    fhand = open(fname)
except:
    print('This file can not be opened! ')
    exit()
emailAddressCount = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    word = line.split()
    try:
        emailAddressCount[word[1]] = emailAddressCount.get(word[1],0) + 1
        #count the times of email address appears,word[1] is a email address
    except:
        continue
valist = emailAddressCount.values()
maxvalue = max(valist)      #count the maximum of email address
for key in emailAddressCount:
    if maxvalue == emailAddressCount[key]:
        print(key,maxvalue)
