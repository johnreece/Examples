import sys
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET
# Create the root element
employees = ET.Element('employees')
# Create the first employee record
empRec = ET.SubElement(employees,'person')
empRec.attrib['empid'] = "12345"
empRec.attrib['ssn'] = "123456789"
first = ET.SubElement(empRec,'first')
first.text = "Jack"
last = ET.SubElement(empRec,'last')
last.text = "Doe"

# Add another blank employee record to quickly illustrate 
# extending the doc

empRec2 = ET.SubElement(employees,'person')

tree = ET.ElementTree(employees)
tree.write(sys.stdout)



	