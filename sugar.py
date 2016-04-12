#!/usr/bin/env python

from time import strftime
from calendar import month_abbr
import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')

    parser.add_argument('start', action='store_true',
                   help='an integer for the accumulator')

    parser.add_argument('stop', dest='accumulate', action='store_true',
                   help='sum the integers (default: find the max)')

    parser.add_argument('show', dest='accumulate', action='store_true',
                   help='sum the integers (default: find the max)')

    parser.add_argument('clear', dest='accumulate', action='store_true',
                   help='sum the integers (default: find the max)')


    usage = """usage: sugar.py [--help] <command> [<args>]
            

            Commands:

            start   start the clock
            stop    stop the clock
            show    display all saved intervals
            clear   delete all saved intervals
            'sugar.py <command> --help' to see how to use a command"""


    options, arguments = parser.parse_args()

    if len(args) != 1:
        parser.print_help()


if __name__ == '__main__':
    main()















    