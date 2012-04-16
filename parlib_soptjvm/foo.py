
def bar(x):
	print "Should not be here.1"
	pass

def start_new_thread():
	print "Should not be here.2"
	pass

def allocate_lock():
	print "Should not be here.3"
	return 0

def acquire_lock(lockNum):
	print "Should not be here.4"
	pass

def release_lock(lockNum):
	print "Should not be here.5"
	pass

def acquire_boot_lock():
	print "Should not be here.6"
	pass

def release_boot_lock():
	print "Should not be here.7"
	pass

def dumpln(s):
	print "Should not be here.8"
	pass

def jpf_random(i):
	print "Should not be here.9"
	return 1

def jpf_begin_atomic():
	print "Should not be here.10"
	pass

def jpf_end_atomic():
	print "Should not be here.11"
	pass

def simplenet_connect(hostname, port):
	print "Should not be here.12"
	return -1
	
def simplenet_read(slotnumber):
	print "Should not be here.13"
	return -1
	
def simplenet_close(slotnumber):
	print "Should not be here.14"
	return -1
	
def simplenet_write_buf(slotnumber, buf):
	print "Should not be here.15"
	return -1
	
def simplenet_write_char(slotnumber, character):
	print "Should not be here.16"
	return -1
	
def simplenet_flush(slotnumber):
	print "Should not be here.17"
	return -1
	
def simplenet_set_timeout(slotnumber, timeoutmillis):
	print "Should not be here.18"
	return -1
	
def simplecon_get_char():
	print "Should not be here.19"
	return -1






