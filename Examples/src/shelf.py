import shelve

x = [1,3,5,7,9]
fh = shelve.open("shelfdb","c")
fh['566025215'] = "John Reece"
fh['111223333'] = "Joe Doakes"
fh.close()
fh = shelve.open("shelfdb")
print fh['111223333']