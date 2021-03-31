"""
HW7_Prob2.py - using dynamic programmming to determine the number of unordered ways to make change for one dollar using 25, 10, 5, and 1 cent coins.
Date - -03/26/21 
Author - Daniel Throop
Class - COSC 3100

"""

import functools

values = [1, 5, 10, 25]

@functools.cache
def ways(n, i):
	if i == 3: #quarters, dimes, nickels, pennies
		result = 0
		for q in range(0, n//values[i]+1):
			result += ways(n-q*values[i], i-1)
		return result
	if i == 2: #dimes, nickles, pennies
		result = 0
		for d in range(0, n//values[i]+1):
			result += ways(n-d*values[i], i-1)
		return result
	if i == 1: #nickels, pennies
		result = 0
		for ni in range(0, n//values[i]+1):
			result += ways(n-ni*values[i], i-1)
		return result
	if i == 0: #pennies
		return 1


# find the number of ways to make change for a dollar (unordered)
print(ways(100, 3))