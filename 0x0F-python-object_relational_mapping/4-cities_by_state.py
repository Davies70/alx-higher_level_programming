#!/usr/bin/python3
"""
lists all cities from a database

"""

import sys
import MySQLdb

if __name__ == "__main__":
    connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON states.id=cities.state_id \
    ORDER BY cities.id ASC")
    [print(city) for city in cur.fetchall()]
