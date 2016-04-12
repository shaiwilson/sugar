#!/usr/bin/env python

from time import strftime
from calendar import month_abbr
from optparse import OptionParser

def main():

    parser = OptionParser()

    usage = """usage: sugar.py [--help] <command> [<args>]
            Log the amount of hours you code per day.

            Commands:

            start   start the clock
            stop    stop the clock
            show    display all saved intervals
            clear   delete all saved intervals
            'sugar <command> --help' to see how to use a command"""


    options, arguments = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args

if __name__ == '__main__':
    main()