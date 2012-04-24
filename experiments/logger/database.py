
class Database:
	def writeInterval(self, device, eventType, value):
		print "INSERT(dev %s,type %s,val %s)" % (device, eventType, value)
	def insertAlarm(self):
		print "INSERT ALARM"
