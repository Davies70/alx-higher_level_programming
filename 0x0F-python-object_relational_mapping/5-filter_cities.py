#!/usr/bin/python3

"""
lists all cities of a state
takes 4 arguments: mysql username, mysql password, \
        database name and state name \
        (SQL injection free!)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
              db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM cities INNER JOIN \
    states ON cities.state_id=states.id")
    print(", ".join([city[2] for city in cur.fetchall() if city[4] == sys.argv[4]]))
