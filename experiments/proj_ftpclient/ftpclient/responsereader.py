from ftpclient.response import Response

class ResponseReader:

	# Prevend DoS
	MAX_LINES = 64*1024

	def __init__(self, net):
		self.net = net

	def read(self):
		lines = []

		line = self.net.readLine()

		if line is None:
			return None

		if len(line) < 3:
			return None

		lines.append(line)
		print "recv: ", line

		code = int(line[0:3])

		counter = 0
		while (len(line) > 3) and (line[3] == '-'):
			line = self.net.readLine()
			if line is None:
				return None
				
			lines.append(line)
			counter += 1
			
			if counter == ResponseReader.MAX_LINES:
				# it is better to signal error than return incomplete response
				return None
			
			print "recv: ", line

		return Response(code, lines);
