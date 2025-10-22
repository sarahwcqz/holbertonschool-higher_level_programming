#!/usr/bin/python3
"""
list all cities from a DB
use a long query to see syntax
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

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities LEFT JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
