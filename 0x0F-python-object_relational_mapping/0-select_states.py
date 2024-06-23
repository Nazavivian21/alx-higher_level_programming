#!/usr/bin/env python3
"""This script lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user='root',
        passwd='',
        db='hbtn_0e_0_usa',
    )

    cur = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
