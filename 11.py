from collections import deque
from intcode import IntCode

with open("11.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

inputs = deque()

def input_func():
	global inputs
	return inputs.popleft()

dirs = {
	(0, 1): [(-1, 0), (1, 0)],
	(-1, 0): [(0, -1), (0, 1)],
	(0, -1): [(1, 0), (-1, 0)],
	(1, 0): [(0, 1), (0, -1)]
}

for i in range(2):
	direction = (0,1)
	x = y = 0
	painted = {}
	painted[(x,y)] = i
	computer = IntCode(state, [])
	inputs = deque()
	while not computer.is_completed():
		panel_col = not ((x, y) not in painted or painted[(x, y)] == 0)
		inputs.append(panel_col)
		try:
			colour = computer.execute(input_func)
			dir_val = computer.execute(input_func)
		except IndexError:
			break

		painted[(x, y)] = colour
		direction = dirs[direction][dir_val]
		x += direction[0]
		y += direction[1]
	if i == 0:
		part_1 = len(painted)

x_vals = [x[0] for x in painted.keys()]
y_vals = [y[0] for y in painted.keys()]
min_x = abs(min(x_vals))
max_x = max(x_vals)
min_y = abs(min(y_vals))
max_y = max(y_vals)

image = [[' ']*(max_x + min_x) for y in range(max_y + min_y)]
print(len(painted))
for panel in painted:
	if painted[panel] == 1:
		image[panel[1] + min_y-1][panel[0] + min_x] = '*'
image = [line for line in image if line.count(' ') < len(image)]

print("Part 1:", part_1)
print("Part 2:")

for i in range(len(image)-1, -1, -1):
	print(''.join(image[i]))