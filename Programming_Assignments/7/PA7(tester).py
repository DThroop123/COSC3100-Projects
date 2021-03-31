"""
PA7.py - implementing LH Hashing with matplotlib
Date - -03/19/21 
Author - Daniel Throop
Class - COSC 3100

"""

import numpy as np
import matplotlib.pyplot as plt
import random

def address(c, level, split):
	a = c % (2**level)
	if a < split:
		a = c % (2 ** (level + 1))
	return a

def linearHash():
	buckets = [0 for _ in range(150)]
	# insert 1000 random records
	for _ in range(2000000):
		# increment count by 1 in specific bucket
		buckets[address(random.getrandbits(32), 7, 22)] += 1
	return buckets

def display(bins):
    plt.bar( range(0,len(bins)), bins)
    plt.title('LH - 150 buckets with l = 7 and sp = 22 (2000000 random records)')
    plt.show()

# display the counts in the buckets
display(linearHash())
