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
	f = open(jfile, "r")
	lines = f.readlines()
	f.close()
	
		
	sourceSymbols = gatherSymbolsToReplace(lines)
	print "Symbols ", ", ".join(sourceSymbols)
	
	replaceDict = findReplacements(pyclassdir, sourceSymbols)
	result = replaceSymbols(lines, replaceDict)
	
	f = open(jfile, "w")
	f.write("".join(result))
	f.close()

def replaceSymbols(lines, replaceDict):
	result = []
	for i in lines:
		s = i
		for j in replaceDict:
			s = s.replace(j, replaceDict[j])
		result.append(s)
	
	return result
			

def gatherSymbolsToReplace(lines):
	result = []
	for line in lines:
		symbol = extractImportedPyPyClass(line)
		if symbol:
			result.append(symbol)
	
	return result

def findReplacements(pyclassdir, symbols):
	result = {}
	for i in symbols:
		classFilename = findClassForSymbol(pyclassdir, stripNumber(i))
		if not classFilename:
			print "Warning, no filename for symbol", i
		else:
			replacement = extractSymbolFromClassFilename(classFilename)
			print "Replacement %s->%s added." % (i, replacement)
			result[i] = replacement
	
	return result;
			

PYPY_IMPORT = re.compile('import\s*pypy\.')

def extractImportedPyPyClass(line):
	match = PYPY_IMPORT.match(line)
	if not match:
		return None
	
	lastDot = line.rfind(".")
	lastSemicolon = line.rfind(";")
	return line[lastDot+1:lastSemicolon]
	
def findClassForSymbol(pyclassdir, symbol):
	"""find unpacked/pypy -name "Client_*.class"""
	cmd = ["find", pyclassdir, "-name", "%s_*.class" % symbol]
	return command(cmd)

def extractSymbolFromClassFilename(filename):
	if not filename:
		return None
	
	last = filename.rfind(".class")
	result = filename[filename.rfind("/")+1:last]
	
	return result

def stripNumber(symbol):
	last = symbol.rfind("_");
	if last == -1:
		return symbol
	
	return symbol[0:last]
	

def command(tokens):
	p = subprocess.Popen(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out
	


if __name__ == "__main__":
	from sys import argv
	main(argv)
