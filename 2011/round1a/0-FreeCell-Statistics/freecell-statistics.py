import sys
sys.path.append('../../')
import codejam

###
# Splits input string into:
# n - max number of games played today
# d - percentage of games won this day
# g - percentage of games won all time
# Then calculates the possibility of these percentages
def test_stats(input_string):
	n, d, g = input_string.split(' ')
	pass

###
inputs = codejam.accept_input()

case_number = 0
for input_string in inputs:
	case_number += 1
	test = test_stats(input_string)
	if (test):
		print('Case #{}: Possible'.format(case_number))
	else:
		print('Case #{}: Broken'.format(case_number))

