"""Model for sugar project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Intervals(db.Model):

    __tablename__ = "intervals"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.String(50), nullable=False)


class Student(db.Model):
    """A user of sugar; stored in a database."""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)

        
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s username=%s>" % (self.user_id, self.username)

# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///intervals'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    
    from sugar import app
    connect_to_db(app)
    print "Connected to intervals DB."