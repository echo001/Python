#Hint:a = [1, 11, 21, 1211, 111221,
#Hint:a[30] = ?     ——>subscript is from a[1] not from a[0]
#a1 = 1         1 of number 1
#a2 = 11        2 of number 1
#a3 = 21        1 of number 2,1 of number 1
#a4 = 1211      1 of number 1,1 of number 2,2 of number 1
#a5 = 111221    3 of number 1,2 of number 2,1 of number 1
#a6 = ?   ——>   312211

import string
def number_get(a):
    doc = ''
    count = 1
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
    return doc

if __name__ == '__main__':
    a = '1'
    for num in range(30):   #why there is 30, can look line 2 Hint
        a = number_get(a)
    print(len(a))
