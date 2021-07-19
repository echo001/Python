#Exercise 1     Write a program that reads the words in words.txt and stores them as
#               keys in a dictionary. It doesn’t matter what the values are. Then you
#               can use the in operator as a fast way to check whether a string is
#               in the dictionary.

fname = input('Enter a file name : ')
try:
    fhand = open(fname)
except:
    print('Ther is no this file %s ' % fname)
    exit()
word = dict()
for line in fhand:
    line = line.rstrip()
#    if line not in word:
#        word[line] = 1
#    else:
#        word[line] = word[line] + 1  #count how many times the same word appear
    word[line] = word.get(line,0) + 1   # the same as if....  else...
print(word)
