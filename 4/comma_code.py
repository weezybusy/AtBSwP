'''
comma_code.py -- takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with 'and' inserted
before the last item.
'''

def comma_code(lst):
    s = ''
    for i in range(len(lst) - 1):
        s += lst[i] + ', '
    s += 'and ' + lst[-1] + '.'

    return s

lst = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(lst))
