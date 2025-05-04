import sqlite3
from contextlib import closing
import json

def init_db():
    # conn = sqlite3.connect('progress.db') # Creates/connects to the database file. Upgraded below
    # c = conn.cursor() # Creates a 'cursor' to execute SQL commands. Upgraded below
    # Upgrade: using a with block ensures graceful exits when errors occur, preventing 'database locked' errors
    with closing(sqlite3.connect('progress.db')) as conn:
        with closing(conn.cursor) as c:
            c.execute('''CREATE TABLE IF NOT EXISTS entries 
                 (date TEXT PRIMARY KEY, fields TEXT)''') # SQL command to create a table if it doesn't exist
            conn.commit() # Saves changes and exits with block, closing the connection
    # conn.close() # Closes the connection. This is not needed when using a with block - the connection closes automatically when the block does

def add_entry(date, fields_json):
    # conn = sqlite3.connect('progress.db') Upgraded
    # c = conn.cursor() Upgraded
    with closing(sqlite3.connect('progress.db')) as conn:
        with closing(conn.cursor) as c:
            c.execute("INSERT OR REPLACE INTO entries VALUES (?, ?)", # Insert or replace entry for given date. Parametrized (?, ?) to prevent SQL injection
              (date, fields_json))
            conn.commit()
    # conn.close() Deprecated (see above)