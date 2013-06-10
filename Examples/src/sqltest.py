import sqlite3 as sql

conn = sql.connect("/home/notroot/workspace-python/Examples/src/employees.db")
curs = conn.cursor()

query = "select * from employees"
curs.execute(query)
for row in curs.fetchall():
	print "%-10s %-10s" % (row[0],row[1])