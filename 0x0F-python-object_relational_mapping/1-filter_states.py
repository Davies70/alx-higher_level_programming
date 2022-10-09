#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306,
                              user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(rows) for rows in cur.fetchall()]
