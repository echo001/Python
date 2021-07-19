# Exercise 4  : use the string function called count which is existed at
#               https://docs.python.org/3.5/library/stdtypes.html#string-methods.
#               This function is similar to the function in the previous 6.3 exercise
#               Write an invocation that counts the number of times the letter
#               a occurs in 'banana'

user_input = input('Enter strings you want to count: ')
counts = user_input.strip().count('banana')
print("The number of times the letter a occurs in 'banana' is : %d" % counts)
