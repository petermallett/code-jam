import sys
sys.path.append('../../')
import codejam

###
# Splits input string into:
# n - max number of games played today
# d - percentage of games won this day
# g - percentage of games jon all time
# Then calculates the possibility of these percentages.
def test_stats(input_string):
	possible = False
	n, d, g = [int(x) for x in input_string.split(' ')]
	if (g == 100 and d != 100) or (g == 0 and d != 0):
		possible = False
	elif (g == d == 0) or (g == d == 100):
		possible = True
	else:
		for t in range(1, n + 1):
			if (t * d) % 100 == 0:
				possible = True	
	return possible

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

