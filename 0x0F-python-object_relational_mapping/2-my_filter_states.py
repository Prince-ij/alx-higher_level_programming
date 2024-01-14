#!/usr/bin/python3
""" Module For python tasks related to MySQLdb """


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Select states where name
    matches desired param
    """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC;"""
                .format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
