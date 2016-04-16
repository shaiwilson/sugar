#!/usr/bin/env python

__author__ = 'Shai Wilson <sjwilson2@usfca.edu>'
__license__ = 'MIT License. See LICENSE.'

def hello(args):
    print('Hello, {0}!'.format(args.username))


def goodbye(args):
    print('Goodbye, {0}!'.format(args.timeframe))



def get_parser():
    """ Get parser object for script sugar.py """

    import argparse

    # handle input
    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')
    subparsers = parser.add_subparsers()

    parser.add_argument('--version', action='version', version='1.0.0')
    parser.add_argument('-s', '--start')

    setup_parser = subparsers.add_parser('setup')
    setup_parser.add_argument('username', help='Give your username to sugar')  # add the name argument
    setup_parser.set_defaults(func=hello)  # set the default function to hello

    show_parser = subparsers.add_parser('show', help='Show the amount of hours you worked by day or week')
    show_parser.add_argument('timeframe')
    show_parser.set_defaults(func=goodbye)


    usage = """usage: sugar.py [--help] <command> [<args>]
          

          Commands:

              sugar.py setup <command>   add username and github account
              sugar.py start             start the clock
              sugar.py stop              stop the clock
              sugar.py show <command>    display all saved intervals
              sugar.py clear             delete all saved intervals
              'sugar.py <command> --help' to see how to use a command


          Options:
              -h --help     Show this screen.
          """

if __name__ == '__main__':
    args = parser.parse_args()

    # show usage text for commands without args
    if len(args) != 1:
        parser.print_help()

    args.func(args)  # call the default function