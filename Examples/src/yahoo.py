import urllib,urllib2
# All industry list is t http://biz.yahoo.com/ic/ind_index.html
url = 'http://finance.yahoo.com/d/quotes.csv?'
# format is ticker, price, 50-day mavg, 200-day mavg, volume, p/e, peg, short interest,ex-div date, div yield
query = {'s':'DIA+SPY+QQQ', 'f':'sl1m3m4vr2r5s7qy' }
encoded_query = urllib.urlencode(query)
get_url = url + encoded_query
request = urllib2.Request(get_url)
response = urllib2.urlopen(request)
print response.read()