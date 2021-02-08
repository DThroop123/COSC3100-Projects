"""
PA2_1.py - The first problem in programming assigment 2. Given a 64 bit number determine the number of ones in the binary representation of the number. 
Date - 02/06/21 
Author - Daniel Throop
Class - COSC 3100
"""
# returns the number of one bits in a decimal number n
# def countOnes(n):
# 	total = 0
# 	binary = bin(n)
# 	binary = binary[2:len(binary)]

# 	for i in range(0, len(binary)):
# 		if(int(binary[i]) ==  1):
# 			total += 1

# 	return total


# table for lookup
table = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1, 9: 2, 0xa: 2, 0xb: 3, 0xc: 2, 0xd: 3, 0xe: 3, 0xf: 4}

# function that uses bitwise operations to determine number of 1 bits in number
def countOnes(n):
	total = 0

	while(n != 0):
		#mask first four bits
		temp = n & 0xf
		#lookup num of ones and add to total
		total += table[temp]
		#shift binary right by 4 bits
		n = n >> 4 

	return total



