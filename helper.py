from bitwise_manipulations import *
import time
import random, json


def inSubset(i, s):
	while i > 0 and s > 0:
		s = s >> 1
		i -= 1
	cond = s & 1
	return cond

def remove(i, s):
	x = 1
	x = x << i
	l = length(s)
	l = 2 ** l - 1
	x = x ^ l
	#print ( "i - %d x - %d  s - %d x&s -  %d " % (i, x, s, x & s) )
	return x & s

def findPath(p):
	n = len(p[0])
	number = 2 ** n - 2
	prev = p[number][0]
	while prev != -1:
		print(prev)
		number = remove(prev, number)
		prev = p[number][prev]

def pretty(a):
	print("=========================")
	for i in range(len(a)):
		for j in range(len(a[0])):
			print "%2d"%(a[i][j]),
		print("")
	print("=========================")

def generateGraph(n):
	a = [ [-1 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			rand = random.randint(0, n)
			if a[i][j] < 0:
				a[i][j] = rand
				a[j][i] = rand
			if i == j:
				a[i][i] = 0
				
	#pretty(a)
	return a

def getInputFromUser():
	n = int(input("Enter number of cities:"))
	a = [[int(input()) for i in range(n)] for j in range(n)]
	print(a)
	return a

def readFromFile():
	with open('input.json', 'r') as f:
		s = f.read()
		data  = json.loads(s)
		print(data)