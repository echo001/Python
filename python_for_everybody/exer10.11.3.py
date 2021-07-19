#Exercise 3     Write a program that reads a file and prints the letters in
#               decreasing order of frequency. Your program should convert all the
#               input to lower case and only count the letters a-z. Your program
#               should not count spaces, digits, punctuation, or anything other than
#               the letters a-z. Find text samples from several different languages
#               and see how letter frequency varies between languages. Compare your
#               results with the tables at wikipedia.org/wiki/Letter_frequencies.
import string
fname = input('Enter a file name : ')
try:
    fhand = open(fname)
except:
    print('This file can not be opened. ')
    exit()
letterCount = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation)) #delete all punctuation
    linelist = line.lower()
    for letter in linelist:
        if letter.isdigit():    #delete all digit
            continue
        letterCount[letter] = letterCount.get(letter,0) + 1     #count letters from files
letterCountList = list(letterCount.items())
letterCountList.sort()      #sort letters from a to z
for letter,count in letterCountList:
    print(letter,count)
