import sys
import sqlite3 as sql

conn = sql.connect("employees.db")
curs = conn.cursor()

query = "select * from employees where first = ?"
curs.execute(query,['Joe'])
for row in curs.fetchall():
	print "%-10s %-10s" % (row[0],row[1])