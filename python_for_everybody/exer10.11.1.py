#Exercise 1     Revise a previous program as follows: Read and parse the“From” lines
#               and pull out the addresses from the line. Count the number of
#               messages from each person using a dictionary.
#               After all the data has been read, print the person with the most
#               commits by creating a list of (count, email) tuples from the
#               dictionary. Then sort the list in reverse order and print out the
#               person who has the most commits.

# like 9.7.4.py but should use (sort) to do the same thing
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
    word = line.split()
    try:
        emailAddressCount[word[1]] = emailAddressCount.get(word[1],0) + 1
    except:
        continue
countEmail = list()
for key,value  in list(emailAddressCount.items()):
    countEmail.append((value,key))    #create list to store (count,email)
countEmail.sort(reverse=True)
for count,email in countEmail[:1]:
    print(email,count)
