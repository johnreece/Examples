# Example of parsing a basic database record

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

employees = ET.ElementTree(file='employee.xml')
#Don't really need this for using iter(?)
#employees.getroot()
for empRec in employees.iter(tag='person'):
	#print empRec.tag
	empid = empRec.attrib['empid']
	ssn = empRec.attrib['ssn']
	first = empRec[0].text
	last = empRec[1].text
	print empid,ssn,first,last
	#empRec[0].text  = "Nobody"
	#print empid, ssn, empRec[0].text, last
