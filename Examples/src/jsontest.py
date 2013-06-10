import json

staff = { "employees" : [
			{ "person" : 
					[ {"first" : "Joseph", "last" : "Blow" } ]
			},
			{	 "person" :
					[ {"first" : "Joe", "last" : "Doakes" } ]
			},
			{  "person" :
					[  {"first" : "Jane", "last" : "Doe" } ]
			}
					] 
		}

# a json structure is a dictionary containing a list containing dictionaries, each containing a list
# containing dictionaries, each containing a list...so alternate string and integer indices.
s =  staff["employees"][1]['person'][0]["last"]
print s, "\n"
for p in staff["employees"]:
	print p["person"][0]["first"], " ", p["person"][0]["last"]

