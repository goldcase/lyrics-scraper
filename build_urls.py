#!/usr/bin/python

import sys

BASE_URL = "http://www.azlyrics.com"
NUMBER_SEGMENT = "/19"

def build_url(artist):
    ret = BASE_URL

    if artist[0].isdigit():
        ret += NUMBER_SEGMENT
    else:
        ret += "/" + artist[0]
    ret += "/" + artist + ".html"

    return ret

def get_urls():
    urls = []
    file = open(sys.argv[1])

    # Read in each normalized artist, remove newlines, and get the URL.
    for line in file:
        urls.append(build_url(line.replace("\n", "")))
    file.close()

    return urls

def write_urls_to_file():
    file = open("urls.txt", "w")
    for url in get_urls():
        file.write(url + "\n")

    file.close()

write_urls_to_file()
