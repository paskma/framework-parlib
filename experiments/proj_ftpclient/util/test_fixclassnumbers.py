
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
		res = body.extractImportedPyPyClass("import pypy.ftpclient.client.Client_67;")
		self.assertEquals(res, "Client_67")
		res = body.extractImportedPyPyClass("import XXX.ftpclient.client.Client_67;")
		self.assertTrue(res is None)
	
	def test_extractSymbolFromFilename(self):
		res = body.extracSymbolFromClassFilename("unpacked/pypy/ftpclient/client/Client_72.class")
		self.assertEquals(res, "Client_72")

if __name__ == "__main__":
	unittest.main()
