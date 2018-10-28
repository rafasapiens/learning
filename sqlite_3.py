import sqlite3

connection = sqlite3.connect("Database.db")
c = connection.cursor()

#SQL

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS dados (id INTEGER, unix REAL, keyrd TEXT, datestamp TEXT, value REAL)")

create_table()
