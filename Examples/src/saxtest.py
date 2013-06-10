import xml.sax  as sax


class MyHandler(sax.ContentHandler):
	global tmpRow
	def __init__(self):
		global tmpRow
		sax.ContentHandler.__init__(self)
		tmpRow = []
	def startElement(self, tagname, attrs):
		#print "Element: " + tagname + ": ",
		global tmpRow
		if tagname == "person":
			tmpRow.append(attrs.getValue("ssn"))
			tmpRow.append(attrs.getValue("empid"))
		#	print "Element: %s: ssn=%s empid=%s" % (tagname,attrs.getValue("ssn"),attrs.getValue("empid")),
	def endElement(self, tagname):
		global tmpRow
		if tagname == "person":
			# If xml->sql would do it here
			print "%s %s %s %s" % (tmpRow[0],tmpRow[1],tmpRow[2],tmpRow[3])
			tmpRow = []
	def characters(self,content):
		global tmpRow
		if content != '\n':
			tmpRow.append(content)
		#print content,
try:

	if __name__ == "__main__":
		source = open("employee.xml")
		sax.parse(source,MyHandler())
		
except Exception, arg:
	print "Oops: %s" % arg
finally:
	print "Buh-bye!"