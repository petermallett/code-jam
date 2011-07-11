class Bot:
	"""A robot class which can press buttons, stand at buttons and move to other buttons"""

	def __init__(self, name):
		self.name = name

	def assemble(self):
		self.commands = []
		self.state = 'standing'
		self.position = 1

	#load the instructions for this robot, along with the sequence number
	def hear_instructions(self, instructions):
		for i, command in enumerate(instructions):
			if command[1] == self.name:
				self.commands.append((i, command[0]))

	def move(self, direction):
		new_position = self.position + direction
		if 0 < new_position <= 100:
			self.position = new_position
			return 1
		else:
			return 0

class TestChamber:
	"""A class which instructs and observes the robots running a test"""

	# a list of program instructions consisting of (button_number, bot_name)
	program = []

	def __init__(self):
		self.completed = False
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
					button_number = int(instruction)
				except (TypeError, ValueError):
					exit('Expected a button number, instruction was "%s".' % instruction)
				if not 0 < button_number <= 100:
					exit('Buttons can only number between 1 and 100, instruction was "%s".' % instruction)
				state = 1
			else:
				bot_name = instruction
				if not (bot_name == 'O' or bot_name == 'B'):
					exit('Robot instructions must be for "O" or "B", instruction was "%s".' % bot_name)
				state = 0
				program.append((button_number, bot_name))
		if state == 1:
			exit('Odd number of instructions. Each button number must be followed by a robot code.')

		self.program = program
		self.test_length = len(program)

	def assemble_bots(self):
		Orange.assemble()
		Blue.assemble()
		return [Orange, Blue]

	def instruct_bots(self, bot_list):
		for bot in bot_list:
			bot.hear_instructions(self.program)

	def button_pressed():
		self.sequence += 1
		if self.sequence == self.test_length:
			self.completed = True

##
 # Accepts program input as a number of commands to follow, folled by strings of instructions
 # for the robots in the format:
 # {button number} {robot color}
def accept_input():
	str = input('--> ')

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
test_cases = []
for input_string in inputs:
	test_chamber = TestChamber()
	test_chamber.load_instructions(input_string)
	test_cases.append(test_chamber)

Orange, Blue = Bot('O'), Bot('B')

for test in test_cases:
	#enter the test chamber
	bots = test.assemble_bots()

	#monologue at the bots
	test.instruct_bots(bots)

	# for bot in bots:
		# print(bot.name, bot.commands)
