import xml.etree.cElementTree as ET
tree = ET.ElementTree(file="branch.xml")
root = tree.getroot()
try: 
	for child in root:
		print child.tag,child.attrib,child.text
	# More elaborate
	for child in root:
		print "NAME: %-12s HASH: %-8s TEXT: %s" % (child.attrib['name'],child.attrib['hash'],child.text.strip()
) 
	# Use iter() to do complete depth-first traversal

	for element in tree.iter():
		print element.tag,element.attrib,element.text
except Exception:
	pass

	