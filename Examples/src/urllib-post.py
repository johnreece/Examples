import urllib,urllib2

url = 'http://www.google.com/'
query = { 'q' : 'sowhat', 'foo' : 'bar' }
encoded_query = urllib.urlencode(query)
request = urllib2.Request(url,encoded_query)
request.add_header('User-agent: ', 'Test')
try:
	response = urllib2.urlopen(request)
except urllib2.HTTPError:
	print response.headers

