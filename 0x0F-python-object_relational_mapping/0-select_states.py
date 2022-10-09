#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3],
                              charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)
    cur.close()
    connect.close()
