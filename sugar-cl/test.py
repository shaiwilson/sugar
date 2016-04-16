#!/usr/bin/env python

__author__ = 'Shai Wilson <sjwilson2@usfca.edu>'
__license__ = 'MIT License. See LICENSE.'

import sys
from time import strftime
from datetime import datetime
# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# constants
DB_DIR = ".sugar"
DB_FILE = "intervals.db"
DATE_DB_FORMAT = "%Y%m%d"
DATE_PRINT_FORMAT = "%b %d, %Y"
TIME_DB_FORMAT = "%H:%M"
TIME_PRINT_FORMAT = "%I:%M %p"
SECS_IN_HOUR = 60 * 60

# db = SQLAlchemy()

# def connect_to_db(app):
#     """Connect the database to Flask app."""

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intervals'
#     db.app = app
#     db.init_app(app)

def hello(args):
    """Add a new user and print confirmation.

    Given a username add user to the
    database and print a confirmation message.
    """

    # QUERY = """INSERT INTO Students VALUES (:username:)"""
    # db_cursor = db.session.execute(QUERY, {'username': username})
    # db.session.commit()

    print('Hello, {0}! Welcome to sugar :-)'.format(args.username))


def goodbye(args):
    print('Goodbye, {0}!'.format(args.timeframe))

def punch_in():
  """Given the start command, log timestamp information for the current work session."""

  # first make sure they did not already punch in 

  now = datetime.now()
  current_time = now.strftime(TIME_DB_FORMAT)
  current_date = now.strftime(DATE_DB_FORMAT)
  print_format = now.strftime(TIME_PRINT_FORMAT)

  # change "date " in intervals db to "date_time"
  # QUERY = """INSERT INTO Intervals (date_time, start_time)
  #          VALUES (:date_time, :start_time)"""

  # db_cursor = db.session.execute(QUERY, {'date_time': current_date, 'start_time': current_time})

  print "Punched in at %s" %(print_format)

def punch_out():
  """Given the stop command, log timestamp information for the current work session."""

  now = datetime.now()
  current_time = now.strftime(TIME_DB_FORMAT)
  current_date = now.strftime(DATE_DB_FORMAT)
  print_format = now.strftime(TIME_PRINT_FORMAT)

  # change "date " in intervals db to "date_time"
  # QUERY = """INSERT INTO Intervals (date_time, end_time)
  #             VALUES (:date_time, :end_time)"""

  # db_cursor = db.session.execute(QUERY, {'date_time': current_date, 'end_time': current_time})

  print "Punched out at %s" %(print_format)

def setGoals(args):

def clearLog(args):


def handle_input(args):
    """ """
    
    command = args[1]

    if command == "start":
        punch_in()

    elif command == "stop":
        punch_out()

    

def get_parser():
    """ Get parser object for script sugar.py """

    import argparse

    # handle input
    parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')
    subparsers = parser.add_subparsers()

    parser.add_argument('--version', action='version', version='1.0.0')

    setup_parser = subparsers.add_parser('setup', help='Start sugar as a new user')
    setup_parser.add_argument('username', help='Give your username to sugar')  # add the name argument
    setup_parser.set_defaults(func=hello)  # set the default function to hello

    show_parser = subparsers.add_parser('show', help='Show the amount of hours you worked by day or week')
    show_parser.add_argument('timeframe')
    show_parser.set_defaults(func=goodbye)

    goals_parser = subparsers.add_parser('goals', help= "Set your work productivity goals.")
    goals_parser.add_argument('goal', help='Give the amount of hours you would like to work today')
    goals_parser.set_defaults(func=setGoals) 

    clear_parser = subparsers.add_parser('clear', help= "Clear your sugar log.")
    clear_parser.add_argument('clear', help='')
    clear_parser.set_defaults(func=clearLog) 


    usage = """usage: sugar.py [--help] <command> [<args>]
          

          Commands:

              sugar.py setup <command>   add username and github account
              sugar.py start             start the clock
              sugar.py stop              stop the clock
              sugar.py show  <command>   display all saved intervals
              sugar.py clear <command>   delete all saved intervals
              'sugar.py <command> --help' to see how to use a command


          Options:
              -h --help     Show this screen.
          """


    return parser


if __name__ == '__main__':
    
    if sys.argv == 'start' or 'stop' :
        handle_input(sys.argv)
    else:
        args = get_parser().parse_args()
        args.func(args)  # call the default function



    