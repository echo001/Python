#use python pickle module to solve this problem
import pickle
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
#the url is from the source code "http://www.pythonchallenge.com/pc/def/peak.html"
fhand = urlopen(url)
loadedlist = pickle.load(fhand)

gameaddr = ''
for line in loadedlist:
    for i in range(len(line)):
        gameaddr = gameaddr + line[i][1]*line[i][0]
    print(gameaddr)
    gameaddr = ''

#the final result will get 'channel' word formulated by '#' character
