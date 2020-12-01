instruction_size = {
	99: 1,
	1: 4,
	2: 4,
	3: 2,
	4: 2,
	5: 3,
	6: 3,
	7: 4,
	8: 4
}

def execute(state, ID):
	i = 0
	outputs = []
	while i < len(state):
		data = str(state[i])
		op = int(data[-2:])
		p = [0,0,0]
		for j in range(len(data[:-2])):
			p[j] = int(data[:-2][len(data[:-2])-1-j])
		#print(op, data, i, p)
		try:
			r1 = state[i+1] if p[0] == 0 else i+1
			r2 = state[i+2] if p[1] == 0 else i+2
			r3 = state[i+3] if p[2] == 0 else i+3
		except IndexError:
			break

		#print(type(state[r3]), type(state[r1]), type(state[r2]))
		if op == 99:# or r1>l or r2>l or r3>l:
			break
		elif op == 1:
			state[r3] = state[r1] + state[r2]
		elif op == 2:
			state[r3] = state[r1] * state[r2]
		elif op == 3:
			state[r1] = ID
		elif op == 4:
			outputs.append(state[r1])
			print(state[r1])
		elif op == 5:
			if state[r1] != 0:
				i = state[r2]
				continue
		elif op == 6:
			if state[r1] == 0:
				i = state[r2]
				continue
		elif op == 7:
			state[r3] = state[r1] < state[r2]
		elif op == 8:
			state[r3] = state[r1] == state[r2]

		i += instruction_size[op]
	return outputs[-1]

with open("05.txt", "r") as f:
	old_state = list(map(int, f.readline().strip().split(",")))

part_1 = execute([x for x in old_state], 1)
part_2 = execute([x for x in old_state], 5)

print("Part 1:", part_1)
print("Part 2:", part_2)