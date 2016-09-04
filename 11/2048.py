#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 2048 is a simple game where you combine tiles by sliding them up, down,
# left, or right with the arrow keys. You can actually get a fairly high
# score by repeatedly sliding in an up, right, down, and left pattern over
# and over again.
#
# Write a program that will open the game at:
#
#       https://gabrielecirulli.github.io/2048/
#
# and keep sending up, right, down, and left keystrokes to automatically
# play the game.

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

up    = '\x1b[A'
down  = '\x1b[B'
right = '\x1b[C'
left  = '\x1b[D'
quit  = 'q'

keys = { up, down, left, right, quit }

def get_move():
    while True:
        key = input('input: ')
        if key not in keys:
            print('not an arrow key!')
            continue
        return key
        break


def main():
    print('Press left, right, up, down arrow keys to move tiles or q to quit.')
    url = 'https://gabrielecirulli.github.io/2048/'
    driver = webdriver.Firefox()
    driver.get(url)
    html_elem = driver.find_element_by_class_name('tile-container')
    while True:
        key = get_move()
        if key == up:
            html_elem.send_keys(Keys.UP)
            continue
        elif key == down:
            html_elem.send_keys(Keys.DOWN)
            continue
        elif key == left:
            html_elem.send_keys(Keys.LEFT)
            continue
        elif key == right:
            html_elem.send_keys(Keys.RIGHT)
            continue
        else:
            break
    driver.quit()


if __name__ == '__main__':
    main()
