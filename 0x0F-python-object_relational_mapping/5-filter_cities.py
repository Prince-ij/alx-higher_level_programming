#!/usr/bin/python3
""" Module focused on MySQLdb projects """


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Select all states from a given
    table based on join on
    states.id and cities.id
    """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()

    cur.execute("""SELECT cities.id, cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC;""",
                {'state_name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row[1])

    cur.close()
    conn.close()
