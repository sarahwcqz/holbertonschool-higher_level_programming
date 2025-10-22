#!/usr/bin/python3
"""
takes the name of the state as argument
then displays its info
-> put a var in the sql query w/ placeholder using format
/!\ NOT SECURED
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
        "SELECT * FROM states WHERE name ='{}' ORDER BY id".format(sys.argv[4])
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
