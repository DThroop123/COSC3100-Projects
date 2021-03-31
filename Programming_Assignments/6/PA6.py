"""
PA6.py - implementing a bloom filter
Date - -03/10/21 
Author - Daniel Throop
Class - COSC 3100

"""

import numpy as np
import random
LENGTH = 4096
MASK = 0xfff

def hasher5(ix):
	return (17377*ix**2>>4)&MASK, ((17377*(ix+5)**2)>>8)&MASK,((10607*(ix+7)**2)>>2)&MASK, ((21193*(ix+9)**2)>>12)&MASK, ((35527*(ix+11)**2)>>10)&MASK 

class Bloom:
	def __init__(self, LENGTH, MASK, hasher):
		self.length = LENGTH
		self.mask = MASK
		self.array = np.zeros(LENGTH, dtype = bool)
		self.hasher = hasher

	def insert(self, x):
		# returns indices to insert number into bloom filter
		indices = hasher5(x)
		# sets specific indices equal to True 
		self.array[indices[0]] = True
		self.array[indices[1]] = True
		self.array[indices[2]] = True
		self.array[indices[3]] = True
		self.array[indices[4]] = True
		print("Inserted: " + str(x))

	def look_up(self, x):
		# returns indices to look up number in bloom filter
		indices = hasher5(x)
		if(np.all([self.array[indices[0]], self.array[indices[1]], self.array[indices[2]], self.array[indices[3]], self.array[indices[4]]])):
			# number is probably in bloom filter
			return True
		# the number is not in the bloom filter
		return False

# creating bloom filter
my_bloom = Bloom(LENGTH, MASK, hasher5)

# inserting 200 random integers
for i in random.sample(range(my_bloom.length), 200):
	my_bloom.insert(i)

print("200 random integers inserted.")

# generate 100000 random integers to check false positive rate
count = 0
for i in range(100000):
	x = random.randint(200, 10000000)
	if(my_bloom.look_up(x)):
		count += 1

# print number of false positives
print("Number of false positives: " + str(count))








