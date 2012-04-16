
class _Bootstrapper:

	def bootstrap():
		pass
	
	bootstrap = staticmethod(bootstrap)

boot = _Bootstrapper()

class Thread:
	def __init__(self):
		pass
	
	def release_bootlock(self):
		pass
	
	def start(self):
		self.RUN()
		
	def RUN(self):
		pass
