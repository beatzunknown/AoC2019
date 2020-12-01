# process input

def execute(state):
	i = 0
	while i < len(state):
		op = state[i]
		r1 = state[i+1]
		r2 = state[i+2]
		s1 = state[i+3] 
		if op == 99:# or r1>l or r2>l or s1>l:
			break
		elif op == 1:
			state[s1] = state[r1] + state[r2]
		elif op == 2:
			state[s1] = state[r1] * state[r2]
		i += 4
	return state[0]

with open("02.txt", "r") as f:
	old_state = list(map(int, f.readline().strip().split(",")))

state = [x for x in old_state]
state[1] = 12
state[2] = 2

part_1 = execute(state)

part_2 = 0
for n in range(100):
	for v in range(100):
		state = [x for x in old_state]
		state[1] = n
		state[2] = v

		output = execute(state)
		if output == 19690720:
			part_2 = 100*n + v
			break

print("Part 1:", part_1)
print("Part 2:", part_2)