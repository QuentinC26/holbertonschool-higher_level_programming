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
    the_db = MySQLdb.connect(
       host="localhost",
       user= sys.argv[1],
       password= sys.argv[2],
       database= sys.argv[3]
   )
    ascending = the_db.cursor()
    ascending.execute(
                "SELECT DISTINCT * FROM states ORDER BY states.id ASC;"
                )
    result = ascending.fetchall()
    print(result)
