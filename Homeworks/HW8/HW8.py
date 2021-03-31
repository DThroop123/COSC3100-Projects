"""
HW8.py - using dynamic programmming to determine the number of unordered ways to score a total number of points in American football.
Date - -03/26/21 
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
print(ways(120, 3))