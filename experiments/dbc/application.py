def make_wrapped_call(func, pre):
    def wrapped(*args):
        pre(*args)
        return func(*args)
    return wrapped
    
class DbcWeaver(type):
    def __init__(cls, clsname, bases, dict):
        super(DbcWeaver, cls).__init__(clsname, bases, dict)

        for name in dict.keys():
            func = dict[name]
            if not callable(func): continue

            try:
                pre = dict[name + '__pre']
            except KeyError:
                continue

            setattr(cls, name, make_wrapped_call(func, pre))

class Math:
    __metaclass__ = DbcWeaver
    
    def factorial__pre(self, n):
        assert n >= 0
    
    def factorial(self, n):
        result = 1
        for i in xrange(2, n+1):
            result *= i
        return result

class Application:
	def main(self, argv):
		fact = Math().factorial
		print "fact(0) is"
		print fact(0)
		print "fact(1) is"
		print fact(1)
		print "fact(5) is"
		print fact(5)
		print "fact(-1) is out of contract, expecting an exception..."
		print fact(-1)
		print "Done."
		return 0
