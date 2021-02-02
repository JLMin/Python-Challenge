# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/zip.html
# http://www.pythonchallenge.com/pc/def/channel.zip

import os
import re
import zipfile
from pathlib import Path

import requests

pattern = 'Next nothing is (\d+)'


def download():
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    content = requests.get(url).content
    with open('level06.zip', 'wb+') as zf:
        zf.write(content)


def unzip():
    with zipfile.ZipFile('level06.zip') as zf:
        zf.extractall(r'.\level06')


def find_hint():
    pattern = 'Next nothing is \d+'
    for file in Path('level06').iterdir():
        with open(file) as f:
            content = f.read()
            if re.match(pattern, content):
                continue
            print(f'file: {file}')
            print(f'content:\n{content}\n')


def find_90052():
    for file in Path('level06').iterdir():
        with open(file) as f:
            content = f.read()
            if '90052' in content or '90052' in str(file):
                print(f'{file:20s}{content}')


def comments(zip_file, num):
    basepath = 'level06'
    file = f'{basepath}\{num}.txt'
    with open(file) as f:
        content = f.read()
        print(zip_file.getinfo(f'{num}.txt').comment.decode('utf-8'), end='')
        match = re.search(pattern, content)
        if match:
            num = match.group(1)
            comments(zip_file, num)


if __name__ == '__main__':
    # download()

    # unzip()

    # find_hint()
    """
        file: level06\46145.txt
        content:
        Collect the comments.

        file: level06\readme.txt
        content:
        welcome to my zipped list.

        hint1: start from 90052
        hint2: answer is inside the zip
    """

    # find_90052()

    zip_file = zipfile.ZipFile('level06.zip')
    comments(zip_file, 90052)
    # http://www.pythonchallenge.com/pc/def/hockey.html
