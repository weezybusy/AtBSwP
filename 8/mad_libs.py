'''
mad_libs.py -- reads in text file and lets the user add their own text
anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears.
'''
import re

with open('src.txt') as original:
    text = original.read()
    blanks_list = re.findall(r'ADJECTIVE|ADVERB|NOUN|VERB', text)
    for blank_type in blanks_list:
        article = 'an' if blank_type[0] in 'AEIOU' else 'a'
        key_word = input('Enter {} {}: '.format(article, blank_type.lower()))
        text = re.sub(blank_type, key_word, text, count=1)
    with open('dest.txt', 'w') as result:
        result.write(text)
    print('\n' + text)
