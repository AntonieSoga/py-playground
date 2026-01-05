import re

def mask_cnp(cnp:str) ->str :
    return re.sub(r".(?=.{6})","*",cnp)

print(mask_cnp("1234567890000"))


def mask_cnp_py(cnp:str) -> str :
    return '*' * (len(cnp) - 6) + cnp[-6:]

print(mask_cnp_py("1234567890000"))


def mask_cnp_iterativ(cnp:str) -> str :
    res = ''
    i = 0
    size = len(cnp)

    for char in cnp:
        if  size - i > 6 :
            i+=1
        else:
            res += char

    return res

print('*'*(13-6)+mask_cnp_iterativ("1234567890000"))