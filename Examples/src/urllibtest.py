import urllib, urllib2

url = "http://www.pythonforbeginners.com"
htmlfile = "download.html"

request = urllib2.Request(url)
request.add_header('User-agent: ", "Urllib tester")
response = urllib2.urlopen(request)
html = response.read()
print html

fh = open(htmlfile,'w')
fh.write(html)
fh.close