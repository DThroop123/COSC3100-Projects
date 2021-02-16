"""
PA3.py - Using backtracking to find a BIBD with ten blocks of length three on six elements (6,3,2).
Date - 11/18/20 
Author - Daniel Throop
Class - COSC 3100

"""

import time
import math

# data structure to hold execution times
times = [0]*20 

# BIBD conditions
nr_blocks = 10
pts_per_block = 3
nr_elements = 6
distinct = 2
blks_with_point = 5

blocks = [pts_per_block*[0] for _ in range(nr_blocks)]

# should work (not tested)
def is_complete(blocks):
    for block in range(10):
        for i in range(3):
            if blocks[block][i] == 0:
                return False
    return True

# both conditions tested and working
def is_valid(blocks):
	# count data structures
	elCount = [0]*nr_elements
	pairs = {"12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "23": 0, "24": 0, "25": 0, "26": 0, "34": 0, "35": 0, "36": 0, "45": 0, "46": 0, "56": 0}

	# check that an element appears exactly 5 times in different blocks
	for block in range(10):
		for i in range(3):
			# if the given position isn't a zero we want to investigate it
			if blocks[block][i] != 0:
				# record that we have seen the element
				elCount[(blocks[block][i]) - 1] += 1

	# determine if the element count is valid
	for num in elCount:
		# if a element appears more than 5 times accross the blocks the solution is invalid 
		if num > 5: 
			return False

	# check that any pair of elements is in two blocks
	for block in range(10):
		if blocks[block][1] != 0:
			pair1 = str(blocks[block][0]) + str(blocks[block][1])
			pairs[pair1] += 1
		if blocks[block][2] != 0:
			pair2 = str(blocks[block][1]) + str(blocks[block][2])
			pairs[pair2] += 1
			pair3 = str(blocks[block][0]) + str(blocks[block][2])
			pairs[pair3] += 1
		else:
			# do nothing its a pair with a zero in it
			pass

	# determine if the pair count is valid
	for num in pairs.values():
		# if a given pair appears more then two times the solution is invlaid
		if num > 2:
			return False

	# all validity tests passed
	return True

# appears to be working (somewhat tested)
def find_first_empty(blocks):
	for block in range(10):
		for i in range(3):
			if blocks[block][i] == 0:
				return block, i

# prints blocks accordingly
def print_it(blocks):
	for block in range(10):
		print(blocks[block])

# main logic 
def bibd(blocks):
	if is_complete(blocks):
		return blocks
	# blk is a block , i an index, this is the first block with a 0
	blk, i = find_first_empty(blocks)
	for num in range(max(blocks[blk])+1, nr_elements+1):
		blocks[blk][i] = num
		if is_valid(blocks):
			result = bibd(blocks)
			if is_complete(result):
				return result
		blocks[blk][i] = 0
	return blocks


# TESTING

# def(s) testing
# print(find_first_empty(blocks))
# print(is_complete(blocks))
# print_it(blocks)

# blocks[0][0] = 1
# blocks[0][1] = 2
# blocks[0][2] = 3


# blocks[3][0] = 2
# blocks[3][1] = 3

# blocks[4][0] = 2
# blocks[4][1] = 3

# print(is_valid(blocks))

# print_it(blocks)

# it seems to backtrack starting here
# [1, 2, 3]
# [1, 2, 3]
# [1, 3, 4]
# [1, 3, 4]
# [1, 4, 5]
# [2, 4, 5]
# [2, 4, 6]
# [2, 5, 6]
# [3, 5, 6]
# [6, 0, 0]

# run 20 trials and write to excel
start_time = time.perf_counter()
bibd(blocks)
print(time.perf_counter() - start_time)















              
