from sys import argv

from parlib.directive import POSIX

#    The Computer Language Benchmarks Game
#    http://shootout.alioth.debian.org/

#    contributed by Isaac Gouy
#    converted to Java by Oleg Mazurov
#    converted to Python by Buck Golemon
#    modified by Justin Peel

def fannkuch(n):
	maxFlipsCount = 0
	permSign = True
	checksum = 0

	perm1 = range(n)
	count = perm1[:]
	rxrange = xrange(2, n - 1)
	nm = n - 1
	while 1:
		k = perm1[0]
		if k:
			perm = perm1[:]
			flipsCount = 1
			kk = perm[k]
			while kk:
				#perm[:k+1] = perm[k::-1]
				Q = 0
				L = k
				while Q <= L:
					T = perm[Q]
					perm[Q] = perm[L]
					perm[L] = T
					Q += 1
					L -= 1
				
				flipsCount += 1
				k = kk
				kk = perm[kk]
			if maxFlipsCount < flipsCount:
				maxFlipsCount = flipsCount
			if permSign:
				checksum += flipsCount
			else:
				checksum += -flipsCount

		# Use incremental change to generate another permutation
		if permSign:
			perm1[0],perm1[1] = perm1[1],perm1[0]
			permSign = False
		else:
			perm1[1],perm1[2] = perm1[2],perm1[1]
			permSign = True
			for r in rxrange:
				if count[r]:
					break
				count[r] = r
				perm0 = perm1[0]
				perm1[:r+1] = perm1[1:r+2]
				perm1[r+1] = perm0
			else:
				r = nm
				if not count[r]:
					#print( checksum )
					return maxFlipsCount
			count[r] -= 1

def main(argv):				
	try:
		N = int(argv[1])
	except:
		N = 8
	x = fannkuch(N)
	print N, " ", x

if __name__ == "__main__":
	from sys import argv
	main(argv)

def entry_point(argv):
	if POSIX:
		from parlib.rthreading import init_threads
		init_threads()
	main(argv)
	return 0

def target(*argv):
	return entry_point, None
