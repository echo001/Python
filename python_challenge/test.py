#Hint:a = [1, 11, 21, 1211, 111221,
#a1 = 1         1 of number 1
#a2 = 11        2 of number 1
#a3 = 21        1 of number 2,1 of number 1
#a4 = 1211      1 of number 1,1 of number 2,2 of number 1
#a5 = 111221    3 of number 1,2 of number 2,1 of number 1
#a6 = ?   ——>   312211

import string
a = '21'
a_dict = dict()
count = 1
doc = ''
for i in range(len(a)):
    if (i < len(a)-1):
        if( a[i] == a[i+1]):
            count += 1
        else:
            doc = doc + str(count) + a[i]
            count = 1
    else:
        if( a[i-1] == a[i]):
            doc = doc + str(count) + a[i]
        else:
            count = 1
            doc = doc + str(count) + a[i]
print(doc)
