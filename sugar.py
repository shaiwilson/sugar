#!/usr/bin/env python

from time import strftime
from calendar import month_abbr
from optparse import OptionParser

def main():

    parser = OptionParser()

    parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")

    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

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
        print "\n\n------- spdeck-scrape: ERROR! --------"
        print "      Usage:"
        print "      Please specify an argument or or -h to display options (if desired):\n"
        print "      Example: "
        print "          sugar.py start\n\n"

    print options
    print args

if __name__ == '__main__':
    main()