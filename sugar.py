#!/usr/bin/env python

from time import strftime
from calendar import month_abbr
import argparse



def start(args):
    


def stop(args):
    

def show(args):
    


def clear(args):



def main():

    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')

    parser.add_argument('start', action='store_true',
                   help='')

    parser.add_argument('stop', dest='accumulate', action='store_true',
                   help='')

    parser.add_argument('show', dest='accumulate', action='store_true',
                   help='')

    parser.add_argument('clear', dest='accumulate', action='store_true',
                   help='')


    usage = """usage: sugar.py [--help] <command> [<args>]
            

            Commands:

                sugar.py start   start the clock
                sugar.py stop    stop the clock
                sugar.py show    display all saved intervals
                sugar.py clear   delete all saved intervals
                'sugar.py <command> --help' to see how to use a command


            Options:
                -h --help     Show this screen.
            """


    options, arguments = parser.parse_args()

    if len(args) != 1:
        parser.print_help()


if __name__ == '__main__':
    main()
    args = parser.parse_args()
    args.func(args)  # call the default function















