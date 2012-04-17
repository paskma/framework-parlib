
def create_new_bucket(i):
	#return "_" * i
	result = range(i)
	result[i/2] = 123
	return result

def main(argv):
	history = []
	history_size = 100
	n = 100000
	bucket_sizes = [1, 1000, 100000]
	bucket_sizes_len = len(bucket_sizes)
	for i in xrange(history_size):
		#history.append("")
		history.append([])
		
	for i in xrange(n):
		new_bucket = create_new_bucket(bucket_sizes[i % bucket_sizes_len])
		history[i % history_size] = new_bucket
	
	check = history_size / 2
	print len(history[check])
	print len(history[check + 1])
	print len(history[check + 2])
		
		
	
