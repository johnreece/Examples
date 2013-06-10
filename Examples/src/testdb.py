import anydbm

db = anydbm.open("test", "c")
db["566025215"] = "John Reece"
db["111223333"] = "Joe Doakes"
db.close()
db = anydbm.open("test")
for k, v in db.iteritems():
	print k," ",v