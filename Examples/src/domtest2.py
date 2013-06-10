import xml.dom.minidom

dom = xml.dom.minidom.parse("employee.xml")
# Need this pro-forma declaration

node =  dom.documentElement

empRecords = dom.getElementsByTagName('person')
for row in empRecords:
	social = row.getAttribute('ssn')
	employeeID = row.getAttribute('empid')
	field1 = row.getElementsByTagName('first')
	print field1.firstChild.data