
from ftpclient.response import *

def main():
	print "Test-response"
	lines = []
	lines.append("200 the ip is 2,3,4,5,6,7")
	response = Response(200, lines)
	print response.getDataSocket().toString()
