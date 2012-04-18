
from ftpclient.command import *

def main():
	print "Test-command"
	user = USER("username")
	print user.toString()
	pasv = PASV()
	print pasv.toString()
	retr = RETR("a_file.txt")
	print retr.toString()
	
