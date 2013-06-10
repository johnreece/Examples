import sqlite3

conn = sqlite3.connect("test.db")
cur  = conn.cursor()
cur.execute("insert into employees values(?,?,?)",["000000000","Not","Null"])
conn.commit()

for row in cur.execute("select * from employees"):
	print "%s %s\n" % (row[0],row[2])