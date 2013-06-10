import urllib,urllib2

url = "http://www.google.com/?"
query = { 'q' : 'whatsupdoc' }
encoded_query = urllib.urlencode(query)
get_url = url + encoded_query
request = urllib2.Request(get_url)
request.add_header('User-agent: ',  'Mozilla 5.10')
response = urllib2.urlopen(request)
# read also takes a parameter for number of bytes to read
print response.read()