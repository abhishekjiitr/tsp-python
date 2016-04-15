import math

a = [4, 2, 3, 5, 6, 1]
mini = float("inf")
print(math.isinf(mini))
for val in a:
	print( mini )
	if mini > val:
		mini = val
