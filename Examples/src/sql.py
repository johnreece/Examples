import sqlite3

try: 
	conn = sqlite3.connect("test.db");
	cur = conn.cursor()
#	cur.execute("create table employees (ssn varchar(9), first varchar(40), last varchar(80))")
	cur.execute("insert into employees values ('555667777','Joe','Blow')")
	cur.execute("insert into employees values (?,?,?)",['111223333','Jane','Doe'])
	newEmp = ['444556666','Joe','Doakes']
	cur.execute("insert into employees values (?,?,?)",newEmp)
	conn.commit()
	print "\nUnformatted dump:\n"
	print cur.execute("select * from employees")
	print cur.fetchall()
	print "\nFormated dump:\n"
	for row in cur.execute("select rowid, * from employees order by last"):
		print "%-5d %s %-10s %-40s" % (row[0],row[1],row[2],row[3])	
except Exception,Argument:

	print "Error: %s", Argument
else:
	print "\nBuh-bye!"