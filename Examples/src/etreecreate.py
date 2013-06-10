import sys
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

empRec = ET.Element('person')
empRec.attrib['empid'] = "12345"
empRec.attrib['ssn'] = "123456789"
first = ET.SubElement(empRec,'first')
first.text = "Jack"
last = ET.SubElement(empRec,'last')
last.text = "Doe"


tree = ET.ElementTree(empRec)
tree.write(sys.stdout)



	