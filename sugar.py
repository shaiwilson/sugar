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


    parser.add_argument('start',
                   help='')

    parser.add_argument('stop',
                   help='')

    parser.add_argument('show',
                   help='')

    parser.add_argument('clear', 
                   help='')

    parser.add_argument('--version', action='version', version='1.0.0')


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

    # if an argument called start was passed, execute the start function.
    if args == 'start':
        start()
    elif args == 'stop':
        stop()

    # args.func(args)  # call the default function















