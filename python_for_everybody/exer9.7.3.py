#Exercise 3     Write a program to read through a mail log, build a histogram using
#               a dictionary to count how many messages have come from each email
#               address, and print the dictionary.

fname = input('Enter a file name: ')
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
    word = line.split()
    try:
        emailAddressCount[word[1]] = emailAddressCount.get(word[1],0) + 1
        #count the times of email address appears,word[1] is a email address
    except:
        continue

print(emailAddressCount)
