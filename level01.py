# http://www.pythonchallenge.com/pc/def/map.html


def translate_string(input):
    normal_lower = 'abcdefghijklmnopqrstuvwxyz'
    secret_lower = 'cdefghijklmnopqrstuvwxyzab'

    normal_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    secret_upper = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'

    normal = normal_lower + normal_upper
    secret = secret_lower + secret_upper

    trans = str.maketrans(normal, secret)

    out = input.translate(trans)
    return out


if __name__ == '__main__':

    raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. "\
          "rfyrq ufyr amknsrcpq ypc dmp. "\
          "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "\
          "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(translate_string(raw))
    print(translate_string('map'))
