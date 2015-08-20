#!/usr/bin/python

import sys
import string

def write_file(results):
    write_file = open(sys.argv[2], "w")
    for line in results:
        write_file.write(line + "\n")
    write_file.close()

def read_file():
    file_name = sys.argv[1]
    file = open(file_name)
    return file

def normalize_artists(file):
    results = []
    for line in file:
        results.append(line.lower().translate(None, string.punctuation + string.whitespace))
    file.close()
    return results

write_file(normalize_artists(read_file()))
