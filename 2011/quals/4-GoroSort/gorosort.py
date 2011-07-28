import sys
sys.path.append('../../')
import code_jam_common

def goro_sort(list):
	

#accept two lines of input for each test case
inputs = code_jam_common.accept_input(2)

for i, v in enumerate(inputs):
	if (i % 2 != 0):
		avg = goro_sort(v)
		print('Case #{0}: {1}'.format(i, avg))

