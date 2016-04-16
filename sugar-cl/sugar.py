#!/usr/bin/env python

from time import strftime
from datetime import datetime
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

def create_new_database():
    """Crete a new databse. """


    Students = """CREATE TABLE Students (
    username VARCHAR(30),
    last_name VARCHAR(30),
    github VARCHAR(30)
    );"""

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

  # first make sure they did not already punch in 

  now = datetime.now()
  current_time = now.strftime(TIME_DB_FORMAT)
  current_date = now.strftime(DATE_DB_FORMAT)
  print_format = now.strftime(TIME_PRINT_FORMAT)

  # change "date " in intervals db to "date_time"
  QUERY = """INSERT INTO Intervals (date_time, start_time)
           VALUES (:date_time, :start_time)"""

  db_cursor = db.session.execute(QUERY, {'date_time': current_date, 'start_time': current_time})

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

  print "Punched in at %s" %(print_format)

def show_intervals(timeframe):
  """Given the show command, display daily or weekly information for the current work session."""
    # if timeframe == 1:
            

    # elif timeframe == 2:
            

def clear_intervals():
  """Given the clear command, clear log information of work sessions."""

  # clear db print "Cleared all intervals"

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

  print "handle input"

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
      timeframe = raw_input("enter 1 to see daily sum or 2 to see weekly sum")
      show_intervals(timeframe)

  elif command == "clear":
      clear_intervals()




# handle input
parser = argparse.ArgumentParser(description='Log the amount of hours you code per day.')
subparsers = parser.add_subparsers()


# show usage text for commands without args
# if len(args) != 1:
#     parser.print_help()

# handle_input(args)

setup_parser = subparsers.add_parser('setup')
setup_parser.add_argument('setup',
             help='Give your username, first name, and github to sugar')
setup_parser.set_defaults(func=make_new_user)


parser.add_argument('start',
             help='Punch in to the clock, you are working now!')

parser.add_argument('stop',
             help='Punch out, but did you finish all your work?')

parser.add_argument('show',
             help='Show the amount of hours you worked by day or week')

parser.add_argument('clear', 
             help='Clear your work log history')

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




if __name__ == '__main__':
    app = Flask(__name__)
    connect_to_db(app)

    args = parser.parse_args()
    args.func(args) # call the default function
    

    db.session.close()











