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
	symbolsWithoutContext = [i[0] for i in sourceSymbols]
	print "Symbols (%s): " % len(sourceSymbols), ", ".join(symbolsWithoutContext)
	
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
			s = s.replace(j[0], replaceDict[j])
		result.append(s)
	
	return result
			

def gatherSymbolsToReplace(lines):
	result = []
	for line in lines:
		symbol = extractSymbolFromImport(line)
		if symbol:
			result.append(symbol)
	
	return result

def findReplacements(pyclassdir, symbols):
	result = {}
	classFiles = loadClassList(pyclassdir).split("\n")
	for i in symbols:
		classFilename = findClassForSymbol(classFiles, i)
		if not classFilename:
			print "Warning, no filename for symbol", i
		else:
			replacement = extractSymbolFromClassFilename(classFilename)
			print "Replacement %s->%s added." % (i, replacement)
			result[i] = replacement
	
	return result;
			
def findClassForSymbol(classFiles, symbol):
	for i in classFiles:
		if i.find("/" + symbol[1] + "/" + stripNumber(symbol[0])) != -1:
			return i
	
	return None

PYPY_IMPORT = re.compile('import\s*pypy\.')

def extractSymbolFromImport(line):
	match = PYPY_IMPORT.match(line)
	if not match:
		return None
	
	lastDot = line.rindex(".")
	lastSemicolon = line.rindex(";")
	penultimateDot = line.rindex(".", 0, lastDot - 1)
	context = line[penultimateDot+1:lastDot]
	return (line[lastDot+1:lastSemicolon], context)
	

def loadClassList(pyclassdir):
	cmd = ["find", pyclassdir, "-name", "*.class"]
	return command(cmd)

def extractSymbolFromClassFilename(filename):
	if not filename:
		return None
	
	last = filename.rindex(".class")
	result = filename[filename.rindex("/")+1:last]
	
	return result

def stripNumber(symbol):
	last = symbol.rindex("_");
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
