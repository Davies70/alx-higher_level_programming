#!/usr/bin/python3
"""
An SQL search query safe from
SQL injections

"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    '{:s}' ASC".format(sys.argv[4], "id"))
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
