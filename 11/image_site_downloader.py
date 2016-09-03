#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting
# images. You could write a program that works with any photo site that has
# a search feature.
# I use Imgur. Program takes a command line argument with the keyword for
# searching and downloads most relevant weekly results.

import bs4
import os
import requests
import sys

def save_img(filename, url): 
    with open(filename, 'wb') as output:
        res = requests.get(url)
        res.raise_for_status()
        output.write(res.content)


def main():
    # Create directory for downloaded photos
    path = '/home/weezy/Pictures/imgur' 
    os.makedirs(path, exist_ok=True)

    # Base web page address
    base_url = 'https://imgur.com'

    # Validate command line arguments
    if len(sys.argv) < 2:
        print('Usage: {} keyword'.format(sys.argv[0]))
        sys.exit(0)

    subject = ' '.join(sys.argv[1:])

    # Compose page url
    url = 'https://imgur.com/search/relevance/week?q=' + subject

    # Get the page with previews
    res = requests.get(url)
    res.raise_for_status()

    # Get the list of image tags with urls to previews
    soup = bs4.BeautifulSoup(res.text)
    img_tags = soup.select('a img')
    count = 1
    for img_tag in img_tags:
        # The difference between preview and full image url is in letter 'b'
        # at the end of the preview name, so we removing
        img_url = 'https://' + img_tag.get('src')[2:].replace('b.', '.')
        img_file = os.path.join(path, str(count))
        # Download and save image
        save_img(img_file, img_url)
        count += 1


if __name__ == '__main__':
    main()
