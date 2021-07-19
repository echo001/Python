#Exercise 2     Write a program to look for lines of the form and extract the number
#               from each of the lines using a regular expression and the findall()
#               method. Compute the average of the numbers and print out the average.
import re
fname = input('Enter file: ')
try:
    fhand = open(fname)
except:
    print('This file is not existed. ')
    exit()
numList = list()
total = i = 0
for line in fhand:
#    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9.]+)',line)  #return a list with one element
    if len(num) > 0 :
        numList = numList + num
for i in range(len(numList)):
    total = total + float(numList[i])
print((total/(i+1)))    # i is begin from zero,so the count of the numList numbers
                        #should add 1
