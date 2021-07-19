#Exercise 5 : Use find function and string slicing to extract the portion of the
#             string after the colon character.Then use the float function to
#             convert the string into floating point number.
#             The Strings:"str = 'X-DSPAM-Confidence:0.8475'"

word = 'X-DSPAM-Confidence:0.8475'
stpos = word.find(":")
despos = word.find("'")
num = word[stpos+1:despos]
print('The floating point number is : %s' % float(num))
