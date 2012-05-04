#!/usr/bin/python

import subprocess
import re

def main(argv):
	if len(argv) != 3:
		print "Usage: ./fixclassnumbers.py javafile_to_fix pypy_class_dir"
		return
	
	jfile = argv[1]
	pyclassdir = argv[2]
	fixclassnumbers(jfile, pyclassdir)

def fixclassnumbers(jfile, pyclassdir):
	lines = File(jfile).readlines()
	replacable = {}
	for line in lines:
		symbol = extractImportedPyPyClass(line)
		if symbol: pass

PYPY_IMPORT = re.compile('import\s*pypy\.')

def extractImportedPyPyClass(line):
	match = PYPY_IMPORT.match(line)
	if not match:
		return None
	
	lastDot = line.rfind(".")
	return line[lastDot+1:len(line)-1]
	
def findClassForSymbol(pyclassdir, symbol):
	"""find unpacked/pypy -name "Client*.class"""
	return command("find", "pyclassdir", "-name", "'%s*.class'" % symbol)

def extracSymbolFromClassFilename(filename):
	if not filename:
		return None
	
	return filename[filename.rfind("/")+1:len(filename)-len(".class")]
	

def command(tokens):
	p = subprocess.Popen(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out
	


if __name__ == "__main__":
	from sys import argv
	main(argv)
