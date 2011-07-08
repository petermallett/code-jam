def parse_input(inputs):
	for input_string in inputs:
		sequence = input_string.split(' ')

		print(sequence)


str = input('--> ')

try:
	num_inputs = int(str)
except ValueError:
	exit('First input must be the number of items to follow.')

inputs = []
while (num_inputs):
	num_inputs -= 1
	inputs.append(input().strip())

results = parse_input(inputs)