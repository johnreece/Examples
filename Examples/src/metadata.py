from BeautifulSoup import BeautifulSoup as BS
import sys

fh = open(sys.argv[1])
html = fh.read()
soup = BS(html)

title = soup.findAll('title')
print "TITLE:       %s" % title[0].text
metadata = soup.findAll('meta')
for item in metadata:
	if item['name'] == 'author':
		print "AUTHOR:      %s" % item['content']
	if item['name'] == 'keywords':
		print "KEYWORDS:    %s" % item['content']
	if item['name'] == "description":
		print "DESCRIPTION: %s" % item['content']