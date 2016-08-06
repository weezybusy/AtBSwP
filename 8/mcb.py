'''
mcb.py -- saves and loads pieces of text to the clipboard.
Usage:
        python mcb.py save <keyword> - saves clipboard to keyword. 
        python mcb.py <keyword>      - loads keyword to clipboard.
        python mcb.py list           - loads all keywords to clipboard.
        python mcb.py del <keyword>  - deletes keyword from the shelf.
        python mcb.py del            - deletes all keywords.
As I have no pyperclip module, I use file content instead of clipboard.
'''
import shelve
import sys

def main():
    mcb_shelf = shelve.open('mcb')
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            with open('data.txt', 'r') as data_file:
                file_content = data_file.read()
                mcb_shelf[sys.argv[2]] = file_content 
        elif sys.argv[1].lower() == 'del':
            if sys.argv[2] in list(mcb_shelf.keys()):
                del mcb_shelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        with open('data.txt', 'w') as data_file:
            if sys.argv[1].lower() == 'list':
                data_file.write(str(list(mcb_shelf.keys())))
            elif sys.argv[1] in mcb_shelf:
                data_file.write(mcb_shelf[sys.argv[1]])
            elif sys.argv[1].lower() == 'del':
                for key in list(mcb_shelf.keys()):
                    del mcb_shelf[key]
    mcb_shelf.close()

main()
