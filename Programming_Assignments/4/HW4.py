"""
HW4.py - Developing a algorithm to find the largest subsequence of a given list 
Date - 02/24/21 
Author - Daniel Throop
Class - COSC 3100

"""

listy = [10,-20,3,4,5,-1,-1,12,-3,1]

def subSum(lista):
	# base case (list is of length one)
	if len(lista):
		# would we not wanna return here?
		pass
	else:
		# divide the array in half (integer division)
		left, right = lista[:len(lista)//2], lista[len(lista)//2:]
		# recursivley return sums
		lbfl, lt, lbfr, ls = subSum(left)
		rbfl, rt, rbfr, rs = subSum(right)

		best_from_left = max(lbfl, ls+rbfl)
		best_from_right = max(rbfr, rs+lbfr)
		best_total = max(lt, rt, lbfr+rbfl)

		# calculate total of both sides
		suma = ls + rs

		return best_from_left, best_total, best_from_right, suma


print(subSum(listy)) 