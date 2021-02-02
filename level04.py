# http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import re
import requests

# pattern = r'\d+'
pattern = r'next nothing is (\d+)'
template = u'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'


def request_from(num):
    url = template.format(num)
    resp = requests.get(url)
    text = resp.text
    print(text)
    match = re.search(pattern, text)
    if match:
        num = match.group(1)
        request_from(num)


if __name__ == '__main__':
    # request_from('12345')
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044
    # Yes. Divide by two and keep going.

    # request_from('8022')
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682
    # There maybe misleading numbers in the text.
    # One example is 82683. Look only for the next nothing and the next nothing is 63579

    request_from('63579')
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
