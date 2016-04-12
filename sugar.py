#!/usr/bin/env python

from time import strftime
import argparse
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# constants
DB_DIR = ".sugar"
DB_FILE = "intervals.db"
DATE_DB_FORMAT = "%Y%m%d"
DATE_PRINT_FORMAT = "%b %d, %Y"
TIME_DB_FORMAT = "%H:%M"
TIME_PRINT_FORMAT = "%I:%M %p"
SECS_IN_HOUR = 60 * 60

db = SQLAlchemy()

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intervals'
    db.app = app
    db.init_app(app)


# db control

def punch_in():
   """Given the start command, log timestamp information for the current work session."""


def punch_out():
    """ """


def show_intervals():
    """ """


def clear_intervals():
    """ """


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

    # show usage text for commands without args
    if len(args) != 1:
        parser.print_help()

def handle_input(args):
    """Helper function to direct commands to corresponding actions."""

    command = args

    args = tokens[1:]

    if command == "start":
        punch_in()

    elif command == "stop":
        punch_out()

    elif command == "show":
        show_intervals()

    elif command == "clear":
        clear_intervals()





if __name__ == '__main__':
    main()
    app = Flask(__name__)
    connect_to_db(app)

    # handle input
    args = parser.parse_args()
    handle_input(args)

    db.session.close()













