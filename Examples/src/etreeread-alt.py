try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

employees = ET.ElementTree(file='employee.xml')
employees.getroot()
for empRec in employees.iter(tag='person'):
	#print empRec.tag, ":"
	print "Employer ID: ",empRec.attrib['empid']
	print "SSN: ",empRec.attrib['ssn']
	for fields in empRec.iter():
		print fields.tag, fields.text
	