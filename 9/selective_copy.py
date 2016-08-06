'''
selective_copy.py -- walks through a folder tree, searching for files with
a certain file extension and copies them into a new folder.
'''
import os
import shutil

def selective_copy(src, dest, ext):
    src_dir = os.path.abspath(src)
    dest_dir = os.path.abspath(dest)

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for dirname, subdirs, filenames in os.walk(src_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ext:
                filename = os.path.join(dirname, filename)
                shutil.copy(filename, dest_dir)


selective_copy('srcdir', 'destdir', '.ext')
