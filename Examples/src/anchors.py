from BeautifulSoup import BeautifulSoup as BS
import sys

script,filename  = sys.argv
fh = open(sys.argv[1])
html = fh.read()
soup = BS(html)
anchors = soup.findAll("a")
for link in anchors:
	print "HREF: %-25s  TEXT: %-s\n" % (link['href'],link.text)