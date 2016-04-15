#!/usr/bin/env python3

from bitwise_manipulations import *
from math import isinf
from helper import *
import json, time

choice = 2
a = []
random_size = 20
def choose(n):
	global a, random_size
	if n == 1:
		a = getInputFromUser()
	if n == 2:
		a = generateGraph(random_size)
	if n == 3:
		a = readFromFile()
choose(choice)

# a = [
# 		[0, 10, 15, 20],
# 		[5, 0, 9, 10],
# 		[6, 13, 0, 12],
# 		[8, 8, 9, 0]
# ]

n = len(a)

def generateSubsets(n):
	l = []
	for i in range(2**n):
		l.append(i)
	return sorted(l, key = lambda x : size(x) )

l = generateSubsets(n)
cost = [ [-1 for city in range(n)] for subset in l]
p = [ [-1 for city in range(n)] for subset in l]

pretty(a)
t1 = time.time()
count = 1
total = len(l)
for subset in l:
	for dest in range(n):
		if not size(subset):
			cost[subset][dest] = a[0][dest]
			#p[subset][dest] = 0
		elif (not inSubset(0, subset)) and (not inSubset(dest, subset)) :
			mini = float("inf")
			for i in range(n):
				if inSubset(i, subset):
					modifiedSubset = remove(i, subset)
					val = a[i][dest] + cost[modifiedSubset][i]
					
					if val < mini:
						mini = val
						p[subset][dest] = i

			if not isinf(mini):
				cost[subset][dest] = mini
	print("%d %%" % (count / total))
	count += 1
path = findPath(p)
t2 = time.time()
diff = t2 - t1
print(" => ".join(path))

Cost = cost[2**n-2][0]
print(Cost)
print(diff * 1000)