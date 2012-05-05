
import unittest

import fixclassnumbers as body


class TestBody(unittest.TestCase):
	def test_match(self):
		match = body.PYPY_IMPORT.match("import  pypy.")
		self.assertTrue(match is not None)
		print "Matched: ",match.group()
		
		match = body.PYPY_IMPORT.match("import xpypy.")
		self.assertTrue(match is None)
	
	def test_extractImported(self):
		res = body.extractSymbolFromImport("import pypy.ftpclient.client.Client_67;")
		self.assertEquals(res[0], "Client_67")
		res = body.extractSymbolFromImport("import XXX.ftpclient.client.Client_67;")
		self.assertTrue(res is None)
	
	def test_findClassForSymbol(self):
		FILE = "unpacked/pypy/ftpclient/client/Client_72.class"
		res = body.findClassForSymbol(
			['foo', FILE, "bar"],
			("Client_33", "client"))
		self.assertEquals(res, FILE)
		
		res = body.findClassForSymbol(
			['foo', FILE, "bar"],
			("Client_33", "zzz"))
		self.assertTrue(res is None)
	
	def test_extractSymbolFromFilename(self):
		res = body.extractSymbolFromClassFilename("unpacked/pypy/ftpclient/client/Client_72.class")
		self.assertEquals(res, "Client_72")
	
	def test_stripNumber(self):
		res = body.stripNumber("Client_72")
		self.assertEquals(res, "Client")
	
	def test_replaceSymbols(self):
		s = ["a b b c d"]
		d = {"b":"B", "c":"C"}
		res = body.replaceSymbols(s, d)
		self.assertEquals("a B B C d", res[0])
		print res[0]
		
	def test_command(self):
		print "Testing command"
		print body.command(["ls"])
		print "--1"
		print body.command(["find", ".", "-name", "*.py"])
		print "Testing command Done."

if __name__ == "__main__":
	unittest.main()
