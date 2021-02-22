"""
PA5.py - implementing a backtracking algorithm to solve a variant of sodoku
Date - -02/19/21 
Author - Daniel Throop
Class - COSC 3100

"""

di = 6
dj = 6
countList = [0,0,0,0,0]
cellOffsets = {0: (-1, -1), 1: (-1, 0), 2: (-1, 1), 3: (0, 1), 4: (1, 1), 5: (1, 0), 6: (1, -1), 7: (0, -1)}

# configuraiton of each section on the board
configuration = [[(0,0), (1,0), (0,1), (2,0)],
                 [(2,1), (3,1), (3,0), (4,0), (5,0)],
                 [(0,2), (1,1), (1,2), (1,3), (2,2)],
                 [(4,1), (4,2)],
                 [(5,1), (5,2), (5,3), (4,4), (5,4)],
                 [(3,2), (2,3), (3,3), (4,3), (3,4)],
                 [(0,3), (0,4), (0,5), (1,4), (2,4)],
                 [(1,5), (2,5), (3,5), (4,5), (5,5)]
                 ]


# initialzing matrix to be manipulated
matrix = [[0 for j in range(dj)] for i in range(di)]
matrix[0][0]=4
matrix[0][4]=5
matrix[2][2]=4
matrix[3][3]=2
matrix[3][4]=3
matrix[4][4]=5
matrix[5][2]=1	

# fills board with 1's for testing purposes
# for i in range(6):
# 	for j in range(6):
# 		matrix[i][j] = 1

# testing if find empty works
# matrix[5][5] = 0

# testing valid so far
# matrix[1][1] = 4 
# matrix[1][2] = 4
# matrix[1][3] = 4 
# matrix[2][3] = 4
# matrix[1][0] = 4
# matrix[3][1] = 4
# matrix[2][1] = 4
# matrix[0][2] = 5
# matrix[2][4] = 5
# matrix[3][2] = 3	

# TESTED
# resets all elements of a list to zero 
def resetList(listy):
	for i in range(len(listy)):
		listy[i] = 0
	return listy


# NOT TESTED ((a) and (b) should be working)
def valid_so_far(board):
	global countList

	# TESTED (should be working)
	# # checks
	# # (a) no two same non-zero integers are next to each other, even diagonally 
	for row in range(6):
		for col in range(6):
			# don't do anything
			if board[row][col] == 0:
				pass
			else:
				# check surrounding 8 cells
				for cell in range(8):
					# add offsets for current cell to check
					chckRow = row + cellOffsets[cell][0]
					chckCol = col + cellOffsets[cell][1]
					if valid_pos(chckRow, chckCol):
						# compare with current position
						if board[row][col] == board[chckRow][chckCol]:
							return False

	# TESTED (should be working)
	# # (b) each area contains only numbers larger than 0 once and not larger than 
	# # the number of cells in the area.

	for block in configuration:
		for tup in block:
			# access current cell
			currCell = board[tup[1]][tup[0]]
			# if it doesnt equal zero we want to investigate it
			if currCell != 0:
				# determine if it is within the legal range of numbers 
				if currCell <= len(block):
					# record we saw this number
					countList[currCell - 1] += 1
				else:
					countList = resetList(countList)
					return False
		for count in countList:
			if count > 1:
				countList = resetList(countList)
				return False
		countList = resetList(countList)

	return True

# TESTED - working
# returns wehther a given check cell is valid to be checked
def valid_pos(row, col):
	if row < 0 or row > 5 or col < 0 or col > 5:
		return False
	else:
		return True

# TESTED - working
def done(board):
	for i in range(6):
		for j in range (6):
			if board[i][j] == 0:
				return False
	return True

# TESTED - working (be careful on the call that their are no empty spots - shouldn't happen, but be wary)
def find_empty(board):
	for i in range(6):
		for j in range(6):
			if board[i][j] == 0:
				return i, j

# TESTED - working
def print_it(board):
	for i in range(6):
		print(board[i])

# NOT TESTED 
def puzzSolver(board):
	if done(board):
		return board
	row, col = find_empty(board)
	for num in range(1, 6):
		board[row][col] = num
		if valid_so_far(board):
			result = puzzSolver(board)
			if done(result):
				return result
		board[row][col] = 0
	return board


# TESTING
print_it(puzzSolver(matrix))


# previous assignment code

# import time

# # BIBD conditions
# nr_blocks = 10
# pts_per_block = 3
# nr_elements = 6
# distinct = 2
# blks_with_point = 5

# blocks = [pts_per_block*[0] for _ in range(nr_blocks)]

# # should work (not tested)
# def is_complete(blocks):
#     for block in range(10):
#         for i in range(3):
#             if blocks[block][i] == 0:
#                 return False
#     return True

# # both conditions tested and working
# def is_valid(blocks):
# 	# count data structures
# 	elCount = [0]*nr_elements
# 	pairs = {"12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "23": 0, "24": 0, "25": 0, "26": 0, "34": 0, "35": 0, "36": 0, "45": 0, "46": 0, "56": 0}

# 	# check that an element appears exactly 5 times in different blocks
# 	for block in range(10):
# 		for i in range(3):
# 			# if the given position isn't a zero we want to investigate it
# 			if blocks[block][i] != 0:
# 				# record that we have seen the element
# 				elCount[(blocks[block][i]) - 1] += 1

# 	# determine if the element count is valid
# 	for num in elCount:
# 		# if a element appears more than 5 times accross the blocks the solution is invalid 
# 		if num > 5: 
# 			return False

# 	# check that any pair of elements is in two blocks
# 	for block in range(10):
# 		if blocks[block][1] != 0:
# 			pair1 = str(blocks[block][0]) + str(blocks[block][1])
# 			pairs[pair1] += 1
# 		if blocks[block][2] != 0:
# 			pair2 = str(blocks[block][1]) + str(blocks[block][2])
# 			pairs[pair2] += 1
# 			pair3 = str(blocks[block][0]) + str(blocks[block][2])
# 			pairs[pair3] += 1
# 		else:
# 			# do nothing its a pair with a zero in it
# 			pass

# 	# determine if the pair count is valid
# 	for num in pairs.values():
# 		# if a given pair appears more then two times the solution is invlaid
# 		if num > 2:
# 			return False

# 	# all validity tests passed
# 	return True

# # appears to be working (somewhat tested)
# def find_first_empty(blocks):
# 	for block in range(10):
# 		for i in range(3):
# 			if blocks[block][i] == 0:
# 				return block, i

# # prints blocks accordingly
# def print_it(blocks):
# 	for block in range(10):
# 		print(blocks[block])

# # main logic 
# def bibd(blocks):
# 	if is_complete(blocks):
# 		return blocks
# 	# blk is a block , i an index, this is the first block with a 0
# 	blk, i = find_first_empty(blocks)
# 	for num in range(max(blocks[blk])+1, nr_elements+1):
# 		blocks[blk][i] = num
# 		if is_valid(blocks):
# 			result = bibd(blocks)
# 			if is_complete(result):
# 				return result
# 		blocks[blk][i] = 0
# 	return blocks


# # TESTING

# # def(s) testing
# # print(find_first_empty(blocks))
# # print(is_complete(blocks))
# # print_it(blocks)
# # print(is_valid(blocks))
# # print_it(blocks)
# # [6, 0, 0]

# # trial runner
# start_time = time.perf_counter()
# print_it(bibd(blocks))
# time.perf_counter() - start_time


