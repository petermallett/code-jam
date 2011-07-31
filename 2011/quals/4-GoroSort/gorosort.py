import sys
sys.path.append('../../')
import codejam

def goro_sort(list):
	count_unsorted = 0
	for i, v in enumerate(list):
		if (i + 1 == int(v)):
			count_unsorted += 1
	return (len(list) - count_unsorted)
		

#accept two lines of input for each test case
inputs = codejam.accept_input(2)

case_number = 0
for i, v in enumerate(inputs):
	if (i % 2 != 0):
		case_number += 1
		input_list = v.split(' ') 
		avg = goro_sort(input_list)
		print('Case #{0}: {1:f}'.format(case_number, avg))

