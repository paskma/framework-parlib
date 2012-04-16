

def p(s, klass="all"):
		print s

def test():
	p("single")
	p("p" + " test")
	p("not avail!!")
	p("next line" + " 2")

if __name__ == "__main__":
	test()
	
def entry_point(argv):
	test()
	return 0

def target(*args):
	return entry_point, None
