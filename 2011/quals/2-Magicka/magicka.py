import sys
sys.path.append('../../')
import codejam

def find_opp(spell, b, oppose):
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
		if len(spell) != 0:
			#look for combo
			combo_result = ''
			if spell[-1] in base_letters:
				combo_result = find_combo(spell[-1], element, combos)
				if combo_result != '':
					spell = spell[0:-1] + combo_result
					continue
			#check for opposition if combo was not created
			opp_result = False
			if combo_result == '':
				opp_result = find_opp(spell, element, oppose)
				if (opp_result):
					spell = ''
					continue
		spell += element
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

###
inputs = codejam.accept_input()

case_number = 1
for input_string in inputs:
	magic = parse_input(input_string)
	spell = evoke(magic)
	output = 'Case #%d: [' % case_number
	for i, element in enumerate(spell):
		output += element
		if i + 1 < len(spell):
			output += ', '
	output += ']'
	print(output)
	case_number += 1
