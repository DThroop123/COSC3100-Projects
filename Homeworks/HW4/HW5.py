"""
HW5.py - Developing a algorithm to find the largest subsequence of a given list 
Date - 02/24/21 
Author - Daniel Throop
Class - COSC 3100

"""

# test lists
listyOne = [10, -20, 3, 4, 5, -1, -1, 12, -3, 1]
listyTwo = [ 2, 2, 7, 5, 2, 2, 0, 6, 4]
listyThree = [8, 6, 1, 3, -2, -2, -1, -7, 6]
listyFour = [3, -2, -6, -7, 1, -3, -6, 7, 6, -8, -6, -2, 8, -4, 2, 2, 6, -1, 2, 4]
listyFive = [-3, -4, 8, 6, 5, -3]
listySix = [-5, -2, 5, -5, -3, -5, -7, -6, -6, 7, -4, 2, 7, -1, -1, -2, 7, 5, -3, 2, -6, 5, 8, -6, 5, 6, 0, 1, 8, 7, 7, -3, 0, 8, -7, 0, -8, -2, -8, -4, -2, 8, -3, -2, 7, -4, -1, 0, 4, 1]


def subSum(lista):
	# base case (list is of length one)
	if len(lista) == 1:
		return lista[0], lista[0], lista[0], lista[0]
	else:
		# divide the array in half (integer division)
		left, right = lista[:len(lista)//2], lista[len(lista)//2:]
		
		# recursivley return sums
		lbfl, lt, lbfr, ls = subSum(left)
		rbfl, rt, rbfr, rs = subSum(right)

		# picking our three best sequecnes
		best_from_left = max(lbfl, ls+rbfl)
		best_from_right = max(rbfr, rs+lbfr)
		best_total = max(lt, rt, lbfr+rbfl)

		# calculate total of both sides
		suma = ls + rs

		return best_from_left, best_total, best_from_right, suma


print(max(subSum(listyOne))) 
print(max(subSum(listyTwo)))
print(max(subSum(listyThree))) 
print(max(subSum(listyFour))) 
print(max(subSum(listyFive))) 
print(max(subSum(listySix))) 