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

def make_new_user(first_name, last_name, github):
    """Add a new user and print confirmation.

    Given a first name, last name, and GitHub account, add user to the
    database and print a confirmation message.
    """

    QUERY = """INSERT INTO Students VALUES (:first_name, :last_name, :github)"""
    db_cursor = db.session.execute(QUERY, {'first_name': first_name, 'last_name': last_name, 'github': github})
    db.session.commit()

    print "Hi %s %s, you're setup to start using sugar! :-)" % (first_name, last_name)

def punch_in():
   """Given the start command, log timestamp information for the current work session."""


def punch_out():
    """Given the stop command, log timestamp information for the current work session."""


def show_intervals():
    """Given the show command, display daily information for the current work session."""


def clear_intervals():
    """Given the clear command, clear log information of work sessions."""

    # clear db
    print "Cleared all intervals"

def get_all_hours():
    """Get the sum of all hours"""

    QUERY = """
        
        """
    db_cursor = db.session.execute(QUERY)
    rows = db_cursor.fetchall()
    return rows


def handle_input(args):
    """Helper function to direct commands to corresponding actions."""

    command = args

    if command == "setup":
        first_name = raw_input("What is your username?")
        last_name = raw_input("What is your last name?")
        github = raw_input("What is your github username?")
        make_new_student(first_name, last_name, github)


    if command == "start":
        punch_in()

    elif command == "stop":
        punch_out()

    elif command == "show":
        show_intervals()

    elif command == "clear":
        clear_intervals()



def main():

    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')

    parser.add_argument('setup',
                   help='')

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

                sugar.py setup   add username and github account
                sugar.py start   start the clock
                sugar.py stop    stop the clock
                sugar.py show    display all saved intervals
                sugar.py clear   delete all saved intervals
                'sugar.py <command> --help' to see how to use a command


            Options:
                -h --help     Show this screen.
            """


    # options, arguments = parser.parse_args()

    # show usage text for commands without args
    if len(args) != 1:
        parser.print_help()


if __name__ == '__main__':
    main()
    app = Flask(__name__)
    connect_to_db(app)

    # handle input
    args = parser.parse_args()
    handle_input(args)

    db.session.close()











