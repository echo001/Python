# create a function called count,and capsulate the number of character like 'a',
# this function will receive string from user Input

def count(user_string,user_letter):
    counts = 0
    for letter in user_input:
        if letter == user_letter:
            counts += 1
    return counts
user_input = input('Enter strings : ')
user_letter = input('Enter a letter you want to count: ')
counts = count(user_input,user_letter)
print('The count of letter %s is %s '% (user_letter,counts))
