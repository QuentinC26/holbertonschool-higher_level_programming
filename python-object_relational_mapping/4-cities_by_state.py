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
        if len(sys.argv) != 4:
            print("the sys.argv must be 3")
            sys.exit(1)
        ascending = the_db.cursor()
        ascending.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY id ASC;"
            )
        result = ascending.fetchall()
        for row in result:
            print(f"({row[0]}, '{row[1]}', '{row[2]}')")
