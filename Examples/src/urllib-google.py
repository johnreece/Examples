# Importing the module
import urllib,urllib2
 
# Define the url
url = 'http://www.google.com/#q=my_search'
url =  'http://www.google.com/#'
query = { 'q' : 'python' }
url = url+urllib.urlencode(query)

# Create the Request. 
request = urllib2.Request(url)
request.add_header( 'User-Agent' , 'Mozilla 5.10' )
 
# Getting the response
response = urllib2.urlopen(request)
 
# Print the headers
print response.headers