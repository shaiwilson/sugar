

# db control

def create_new_database():
    """Crete a new databse. """


    Students = """CREATE TABLE Students (
    username VARCHAR(30),
    last_name VARCHAR(30),
    github VARCHAR(30)
    );"""




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
















