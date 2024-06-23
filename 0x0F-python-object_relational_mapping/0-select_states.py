#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cur = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
