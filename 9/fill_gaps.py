'''
fill_gaps.py -- finds all files with the given prefix in a single folder,
locates any gaps in the numbering and renames all later files to close the gap.
This version takes folder and prefix as command-line arguments.
'''
import os, re, shutil, sys

def fill_gaps():
    # check the number of arguments
    if len(sys.argv) < 3:
        print('Usage: python fill_gaps.py folder prefix')
        return

    folder = sys.argv[1]
    prefix = sys.argv[2]

    # make sure folder path is absolute
    folder = os.path.abspath(folder)

    # check if folder exists
    if not os.path.exists(folder):
        print('"{}" doesn\'t exist.'.format(folder))
        return

    # regex pattern
    regex = re.compile(r'''
                       ({})                # prefix
                       (\d+)               # numbering
                       (\.[a-zA-Z0-9]+)    # extension
                       '''.format(prefix), re.VERBOSE)

    counter = 1
    # walk through all files and find matches
    for filename in sorted(os.listdir(folder)):
        mo = regex.search(filename)

        # if file doesn't match pattern, skip it
        if mo == None:
            continue

        # break filename into pieces
        numbering = mo.group(2)
        extension = mo.group(3)

        # if filename numbering is in order, go to the next file
        if int(numbering) == counter:
            counter += 1
            continue

        # file numbering is out of order, make a correct one
        new_numbering = str(counter)

        # pad new numbering with 0's if needed
        while len(new_numbering) < len(numbering):
            new_numbering = '0' + new_numbering

        # compose old and new filenames with full paths
        filename = os.path.join(folder, filename)
        new_filename = prefix + new_numbering + extension
        new_filename = os.path.join(folder, new_filename)

        # rename unordered filenames
        shutil.move(filename, new_filename)

        # increment numbering
        counter += 1

fill_gaps()
