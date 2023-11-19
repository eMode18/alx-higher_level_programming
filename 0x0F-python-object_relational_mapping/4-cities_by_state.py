#!/usr/bin/python3
"""  display every state from  hbtn_0e_0_usa database"""
import MySQLdb
import sys


if __name__ == "__main__":
    d_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], d_base=sys.argv[3], port=3306)
    cursor = d_base.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    result_set = cursor.fetchall()
    for result in result_set:
        print(result)
    cursor.close()
    d_base.close()
