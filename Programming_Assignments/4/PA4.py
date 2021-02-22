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

# TESTED - working
def find_empty(board):
	for i in range(6):
		for j in range(6):
			if board[i][j] == 0:
				return i, j

# TESTED - working
def print_it(board):
	for i in range(6):
		print(board[i])

# TESTED - working
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




