#!/usr/bin/python3
""" A module focused on MySQLdb Usage """


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Select city name, id and state name
    Also jotin the table where city.states.id
    == states.id
    """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
