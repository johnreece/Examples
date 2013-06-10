import xml.dom.minidom

dom = xml.dom.minidom.parse("employee.xml")
# Need this pro-forma declaration

node =  dom.documentElement

empRecords = dom.getElementsByTagName('person')
for row in empRecords:
	social = row.getAttribute('ssn')
	employeeID = row.getAttribute('empid')
	fields = row.childNodes
	print social, employeeID,
	for node in fields:
		if node.nodeName == "first":
			# Have to test this since if there is no text
			# it will blow up
			if node.firstChild:
				print node.nodeName,": ",node.firstChild.data,
		if node.nodeName == "last":
			if node.firstChild
				print node.nodeName,": ",node.firstChild.data