# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import requests


def download():
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    content = requests.get(url).content
    with open('level07.png', 'wb+') as img:
        img.write(content)


def get_grays():
    grays = []
    with Image.open('level07.png') as img:
        pa = img.load()
        width, height = img.size
        mid = height // 2
        for i in range(width):
            r, g, b, _ = pa[i, mid]
            if r == g == b:
                grays.append(r)
    return grays


def seprate_block(grays):
    count, maxsize = 1, 8
    pre = None
    out = ''
    for cur in grays:
        if cur != pre:
            out += chr(cur)
            count = 1
            pre = cur
        else:
            if count < maxsize:
                count += 1
            else:
                count = 1
                pre = None
    return out


def decode_grays(grays):
    out = ''
    for g in grays:
        out += chr(g)
    return out


if __name__ == '__main__':
    # download()

    grays = get_grays()

    msg = decode_grays(grays)
    print(msg)

    msg = seprate_block(grays)
    print(msg)

    next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    msg = decode_grays(next_level)
    print(msg)
