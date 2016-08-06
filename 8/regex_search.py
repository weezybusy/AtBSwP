'''
regex_search.py -- opens all files in a folder and searches
for any line that matches a user-supplied regular expression.
Result is printed on the screen.
'''
import os
import re

def main():
    path = '.'
    pattern = r'c\w+n'
    regex = re.compile(pattern, re.I)
    file_list = os.listdir(path)
    for filename in file_list:
        if filename.endswith('.txt'):
            with open(os.path.join(path, filename), 'r') as some_file:
                file_content = some_file.read()
                matches = re.findall(regex, file_content)
                if len(matches) > 0:
                    for match in matches:
                        print('{}: {}'.format(filename, str(match)))
                else:
                    print('No matches in {}'.format(filename))

main()
