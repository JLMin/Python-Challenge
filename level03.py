# http://www.pythonchallenge.com/pc/def/equality.html

import re

with open('level03.txt') as f:
    content = f.read()
    pattern = r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
    matches = re.findall(pattern, content)
    out = ''.join(matches)
    print(out)
