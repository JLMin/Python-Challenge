# http://www.pythonchallenge.com/pc/def/peak.html
# http://www.pythonchallenge.com/pc/def/pickle.html


import requests
import pickle
import pprint

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

content = requests.get(url).content
thing = pickle.loads(content)
# pprint.pp(thing)

for section in thing:
    for item in section:
        char, repeat = item
        print(char * repeat, end='')
    print()
