import urllib,urllib2

url = "http://www.dummy.com/?"
query = { 'q' : 'whatsupdoc', 'foo' : 'bar' }
encoded_query = urllib.urlencode(query)
url = url + encoded_query
print url