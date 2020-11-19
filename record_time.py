import sqlite3
from sqlite3 import Error
import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insert_clock_in(conn):

    cur = conn.cursor()
    cur.execute("INSERT INTO timesheet(clock_in) VALUES(CURRENT_TIMESTAMP)")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_clock_out(conn):

    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM timesheet;")


    rows = cur.fetchall()

    for row in rows:
        print(row)
        insert_cur = conn.cursor()
        insert_cur.execute("INSERT INTO timesheet(id, clock_out) VALUES(CURRENT_TIMESTAMP) WHERE id=row ")


def main():
    database = r"/home/base/times"

    # create a database connection
    conn = create_connection(database)
    with conn:

        if  'in' in sys.argv[1]:
            insert_clock_in(conn)
        elif  'out' in sys.argv[1]:
            insert_clock_out(conn)


if __name__ == '__main__':

    main()