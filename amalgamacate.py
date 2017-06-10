#!/usr/bin/env python
"""Amalgamates all specified file references from a main source file into one large source file.

Searches through the main source file for a 'hotword:source_file' phrase.
Replaces this line with the full contents of the specified 'source_file'.
"""

__author__ = "Carl Baumann"
__copyright__ = "Copyright 2017"

__license__ = "MIT"


import argparse
import shutil


def amalgamacate():
    # Set up Command line argument detection
    parser = argparse.ArgumentParser(description='Amalgamate source files into one large file')
    parser.add_argument('main', help='the file that contains the main process')
    parser.add_argument('output', help='the destination file')
    parser.add_argument('-hw', '--hotword', help='the hot word to look for, default="AMALGAMACATE:"')
    args = parser.parse_args()

    if args.hotword is None:
        args.hotword = 'AMALGAMACATE'

    # if no file type is given, copy the 'main's file type
    if '.' not in args.output:
        file_suffix = args.main.split('.')
        if len(file_suffix) > 1:
            args.output += "." + file_suffix[-1].rstrip()
        exit()

    with open(args.main, 'r') as infile, open(args.output, 'w+') as outfile:
        for line in infile:
            if line.__contains__(args.hotword):
                hotline = line.split(':')
                with open(hotline[1].rstrip()) as external_file:
                    shutil.copyfileobj(external_file, outfile)
            else:
                outfile.write(line)

    print('Files successfully amalgamacated into one!')


if __name__ == "__main__":
    amalgamacate()
