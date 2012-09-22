
from parlibutil.locking import Monitor

from statemachine_synchronization_config import USE_FAKE_SYNCHRONIZATION
if USE_FAKE_SYNCHRONIZATION:
	from parlibutil.locking import fake_synchronized as synchronized
else:
	from parlibutil.locking import synchronized

from ftpclient.responsereader import ResponseReader
from ftpclient import command as Command

from ftpclient.statemachine_decorators import *

class StateException(Exception):
	def __init__(self, message):
		self.message = message
	def toString(self): return self.message

# States are on file level to be accessible by decorators
STATE_READY = 1
STATE_CONNECTED = 2
STATE_WAITING_PASSWORD = 21
STATE_LOGGED = 3
STATE_WAITING_DATA_CONNECTION = 4
STATE_DATA_CONNECTION_ESTABLISHED = 41
STATE_TRANSFERING = 5

class StateMachine(Monitor):


	def __init__(self, net):
		Monitor.__init__(self)
		self.net = net
		self.reader = None
		self.dataSocket = None
		self.state = STATE_READY

	def _assertState(self, shouldBe):
		if self.state != shouldBe:
			print "State is %s, should be %s." % (self.state, shouldBe)
			raise StateException("State is %s, should be %s." % (self.state, shouldBe))
	
	def _assertStates(self, shouldBe, orShouldBe):
		if (self.state != shouldBe) and (self.state != orShouldBe):
			#print "State is %s, should be %s,%s." % (self.state, shouldBe, orShouldBe)
			raise StateException("State is %s, should be %s,%s." % (self.state, shouldBe, orShouldBe))


	def _assertStates3(self, shouldBe, orShouldBe, orShouldBe2):
		if (self.state != shouldBe) and (self.state != orShouldBe) and (self.state != orShouldBe2):
			#print "State is %s, should be %s,%s,%s." % (self.state, shouldBe, orShouldBe, orShouldBe2)
			raise StateException("State is %s, should be %s,%s,%s." % (self.state, shouldBe, orShouldBe, orShouldBe2))
	
	def _assertNotState(self, shouldNotBe):
		if self.state == shouldNotBe:
			print "State should not be %s" % self.state
			raise StateException("State should not be %s" % self.state)

	def _setState(self, newState):
		#print "State set to: ", newState
		self.state = newState

	@synchronized
	def getState(self):
		return self.state

	@synchronized
	@precond_state(STATE_WAITING_DATA_CONNECTION)
	def getDataSocket(self):
		return self.dataSocket

	@synchronized
	@precond_state(STATE_READY)
	@postcond_states(STATE_CONNECTED, STATE_READY)
	def connect(self, host, port):
		suc = self.net.connect(host, port)

		if suc:
			self.reader = ResponseReader(self.net.createNetworkReader())
			resp = self.reader.read()
			if resp is not None and resp.isPositiveCompletion():
				self._setState(STATE_CONNECTED)
			else:
				return False
		else:
			return False

		return suc

	@synchronized
	@precond_state(STATE_CONNECTED)
	@postcond_states3(STATE_LOGGED, STATE_WAITING_PASSWORD, STATE_CONNECTED)
	def user(self, username):
		user = Command.USER(username)
		sent = self.net.sendMessage(user.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositiveCompletion():
			self._setState(STATE_LOGGED)
			return True
		elif response is not None and response.isPositiveIntermediate():
			self._setState(STATE_WAITING_PASSWORD)
			return True

		return False

	@synchronized
	@precond_state(STATE_WAITING_PASSWORD)
	@postcond_states(STATE_LOGGED, STATE_WAITING_PASSWORD)
	def password(self, password_str):
		command = Command.PASS(password_str)
		sent = self.net.sendMessage(command.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositiveCompletion():
			self._setState(STATE_LOGGED)
			return True

		return False

	@synchronized
	@precond_state(STATE_LOGGED)
	@postcond_states(STATE_WAITING_DATA_CONNECTION, STATE_LOGGED)
	def pasv(self):
		pasv = Command.PASV()
		sent = self.net.sendMessage(pasv.toString())
		if not sent:
			return False
			
		response = self.reader.read()
		if response is not None and response.isPositiveCompletion():
			self.dataSocket = response.getDataSocket()
			self._setState(STATE_WAITING_DATA_CONNECTION)
			return True

		return False

	@synchronized
	@precond_state(STATE_WAITING_DATA_CONNECTION)
	@postcond_state(STATE_DATA_CONNECTION_ESTABLISHED)
	def dataConnectionEstablished(self):
		self._setState(STATE_DATA_CONNECTION_ESTABLISHED)

	@synchronized
	@precond_state(STATE_DATA_CONNECTION_ESTABLISHED)
	@postcond_states(STATE_TRANSFERING, STATE_DATA_CONNECTION_ESTABLISHED)
	def listing(self):
		listing = Command.LIST()
		sent = self.net.sendMessage(listing.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositivePreliminary():
			self._setState(STATE_TRANSFERING)
			return True

		return False

	@synchronized
	@precond_state(STATE_DATA_CONNECTION_ESTABLISHED)
	@postcond_states(STATE_TRANSFERING, STATE_DATA_CONNECTION_ESTABLISHED)
	def retr(self, filename):
		retr = Command.RETR(filename)
		sent = self.net.sendMessage(retr.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositivePreliminary():
			self._setState(STATE_TRANSFERING)
			return True

		return False
	
	@synchronized
	@precond_state(STATE_LOGGED)
	@postcond_state(STATE_LOGGED)
	def dele(self, filename):
		dele = Command.DELE(filename)
		sent = self.net.sendMessage(dele.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositiveCompletion():
			return True

		return False

	@synchronized
	@precond_state(STATE_TRANSFERING)
	@postcond_states(STATE_LOGGED, STATE_TRANSFERING)
	def transferSuccessfullyDone(self):
		response = self.reader.read()

		if response is not None and response.isPositiveCompletion():
			self._setState(STATE_LOGGED)
			return True

		return False

	@synchronized
	@precond_states3(STATE_WAITING_DATA_CONNECTION, STATE_TRANSFERING, STATE_DATA_CONNECTION_ESTABLISHED)
	@postcond_state(STATE_LOGGED)
	def dataConnectionClearAfterError(self):
		self._setState(STATE_LOGGED)

	@synchronized
	@precond_state(STATE_LOGGED)
	@postcond_state(STATE_LOGGED)
	def cwd(self, directory):

		cwd = Command.CWD(directory)
		sent = self.net.sendMessage(cwd.toString())
		if not sent:
			return False
		response = self.reader.read()
		
		if response is not None and response.isPositiveCompletion():
			return True

		return False
	
	@synchronized
	@precond_state_inverse(STATE_READY) # this command is valid in all states except ready
	@postcond_state_any
	def quit(self):
		quit = Command.QUIT()
		sent = self.net.sendMessage(quit.toString())
		if not sent:
			return False
		response = self.reader.read()

		if response is not None and response.isPositiveCompletion():
			self._setState(STATE_READY)
			return True

		return False
