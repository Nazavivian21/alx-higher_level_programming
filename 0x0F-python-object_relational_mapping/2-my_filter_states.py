#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table \
    of hbtn_0e_0_usa where name matches the argume
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
