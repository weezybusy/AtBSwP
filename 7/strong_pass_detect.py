'''
strong_pass_detect.py -- function uses regex to make sure the password string
it's passed is strong. A strong password is defined as one that is at least
eight characters long, contains both uppercase and lowercase characters, and
has at least one digit.
'''
import re

def is_strong(password):
    # variant 1
    print(re.search(r'[A-Za-z\d]{8,}', password) != None and
          re.search(r'[A-Z]',          password) != None and
          re.search(r'[a-z]',          password) != None and
          re.search(r'\d',             password) != None)

    # variant 2
    print(re.match(r'''
        ^(?=.*?\d)       # at least one digit
        (?=.*?[A-Z])     # at least one uppercase
        (?=.*?[a-z])     # at least one lowercase
        [A-Za-z\d]{8,}$  # 8+ uppercase, lowercase, or digit characters
        ''', password, re.VERBOSE) != None)


is_strong('helloG5world')
