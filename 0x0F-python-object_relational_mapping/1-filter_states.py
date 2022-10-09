#!/usr/bin/python3

"""

Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
Usage: script should take 3 arguments:
mysql username, mysql password and database name
(no argument validation needed)

"""


import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306,
                              user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(rows) for rows in cur.fetchall()]
