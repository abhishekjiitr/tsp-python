#!/usr/bin/env python3

from bitwise_manipulations import *
from helper import *
import json

choice = 3
a = []

def choose(n):
	global a
	if n == 1:
		a = getInputFromUser()
	if n == 2:
		a = generateGraph(4)
	if n == 3:
		a = readFromFile()
choose(choice)

a = [
		[0, 10, 15, 20],
		[5, 0, 9, 10],
		[6, 13, 0, 12],
		[8, 8, 9, 0]
]

n = len(a)

def generateSubsets(n):
	l = []
	for i in range(2**n):
		#print bin(i)
		l.append(i)
	return sorted(l, key = lambda x : size(x) )

l = generateSubsets(n)
cost = [ [-1 for city in range(n)] for subset in l]
p = [ [-1 for city in range(n)] for subset in l]

pretty(a)

for subset in l:
	for dest in range(n):
		print("Subset: %s Dest: %d" % (bin(subset), dest))
		if not size(subset):
			cost[subset][dest] = a[0][dest]
			#p[subset][dest] = 0
		elif (not inSubset(0, subset)) and (not inSubset(dest, subset)) :
			isSet = 0
			mini = 0
			for i in range(n):
				if inSubset(i, subset):
					modifiedSubset = remove(i, subset)
					print("Subset is %d => Modified %d" % (subset, modifiedSubset))
					val = a[i][dest] + cost[modifiedSubset][i]
					print("i is %d a[i][dest] = %d cost = %d modifiedS = %d"%(i, a[i][dest], cost[modifiedSubset][i], modifiedSubset))
					print("Val = %d" % (val))
					print(mini)

					if isSet == 0:
						mini = val
						isSet = 1
						p[subset][dest]=i
					else:
						if val<mini:
							val= mini
							p[subset][dest] = i
					print(mini)
			cost[subset][dest] = mini
			print("Setting Value of %s, %d => %d" % (bin(subset), dest, mini))
		pretty(cost)


# pretty(p)
# findPath(p)
pretty(cost)