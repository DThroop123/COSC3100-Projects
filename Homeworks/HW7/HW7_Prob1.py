"""
HW7_Prob1.py - using dynamic programmming to determine the number of ordered ways to make change for one dollar using 25, 10, 5, and 1 cent coins.
Date - -03/26/21 
Author - Daniel Throop
Class - COSC 3100

"""

import functools

@functools.cache
def ways(n):
	# pennies
	if n < 5:
		return 1
	else:
		return ways(n-1) + ways(n-5) + ways(n-10) + ways(n-25)

# find the number of ways to make change for 1 dollar 
print(ways(1000))
