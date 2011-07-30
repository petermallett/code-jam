import sys
sys.path.append('../../')
import codejam

def goro_sort(list):
	

#accept two lines of input for each test case
inputs = codejam.accept_input(2)

for i, v in enumerate(inputs):
	if (i % 2 != 0):
		avg = goro_sort(v)
		print('Case #{0}: {1}'.format(i, avg))

