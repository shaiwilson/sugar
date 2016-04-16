#!/usr/bin/env python

__author__ = 'Shai Wilson <sjwilson2@usfca.edu>'
__license__ = 'MIT License. See LICENSE.'

import sys

def hello(args):
    print('Hello, {0}!'.format(args.username))


def goodbye(args):
    print('Goodbye, {0}!'.format(args.timeframe))

def handle_input():
    """"""

    command = None

    
    input_string = raw_input("HBA Database> ")
    tokens = input_string.split()
    command = tokens[0]
    args = tokens[1:]

    if command == "student":
        if len(args) != 1:
            print "Invalid, please use: student [github name]"
        else:
            github = args[0]
            get_student_by_github(github)

    elif command == "new_student":
        if len(args) != 3:
            print "Invalid, please use: new_student [first] [last] [github]"
        else:
            first_name, last_name, github = args  # unpack!
            make_new_student(first_name, last_name, github)

    elif command == "project":
        if len(args) != 1:
            print "Invalid, please use: project [title]"
        else:
            title = args[0]
            get_project_by_title(title)

    elif command == "grade":
        if len(args) != 2:
            print "Invalid, please use: grade [github] [title]"
        else:
            github, title = args
            get_grade_by_github_title(github, title)

    elif command == "assign_grade":
        if len(args) != 3:
            print "Invalid, please use: assign_grade [github] [title] [grade]"
        else:
            github, title, grade = args
            assign_grade(github, title, grade)

    # NEW COMMANDS IN ADVANCED

    elif command == "new_project":
        # This is tricky, since the description could be many words --
        # it isn't just a single word in args.
        #
        # So, they're in order of "title", "max_grade", "description"
        # and description becomes everything after max_grade

        if len(args) < 3:
            print "Invalid, please use: new_project [title] [max-grade] [description]"
        else:
            title = args[0]
            max_grade = int(args[1])
            description = " ".join(args[2:])

            make_new_project(title, description, max_grade)

    elif command == "grades":
        if len(args) != 1:
            print "Invalid, please use: grades [github]"
        else:
            github = args[0]
            get_grades_by_github(github)

def get_parser():
    """ Get parser object for script sugar.py """

    import argparse

    # handle input
    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')
    subparsers = parser.add_subparsers()

    parser.add_argument('--version', action='version', version='1.0.0')

    # parser.add_argument('-s', 'start',
    #                     action = 'store_true',
    #                     default = False,
    #                     dest='start_sugar',
    #                     help='Punch in to the clock, you are working now!')

    # parser.add_argument('-q', 'quit',
    #                     action = 'store_true',
    #                     default = False,
    #                     dest='stop_sugar',
    #                     help='Punch out, but did you finish all your work?')

    # parser.add_argument('-c', 'clear',
    #                     action = 'store_true',
    #                     default = False,
    #                     dest='clear_sugar',
    #                     help='Clear your work log history')

    setup_parser = subparsers.add_parser('setup', help='Start sugar as a new user')
    setup_parser.add_argument('username', help='Give your username to sugar')  # add the name argument
    setup_parser.set_defaults(func=hello)  # set the default function to hello

    show_parser = subparsers.add_parser('show', help='Show the amount of hours you worked by day or week')
    show_parser.add_argument('timeframe')
    show_parser.set_defaults(func=goodbye)


    usage = """usage: sugar.py [--help] <command> [<args>]
          

          Commands:

              sugar.py setup <command>   add username and github account
              sugar.py start             start the clock
              sugar.py quit              stop the clock
              sugar.py show <command>    display all saved intervals
              sugar.py clear             delete all saved intervals
              'sugar.py <command> --help' to see how to use a command


          Options:
              -h --help     Show this screen.
          """


    return parser


if __name__ == '__main__':
    
    if sys.argv == 'start' or 'stop' :
        handle_input()
    else:
        args = get_parser().parse_args()
        args.func(args)  # call the default function



    