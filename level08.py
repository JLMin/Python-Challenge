# http://www.pythonchallenge.com/pc/def/integrity.html
# http://www.pythonchallenge.com/pc/return/good.html

import re
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 '\
     b'\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ '\
     b'\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


username = bz2.decompress(un)
password = bz2.decompress(pw)

print(f'username = "{username}"')
print(f'password = "{password}"')

# """
#     Replace hex?
# """
# pattern = r'\\x.{2}'

# def replace_hex(s):
#     matches = re.findall(pattern, s)
#     for match in matches:
#         s = s.replace(f'{match}', str(int(match[2:], 16)))
#     return s

# username = replace_hex(un)
# password = replace_hex(pw)

# print(f'username = "{username}"')
# print(f'password = "{password}"')

# """
# username = "BZh91AY&SYA175130\r0011128219220 0!154h3M7<]20120225BA619084"
# password = "BZh91AY&SY148$|1400012903$ 0!154h3M19<]20120225BBP1452408"

# username = "BZh91AY & SYA175130\r0011128219220 0!154h 3M7  <]2012 02 25 BA619084"
# password = "BZh91AY & SY148$|1400012903$       0!154h 3M19 <]2012 02 25 BBP1452408"
# """
