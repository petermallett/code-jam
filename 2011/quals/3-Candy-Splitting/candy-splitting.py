import sys
sys.path.append('../../')
import codejam

def split_candy(input_string):
	weights = [int(n) for n in input_string.split(' ')]
	patrick_sum = weights[0]
	for n in weights[1:]:
		patrick_sum = patrick_sum ^ n
	if patrick_sum == 0:
		weights.sort()
		sean_sum = 0
		for n in weights[1:]:
			sean_sum += n
		return sean_sum	
	else:
		return False

###
inputs = codejam.accept_input(2)
case_number = 1
for i, input_string in enumerate(inputs):
	# each odd input line is the list of weight values
	if i % 2 == 1:
		result = split_candy(input_string)
		if result == False:
			result = 'NO'
		print('Case #{0}: {1}'.format(case_number, result))
		case_number += 1

