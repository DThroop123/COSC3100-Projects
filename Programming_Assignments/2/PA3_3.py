"""
PA2_3.py - The third problem in programming assigment 2. Given a 9x9 array or Sudoku board, determine if the given board is a vlaid solution.
Date - 02/06/21 
Author - Daniel Throop
Class - COSC 3100
"""

table = [0,0,0,0,0,0,0,0,0]

# function that checks the validity of a sudoku solution
def checkSol(board):
	global table

	# check columns
	for i in range(0, 9):
		for j in range(0, 9):
			currNum = board[j][i]
			# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] & 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
		# reset the table to all zeros 
		table = reset(table)

	# check rows
	for i in range(0, 9):
		for j in range(0, 9):
			currNum = board[i][j]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] & 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
		# reset the table to all zeros 
		table = reset(table)

	# check house 1 (3x3 subgrid)

	for i in range(3):
		for j in range(3):
			currNum = board[i][j]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

	# check house 2 (3x3 subgrid)

	for i in range(3,6,1):
		for j in range(3):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

	# check house 3 (3x3 subgrid)

	for i in range(6,9,1):
		for j in range(3):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

	# check house 4 (3x3 subgrid)

	for i in range(3):
		for j in range(3,6,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)


	# check house 5 (3x3 subgrid)

	for i in range(3,6,1):
		for j in range(3,6,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

	# check house 6 (3x3 subgrid)

	for i in range(6,9,1):
		for j in range(3,6,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)


	# check house 7 (3x3 subgrid)

	for i in range(3):
		for j in range(6,9,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)


	# check house 8 (3x3 subgrid)

	for i in range(3,6,1):
		for j in range(6,9,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

		# check house 8 (3x3 subgrid)

	for i in range(6,9,1):
		for j in range(6,9,1):
			currNum = board[j][i]
				# check if currNum has already been seen
			if(currNum == 0):
				pass
			else:
				if(table[currNum - 1] == 1):
					return False
				else:
					# show that we have seen the number 
					table[currNum - 1] = 1 
			
	# reset table to all zeros					
	table = reset(table)

	#partial solution is valid
	return True

# function that resets the lookup table
def reset(table):
	clean = [0,0,0,0,0,0,0,0,0]

	for i in range(0, len(table)):
		clean[i] = 0 & table[i]

	return clean


testBoard = [[0,5,0,0,0,8,0,4,0], 
			 [0,4,0,3,0,0,0,7,0], 
			 [0,3,1,7,2,0,8,9,0],
			 [3,0,0,0,0,0,7,8,0], 
             [0,0,5,0,0,0,1,0,0], 
             [0,6,2,0,0,0,0,0,3], 
             [0,2,6,0,4,7,9,3,0], 
             [0,8,0,0,0,6,0,2,0], 
             [0,9,0,8,0,0,0,1,0]]

print(checkSol(testBoard))

