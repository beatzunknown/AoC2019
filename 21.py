from intcode_13 import IntCode

with open("21.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

walk_script = ['NOT B J',
			   'NOT C T',
			   'OR T J', #(if theres no ground 2 or 3 steps away
			   'AND D J', # and theres ground 4 steps away)
			   'NOT A T',
			   'OR T J', # or (if there's no ground 1 step away) the jump
			   'WALK']

run_script = ['NOT B J',
			   'NOT C T',
			   'OR T J', #((if theres no ground 2 or 3 steps away)
			   'AND D J', # and theres ground 4 steps away
			   'AND H J', # and theres ground 8 steps away)
			   'NOT A T',
			   'OR T J', # or (if there's no ground 1 step away)
			   'RUN'] # then jump

inputs = []
input_i = 0

def convert_script(script):
	data = []
	script = [list(map(ord, s)) for s in script]
	for line in script:
		data += line + [ord('\n')]
	return data

def input_func():
	global input_i
	input_i += 1
	return inputs[input_i-1]

def calc_damage(script):
	global inputs, input_i
	inputs, input_i = convert_script(script), 0
	output = []
	text = []
	computer = IntCode(state, [])
	while not computer.is_completed():
		try:
			out = computer.execute(input_func)
			if out == 10:
				text.append(output)
				output = []
			else:
				output += [out]
		except IndexError:
			break

	print(*[''.join(list(map(chr, line))) for line in text], sep='\n')

	return output.pop()

part_1 = calc_damage(walk_script)
part_2 = calc_damage(run_script)

print("Part 1:", part_1)
print("Part 2:", part_2)