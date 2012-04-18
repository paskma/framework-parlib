
from ftpclient.directory_parser import parseListing, _EXAMPLE

BORKED_EXAMPLE = (
"drwxrwxr-x  283 0        3003    12288 Aug 30 18:45 gnu\r\n"
+
"-rwxrwxr-x  283 0        3003        12288 Aug 30 18:45 just file\r\n"
+
"\r\n"
)

def main():
	print "Test-directory_parser"
	files = parseListing(_EXAMPLE)
	for i in files:
		print i.toString()
	
	print "Borked example"
	try:
		files = parseListing(BORKED_EXAMPLE)
		for i in files:
			print i.toString()
	except Exception, ex:
		print "Exception!"
		print str(ex)
