#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>

"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3],
                              charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)
