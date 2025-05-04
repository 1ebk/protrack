import sqlite3
import json

def init_db():
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries
                 (date TEXT PRIMARY KEY, fields TEXT)''')
    conn.commit()
    conn.close()

def add_entry(date, fields_json):
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO entries VALUES (?, ?)",
              (date, fields_json))
    conn.commit()
    conn.close()