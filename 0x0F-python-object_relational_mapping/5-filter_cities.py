#!/usr/bin/python3
"""  display every state from  hbtn_0e_0_usa database"""
import MySQLdb
import sys


if __name__ == "__main__":
    d_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], d_base=sys.argv[3], port=3306)
    cursor = d_base.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    result_set = cursor.fetchall()
    temp = list(result[0] for result in result_set)
    print(*temp, separator=", ")
    cursor.close()
    d_base.close()
