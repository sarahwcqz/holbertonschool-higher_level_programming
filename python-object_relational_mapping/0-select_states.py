#!/usr/bin/python3
"""
Lists all states from DB
username, passwd and db name are passed as arguments
Connecting to a mysql DB
"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
