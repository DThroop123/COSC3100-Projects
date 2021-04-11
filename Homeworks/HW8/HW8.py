"""
HW8.py - using dynamic programmming to determine the number of unordered ways to score a total number of points in American football.
Date - -03/31/21 
Author - Daniel Throop
Class - COSC 3100

"""

import functools

values = [2, 3, 6, 7]

@functools.cache
def ways(n, i):
	if i == 3: # td w/ conversion, td w/o conversion, fg, and safety
		result = 0
		for tdc in range(0, n//values[i]+1):
			result += ways(n-tdc*values[i], i-1)
		return result
	if i == 2: # td w/o conversion, fg, and safety
		result = 0
		for td in range(0, n//values[i]+1):
			result += ways(n-td*values[i], i-1)
		return result
	if i == 1: # fg, and safety
		result = 0
		for fg in range(0, n//values[i]+1):
			result += ways(n-fg*values[i], i-1)
		return result
	if i == 0: # safeties
		return values[i]

# find the number of ways to score for 120 points
# print(ways(120, 3))

# find the number of ways to score for 1-120 points
for i in range(1, 11):
	print(str(i) + ': ' + str(ways(i, 3)))
print("...")
for i in range(110, 121):
	print(str(i) + ': ' + str(ways(i, 3)))

# change value of field goal to 4

values2 = [2, 4, 6, 7]

@functools.cache
def ways2(n, i):
	if i == 3: # td w/ conversion, td w/o conversion, fg, and safety
		result = 0
		for tdc in range(0, n//values2[i]+1):
			result += ways2(n-tdc*values2[i], i-1)
		return result
	if i == 2: # td w/o conversion, fg, and safety
		result = 0
		for td in range(0, n//values2[i]+1):
			result += ways2(n-td*values2[i], i-1)
		return result
	if i == 1: # fg, and safety
		result = 0
		for fg in range(0, n//values2[i]+1):
			result += ways2(n-fg*values2[i], i-1)
		return result
	if i == 0: # safeties
		return values2[i]

# find the number of ways to score for 120 points
# print(ways2(120, 3))

print("Value of field goal changed to 4.")

# find the number of ways to score for 1-120 points
for i in range(1, 11):
	print(str(i) + ': ' + str(ways2(i, 3)))
print("...")
for i in range(110, 121):
	print(str(i) + ': ' + str(ways2(i, 3)))








