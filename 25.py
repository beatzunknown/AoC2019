from collections import deque
from intcode import IntCode

'''
some orderings (heaviest to lightest)
astronaut ice cream (must have)
jam, shell (can't have)
klein bottle, space heater
asterisk, spool of cat6, space law space brochure

answer was 2105377 attained by (ice cream, bottle, heater, asterisk)
'''

with open("25.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

inputs = deque()

def input_func():
	global inputs
	
	if len(inputs) == 0:
		data = input()
		for c in data:
			inputs.append(ord(c))
		inputs.append(10)
	return inputs.popleft()

def travel_ship():
	output = []
	computer = IntCode(state, [])
	while not computer.is_completed():
		try:
			out = computer.execute(input_func)
			if out == 10:
				print(''.join(list(map(chr, output))))
				output = []
			else:
				output += [out]
		except IndexError:
			break

travel_ship()