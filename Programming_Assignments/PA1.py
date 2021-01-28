"""
PA1.py - analyzing the runtimes of the python fibonnaci implementation for both recursive and non-recursive solutions
Date - 11/18/20 
Author - Daniel Throop
Class - COSC 3100

"""




import time
import math
import xlsxwriter


# intialize workbooks
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

# writing headers
outSheet.write(0, 0, "rec_fib(n)")

for i in range(1, 25):
	outSheet.write(0, i, i)
	outSheet.write(i, 0, i)

# intializes dictionary to gather durations of fib() runs
def initDict(n):
	dummy = {}
	for i in range(1, n):
		dummy[i] = []
	return dummy

durations = initDict(25)
averages = initDict(25)
# print(durations)
# print(averages)


# recursive  
def rec_fibonnaci(i):
	if i < 2:
		return i
	else:
		return rec_fibonnaci(i-1)+rec_fibonnaci(i-2)

# non-recursive 
# def good_fibonnaci(i):
# 	pre = 0
# 	curr = 1
# 	if i == 0:
# 		return pre
# 	elif i ==1:
# 		return curr
# 	else:
# 		return
		


for trial in range(1, 2):

	# recording time durations (nsecs)
	for i in range(1, 25):
		total = 0
		print(i)
		for j  in range(20):
			start_time = time.perf_counter_ns()
			for _ in range(50):
				x = rec_fibonnaci(i)
			duration = (time.perf_counter_ns() - start_time)/50
			print("{:12.10f}".format(duration))
			durations[i].append(duration)

		# storing the average of the 20 runs from fib(n)

		# sum the 20 runs of fib(n)
		for j in range(len(durations[1])):
			total = total + durations[i][j]
		# take the average of the total
		total = total/20.0
		# store away average to be put in excel
		averages[i] = round(total, 4 - (int(math.floor(math.log10(abs(total)))) - 1))
		print("\n")

	print(averages)

	# write averages to excel sheet
	for row in range(1, len(averages) + 1):
		outSheet.write(row, trial, str(averages[row]))

	durations.clear()
	averages.clear()

	durations = initDict(25)
	averages = initDict(25)


outWorkbook.close()










# storing averages of time durations for precision

# for i in range(1, len(durations) + 1):
# 	total = 0
# 	# sum the 20 runs of fib(n)
# 	for j in range(len(durations[1])):
# 		total = total + durations[i][j]
# 	# take the average of the total
# 	total = total/20.0
# 	# store away average to be put in excel
# 	averages[i] = round(total, 4 - (int(math.floor(math.log10(abs(total)))) - 1))




# modified version easier to paste to numbers

# for i in range(1, 25):
# 	start_time = time.perf_counter_ns()
# 	for _ in range(50):
# 		x = rec_fibonnaci(i)
# 	duration = (time.perf_counter_ns() - start_time)/50
# 	print("{:12.10f}".format(duration))
