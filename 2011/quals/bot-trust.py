def parse_input(inputs):
	for input_string in inputs:
		sequence = input_string.split(' ')
		
		state = 0
		for instruction in sequence:
			if state == 0:
				try:
					button_number = int(instruction)
				except (TypeError, ValueError):
					exit('Expected a button number, instruction was "%s".' % instruction)
				if not 0 < button_number <= 100:
					exit('Buttons can only number between 1 and 100, instruction was "%s".' % instruction)
				state = 1
			else:
				if not (instruction == 'O' or instruction == 'B'):
					exit('Robot instructions must be for "O" or "B", instruction was "%s".' % instruction)
				state = 0
		if state == 1:
			exit('Odd number of instructions. Each button number must be followed by a robot code.')

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