#!/usr/bin/python3
"""
A module that lists all states from a database hbtn_0
Starting with N
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access database and get the list
    of sates starting with N
    from within printing
    each to the screen
    """
    username, password, db_n = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_n)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC""")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
