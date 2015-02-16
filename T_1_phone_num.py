def phone(astr_num):
    """ input - a string that represent a phone number in usual format.
        output - a string representing international format. """
    res = ""
    for char in astr_num:
        if char not in "()":
            res += char
    return "+38"+res

num1 = "(012) 535 14 71"
ans = phone(num1)
print ans
