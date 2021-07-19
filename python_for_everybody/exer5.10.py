#Exercise 1   Write a program which repeatedly reads numbers until the user enters
#             “done”. Once “done” is entered, print out the total, count, and
#             average of the numbers. If the user enters anything other than a number
#             , detect their mistake using try and except and print an error
#             message and skip to the next number

total = count = average = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        user_input = int(user_input)
    except:
        print("Invalid Input")
        continue
    total = total + user_input
    count += 1
try:
    average = total / count
except:
    print("")
else:
    print(total,count,average)
