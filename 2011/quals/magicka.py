﻿def find_opp(spell, b, oppose):
	for o in oppose:
		for e in spell:
			if (e == o[0] and b == o[1]) or (e == o[1] and b == o[0]):
				return True
	return False

def find_combo(a, b, combos):
	for c in combos:
		if (a == c[0] and b == c[1]) or (a == c[1] and b == c[0]):
			return c[2]
	return ''

def evoke(magic):
	base_letters = 'QWERASDF'
	combos = magic[0]
	combo_letters = ''

	oppose = magic[1]
	oppose_letters = ''
	for o in oppose:
		oppose_letters += o

	evoke = magic[2]
	spell = ''

	for element in evoke:
		if len(spell) == 0:
			spell += element
		else:
			#look for combo
			combo_result = ''
			if spell[-1] in base_letters:
				combo_result = find_combo(spell[-1], element, combos)
				if combo_result != '':
					spell[-1] = combo_result
			#check for opposition if combo was not created
			opp_result = False
			if combo_result == '':
				opp_result = find_opp(spell, element, oppose)
				if (opp_result):
					spell = ''
	return spell

def parse_input(input_string):
	tokens = input_string.split(' ')

	combo, oppose = [], []
	combo_count = int(tokens[0])
	oppose_count = int(tokens[combo_count + 1])

	if combo_count != 0:
		combo = tokens[1:combo_count + 1]
	if oppose_count != 0:
		oppose = tokens[combo_count + 2:combo_count + oppose_count + 2]
	evoke = tokens[-1]
	
	return [combo, oppose, evoke]

##
 # Accepts program input as a number of commands to follow, follewed by strings of input
def accept_input():
	str = input()

	try:
		num_inputs = int(str)
	except ValueError:
		exit('First input must be the number of items to follow.')

	inputs = []
	while (num_inputs):
		num_inputs -= 1
		inputs.append(input().strip())

	return inputs

###
inputs = accept_input()
case_number = 1
for input_string in inputs:
	magic = parse_input(input_string)
	spell = evoke(magic)
	print('Case #%d:' % case_number, spell)
	case_number += 1