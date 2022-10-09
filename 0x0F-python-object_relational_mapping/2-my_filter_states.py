#!/usr/bin/python3
"""
filter states by user input
script 4 arguments: mysql username, mysql password,
database name and state name searched

"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall() if state == sys.argv[4]]
