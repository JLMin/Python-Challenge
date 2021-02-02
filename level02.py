# http://www.pythonchallenge.com/pc/def/ocr.html

from collections import Counter

with open('level02.txt') as f:
    content = f.read()
    count = Counter(content)
    ordered = count.most_common()[::-1]
    print(ordered)

rare = [('y', 1), ('t', 1), ('i', 1), ('l', 1), ('a', 1), ('u', 1), ('q', 1), ('e', 1)]
rare.reverse()
out = ''.join([p[0] for p in rare])
print(out)
