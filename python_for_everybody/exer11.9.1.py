#Exercise 1     Write a simple program to simulate the operation of the grep command
#               on Unix. Ask the user to enter a regular expression and count the number
#               of lines that matched the regular expression:
import re
reInput = input('Enter a regular expression: ')
try:
    fhand = open('mbox.txt')
except:
    print('mbox.txt is not existed. ')
    exit()
count = 0
for line in fhand:
    if re.search(reInput,line):
        count += 1
print('mbox.txt had %s lines that matched %s ' % (count,reInput))
