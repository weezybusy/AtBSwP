'''
del_unneeded_files.py -- searches for files larger than 100MB in specified
folder and prints them out. This program doesn't delete files, but prints
them out instead.
'''
import os

def del_unneeded_files(folder):
    # make sure folder is absolute
    folder = os.path.abspath(folder)

    # check if folder exists
    if not os.path.exists(folder):
        print('Folder "{}" doesn\'t exist.'.format(folder))
        return

    # walk through folder
    for foldname, subfolds, filenames in os.walk(folder):
        # walk through files in current folder
        for filename in filenames:
            # get file name with its absolute path
            filename = os.path.join(foldname, filename)
            # get file size in MB
            filesize = os.path.getsize(filename) / 1000000

            # print file name with full path if size is larger than 100MB
            if filesize > 100:
                print('{}: {:.0f}MB'.format(filename, filesize))

del_unneeded_files('/some/path')
