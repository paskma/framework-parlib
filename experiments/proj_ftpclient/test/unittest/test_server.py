from server import Server

def main():
	print "Test-server"
	server = Server()
	server.connectToCommand()
	print server.reply()

if __name__ == "__main__":
	main()
