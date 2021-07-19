#Exercise 2     This program counts the distribution of the hour of the day for each of
#               the messages. You can pull the hour from the “From” line by finding
#               the time string and then splitting that string into parts using the
#               colon character. Once you have accumulated the counts for each hour,
#               print out the counts, one per line, sorted by hour as shown below
fname = input('Enter a file name : ')
try:
    fhand = open(fname)
except:
    print('This file can not be opened. ')
    exit()
emailHourCount = dict()
for line in fhand:
    if not line.startswith('From'):
        continue
    linesplit = line.split()
    try:
        hoursplit = linesplit[5].split(':')
    except:
        continue
    emailHourCount[hoursplit[0]] = emailHourCount.get(hoursplit[0],0) + 1
    #count the hour appears from emails
print(emailHourCount)
countHour = list(emailHourCount.items())
countHour.sort()
for hour,count in countHour:
    print(hour,count)
