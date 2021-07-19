#Exercise 2     Write another program that prompts for a list of numbers as above
#               and at the end prints out both the maximum and minimum of the
#               numbers instead of the average.
maximum = minimum = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        num = float(user_input)
    except:
        print("Invalid number")
        continue
    if maximum == None or num > maximum:
        maximum = num
    if minimum == None or num < minimum:
        minimum = num
print(maximum,minimum)
