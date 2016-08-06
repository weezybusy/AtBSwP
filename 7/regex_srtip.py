'''
regex_strip.py -- function takes string as a parameter and does the same
thing as the strip() string method.
'''
import re

def build_re_char_class(chars):
    # If string specified by chars contains special characters
    # such as ]\^-, substitutes them with escaped ones and
    # returns a new string.
    return r'[' + re.sub(r'([\]\\\^\-])', r'\1', chars) + r']'


def strip_cust(string, chars=None):
    # Return a copy of the string with the leading and trailing
    # characters removed. The c argument is a string specifying
    # the set of characters to be removed. If omitted or None, the
    # chars argument defaults to removing whitespace. The c
    # argument is not a prefix or suffix; rather, all combinations
    # of its values are stripped.
    if chars == None:
        chars = '\s'
    else:
        chars = build_re_char_class(chars)
    return re.sub(r'^' + chars + '*(.*?)' + chars + '*$', r'\1', string)


print(strip_cust('eeeestripee', 'e'))
print(strip_cust('///strip/', '/'))
print(strip_cust(']]]strip]]', ']'))
print(strip_cust('bcastripacb', 'abc'))
print(strip_cust(':.strip.,.', '.,:'))
