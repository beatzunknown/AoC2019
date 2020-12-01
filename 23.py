from collections import deque
from intcode import IntCode

with open("23.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))
	network_size = 50

computers = [IntCode(state, []) for i in range(network_size)]
i_queue = [deque([i]) for i in range(network_size)]
o_queue = [deque() for i in range(network_size)]

curr_comp = 0

def input_func():
	if len(i_queue[curr_comp]) > 0:
		return i_queue[curr_comp].popleft()
	else:
		computers[curr_comp].halt()
		idle[curr_comp] = True
		return -1

found = False
part_1 = part_2 = nat = nat_trans = None

while not part_1 or not part_2:
	idle = [False for i in range(network_size)]
	for i in range(50):
		curr_comp = i
		try:
			o_queue[i].append(computers[i].execute(input_func))
		except IndexError:
			continue
		if len(o_queue[i]) >= 3:
			addr = o_queue[i].popleft()
			x = o_queue[i].popleft()
			y = o_queue[i].popleft()
			if addr == 255:
				if not part_1:
					part_1 = y
				nat = (x,y)
			else:
				i_queue[addr].append(x)
				i_queue[addr].append(y)
	if all(idle) and nat != None:
		i_queue[0].append(nat[0])
		i_queue[0].append(nat[1])
		if nat == nat_trans:
			part_2 = nat[1]
		else:
			nat_trans = nat

print("Part 1:", part_1)
print("Part 2:", part_2)