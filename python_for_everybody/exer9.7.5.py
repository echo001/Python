#Exercise 5     This program records the domain name (instead of the address) where
#               the message was sent from instead of who the mail came from (i.e.,
#               the whole email address).At the end of the program, print out the
#               contents of your dictionary

fname = input('Enter a file name : ')
try:
    fhand = open(fname)
except:
    print('This file can not be opened. ')
    exit()
emailAddressCount = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    wholeaddress = line.split()
    word = wholeaddress[1].split('@')
    try:
        emailAddressCount[word[1]] = emailAddressCount.get(word[1],0) + 1
        #count the times of email address appears,word[1] is a email address
    except:
        continue

print(emailAddressCount)
