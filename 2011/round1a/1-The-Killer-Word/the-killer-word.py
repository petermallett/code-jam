
##
 # Accepts program input as a number of commands to follow, follewed by strings of input
def accept_input():
	input_str = input()

	try:
		num_inputs = int(input_str)
	except ValueError:
		exit('First input must be the number of items to follow.')

	cases = []
	while (num_inputs):
		num_inputs -= 1
		word_count, order_str_count = [int(x) for x in input().split(' ')]
		words = []
		order_strings = []
		while (word_count):
			word_count -= 1
			words.append(input().strip())
		while (order_str_count):
			order_str_count -= 1
			order_strings.append(input().strip())

		cases.append([words, order_strings])

	return cases

###
inputs = accept_input()

case_number = 0
for case in inputs:
	case_number += 1
	print('Case #{}: '.format(case_number), case)

