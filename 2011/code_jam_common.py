##
 # Accepts program input as a number of commands to follow, follewed by strings of input
def accept_input(lines_per = 1):
	str = input()

	try:
		num_inputs = int(str)
	except ValueError:
		exit('First input must be the number of items to follow.')

	num_inputs *= lines_per
	inputs = []
	while (num_inputs):
		num_inputs -= 1
		inputs.append(input().strip())

	return inputs

