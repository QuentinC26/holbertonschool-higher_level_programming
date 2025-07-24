#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb 
import sys

'''
script that lists all states from the database hbtn_0e_0_usa
'''
class hbtn_0e_0_usa():
        the_db = MySQLdb.connect(
                "Hostname", "mysql username", "mysql password", "database name"
        )
        ascending = the_db.cursor()
        ascending.execute(
                "SELECT states FROM hbtn_0e_0_usa ORDER BY states.id ASC;"
                )
