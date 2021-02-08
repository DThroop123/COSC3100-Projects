"""
PA2_2.py - The second problem in programming assigment 2. Given a 64 bit number determine the number of ones in the binary representation of the number. 
Date - 02/06/21 
Author - Daniel Throop
Class - COSC 3100
"""

#table for lookup
table = {0: 0xf, 1: 0xe, 2: 0xd, 3: 0xc, 4: 0xb, 5: 0xa, 6: 9, 7: 8, 8: 7, 9: 6, 0xa: 5, 0xb: 4, 0xc: 3, 0xd: 2, 0xe: 1, 0xf: 0}
# translation = [0xf, 0xe, 0xd, 0xc, 0xb, 0xa, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def invert(n):
	final = 0
	stack = []

	# print(bin(n))

	while(n != 0):
		temp = n & 0xf
		stack.append(table[temp])
		n = n >> 4 

	for i in range(len(stack) - 1, -1, -1):
		final = final << 4
		final = final | stack[i]

	return final

# def flip(x):
# 	print(bin(x))
# 	result = 0
# 	for i in range(0,4):
# 		d = translation[(x >> 4 * i) & 0xf]
# 		result = result | (d << 4*i)
# 	return result


print(bin(invert(8)))