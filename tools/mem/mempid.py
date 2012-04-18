#!/usr/bin/python

"""
		Prints the maxumum for every field.
		If MEMPIDCSV environment is set, then CSV is generated.
"""

import os
from time import sleep
import sys

_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
		  'KB': 1024.0, 'MB': 1024.0*1024.0}

def _VmB(proc_status, VmKeys):
	'''Private.
	'''
	global _proc_status, _scale
	 # get pseudo file  /proc/<pid>/status
	try:
		t = open(proc_status)
		v = t.read()
		t.close()
	except IOError:
		#return (0.0, 0.0, 0.0)  # non-Linux?
		raise
	
	result = []
	for VmKey in VmKeys:
		# get VmKey line e.g. 'VmRSS:  9999  kB\n ...'
		try:
			i = v.index(VmKey)
			vx = v[i:].split(None, 3)  # whitespace
			if len(vx) < 3:
			    return 0.0  # invalid format?
			 # convert Vm value to bytes
			result.append(float(vx[1]) * _scale[vx[2]])
		except ValueError:
			result.append(0)
	return result

def main(pid, count, csv):
	proc_status = '/proc/%s/status' % pid
	keys = ['VmSize:', 'VmRSS:', 'VmLib:', 'VmStk:', 'VmData:', 'VmExe:', 'VmSwap:']
	values = []
	for i in range(len(keys)):
		values.append([])

	probecount = 0
	try:
		for i in xrange(count):
			probe = _VmB(proc_status, keys)
			for j in range(len(keys)):
				values[j].append(probe[j])
			if probecount % 4 == 0: print >> sys.stderr, probe
			probecount += 1
			sleep(0.5)		
	except IOError:
		if probecount == 0:
			print >> sys.stderr, "Target prematurely ended."
		else:
			print >> sys.stderr, "Target ended."
		

	if probecount > 0:
		result = ""
		if csv:
			#result = ";".join(keys)
			#result += "\n"
			result += ";".join([str(max(i)) for i in values])
		else:
			for i in range(len(keys)):
				result += keys[i] + str(max(values[i])/1024) + " K    "
		print result

if __name__ == "__main__":
	from sys import argv
	pid = int(argv[1])
	count = 1
	if len(argv) == 3:
		count = int(argv[2])
	csv = "MEMPIDCSV" in os.environ.keys()
	main(pid, count, csv)
