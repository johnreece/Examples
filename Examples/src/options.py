import sys, getopt

try:

	options,arguments = getopt.getopt(sys.argv[1:],"hf:u:",["file=","user="])
	print "Options: ",options
	print "Argument: ", arguments[0],"\n\n"
except Exception:

	print "Usage: options -h [-i --file] command"
	sys.exit()
	
for opt,arg in options:
	if opt == '-h':
		print "Option is to display help"
	if opt in ["-f","--file"]:
		print "Option is for file: ",arg
	if opt in ["-u","--user"]:
		print "Option is for user: ", arg

