#Exercise 2     Write a program that categorizes each mail message by which day of
#               the week the commit was done. To do this look for lines that start
#               with “From”, then look for the third word and keep a running count
#               of each of the days of the week. At the end of the program print
#               out the contents of your dictionary (order does not matter)

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('This file can not be opened.')
daycount = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    word = line.split()
    try:
        daycount[word[2]] = daycount.get(word[2],0) + 1
    except:
        continue

print(daycount)
