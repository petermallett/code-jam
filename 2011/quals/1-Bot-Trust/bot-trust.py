import sys
sys.path.append('../../')
import code_jam_common

class Bot:
	"""A robot class which can press buttons, stand at buttons and move to other buttons"""

	def __init__(self, name):
		self.name = name
		self.commands = []
		self.position = 1		

	#load the instructions for this robot, along with the sequence number
	def hear_instructions(self, instructions):
		for i, command in enumerate(instructions):
			if command[1] == self.name:
				self.commands.append((i, command[0]))

	#return the distance to the next button
	def shout_distance(self):
		if len(self.commands) != 0:
			return abs(self.position - self.commands[0][1])
		else:
			return 0

	#If not at the next button, move towards the next button
	def move(self, distance):
		if len(self.commands) != 0:
			if self.position != self.commands[0][1]:
				if self.position < self.commands[0][1]:
					self.position += distance
				else:
					self.position -= distance

	#If this bot is next to press, move to its button.
	def move_if_next(self, sequence):
		if len(self.commands) != 0:
			if (sequence == self.commands[0][0]):
				distance = abs(self.position - self.commands[0][1])
				self.position = self.commands[0][1]
				return distance
		
		return 0
	
	#If the bot is at its next button and it is the next in the program sequnce, press it and return True
	#otherwise, return False
	def act(self, sequence):
		if len(self.commands) != 0:
			if self.position == self.commands[0][1] and sequence == self.commands[0][0]:
				del self.commands[0]
				return True
		
		return False


class TestChamber:
	"""A class which instructs and observes the robots running a test"""

	# a list of program instructions consisting of (button_number, bot_name)
	program = []

	def __init__(self, test_number):
		self.test_number = test_number
		self.time_elapsed = 0
		self.sequence = 0

	# Tests the validity of the input string and stores the instructions.
	def load_instructions(self, input_string):
		sequence = input_string.split(' ')
		program = []
		state = 0
		for instruction in sequence:
			if state == 0:
				try:
					instruction_count = int(instruction)
				except (TypeError, ValueError):
					exit('Expected a number, instruction was "%s".' % instruction)
				state = 1
			elif state == 1:
				bot_name = instruction
				if not (bot_name == 'O' or bot_name == 'B'):
					exit('Robot instructions must be for "O" or "B", instruction was "%s".' % bot_name)
				state = 2
			else:
				try:
					button_number = int(instruction)
				except (TypeError, ValueError):
					exit('Expected a button number, instruction was "%s".' % instruction)
				if not 0 < button_number <= 100:
					exit('Buttons can only number between 1 and 100, instruction was "%s".' % instruction)
				state = 1
				program.append((button_number, bot_name))

		if state == 2:
			exit('Odd number of instructions. Each robot code must be followed by a button number.')

		self.program = program
		self.test_length = len(program)

		if instruction_count != self.test_length:
			exit('Improper number of instructions input. Expected %d.' % instruction_count)

	def run(self):
		#enter the test chamber
		self.assemble_bots()

		#monologue at the bots
		self.instruct_bots()
		
		Orange = self.bots[0]
		Blue = self.bots[1]

		#time the bots' run
		while self.sequence < self.test_length:
			d0 = Orange.shout_distance()
			d1 = Blue.shout_distance()
			#print('seq:',self.sequence)
			#print(' elap:',self.time_elapsed, 'o pos:',Orange.position, 'o dis:',d0, 'blue pos',Blue.position, 'blue dis:',d1)
			if (d0 != 0 and d1 != 0):
				#neither bot is at their next button, move
				if (d0 < d1):
					Orange.move(d0)
					Blue.move(d0)
					self.time_elapsed += d0
				else:
					Orange.move(d1)
					Blue.move(d1)
					self.time_elapsed += d1
			else:
				#one bot is already at its button, ask the other to move
				if (d0 == 0):
					self.time_elapsed += Blue.move_if_next(self.sequence)
				else:
					self.time_elapsed += Orange.move_if_next(self.sequence)

			#at least one bot is at their button, don't move
			#ask him to press it
			pressed = Orange.act(self.sequence)
			if (pressed):
				self.sequence += 1
				Blue.move(1)
				self.time_elapsed += 1

			pressed = Blue.act(self.sequence)
			if (pressed):
				self.sequence += 1
				Orange.move(1)
				self.time_elapsed += 1

	def assemble_bots(self):
		Orange, Blue = Bot('O'), Bot('B')
		self.bots = [Orange, Blue]

	def instruct_bots(self):
		for bot in self.bots:
			bot.hear_instructions(self.program)

	def print_result(self):
		print('Case #%d:' % self.test_number, self.time_elapsed)

###
inputs = code_jam_common.accept_input()
test_cases = []
test_number = 1
for input_string in inputs:
	test_chamber = TestChamber(test_number)
	test_chamber.load_instructions(input_string)
	test_cases.append(test_chamber)
	test_number += 1


for test in test_cases:
	test.run()
	test.print_result()
