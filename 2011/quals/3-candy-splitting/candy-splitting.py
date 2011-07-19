#sum = 3 ^ 5 ^ 6
#print(sum)
#exit()

##
 # Accepts program input as a number of commands to follow, follewed by strings of input
def accept_input():
	str = input()

	try:
		num_inputs = int(str)
	except ValueError:
		exit('First input must be the number of items to follow.')

	#each test case is comprised of two lines of input
	num_inputs *= 2
	inputs = []
	while (num_inputs):
		num_inputs -= 1
		inputs.append(input().strip())

	return inputs

###
inputs = accept_input()
case_number = 1
for i, input_string in enumerate(inputs):
	# each odd input line is the list of weight values
	if i % 2 == 1:
		print(input_string)
