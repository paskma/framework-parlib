from parlibutil.reflect import clone_function

class Displayable:
	_mixin_ = True

	def display(self):
		print "value = ", self.value

class Addable:
	_mixin_ = True
                                       
	def add(self,x):
		return self.value + x

                                                                            
class Number(Displayable,Addable):
	def __init__(self, value):
		self.value = value

class String(Displayable,Addable):
	def __init__(self, value):
		self.value = value

def interface_test(aDisplayable):
	"""Unable to translate directly, needs base class.
	Mixins cannot be used as interface.
	Function can be cloned, however"""
	aDisplayable.display()

i_t = interface_test
i_t2 = clone_function("i_t2", i_t)

def demo():
	n = Number(40)
	s = String("Hello ")                   
	print n.add(2)         # 42   
	print s.add("world!")  # Hello world
	n.display()            # value = 40
	s.display()            # value = Hello is not limited to, exec, nested scopes, and metaclasses.
	i_t(n)
	i_t2(s)

class Application:
	def main(self, argv):
		demo()
		return 0
