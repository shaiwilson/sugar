"""Models and sugar project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Intervals(db.Model):

    __tablename__ = "intervals"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime, db.ForeignKey('intervals.start'))
    end_time = db.Column(db.String(50), nullable=False)


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)


    intervals = db.relationship('Intervals', backref="student")

    def __init__(self, username):
        self.username = username
        
    def __repr__(self):
        return '<User %r>' % self.username

# End Part 1
##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///intervals'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to intervals DB."