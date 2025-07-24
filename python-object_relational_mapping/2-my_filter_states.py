#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys


class hbtn_0e_0_usa():
    '''
    script that lists all states from the database hbtn_0e_0_usa
    '''
    if __name__ == "__main__":
        the_db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )
        if len(sys.argv) != 5:
            print("the sys.argv must be 4")
            sys.exit(1)
        ascending = the_db.cursor()
        ascending.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
            )
        result = ascending.fetchall()
        state_name_searched = sys.argv[4]
        for rows in result:
            pass
        print(f"({rows[0]}, {state_name_searched.format()})")
