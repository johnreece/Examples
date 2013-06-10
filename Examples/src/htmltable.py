from BeautifulSoup import BeautifulSoup as BS
import sys

scriptname, filename = sys.argv

fh = open(sys.argv[1])
html = fh.read() 
soup = BS(html)
#print soup.prettify()

tables = soup.findAll('table')

print "The raw table:\n\n" ,  tables[1] , "\n" 

print "The parsed table data:\n"
rows = tables[1].findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        data = td.find(text=True)
        print data + " | ",
        print
