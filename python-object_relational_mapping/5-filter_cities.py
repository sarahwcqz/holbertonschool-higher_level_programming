#!/usr/bin/python3
"""
list all cities from a state passed as arg
use .join() for output
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
        "SELECT cities.name "
        "FROM cities RIGHT JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id", (sys.argv[4],)
    )

    print(", ".join([row[0] for row in cursor.fetchall()]))

    cursor.close()
    db.close()
