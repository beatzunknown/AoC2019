import sys, copy
from intcode import IntCode

sys.setrecursionlimit(10**8)

directions = [(), (0,-1), (0,1), (-1,0), (1,0)]

with open("15.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

computer = IntCode(state, [])

x = y = 0
seen = {(x,y):0}
move_to_make = 1
oxygen = None
part_1 = 100000000000000000000000000000

def reverse_move(d):
	return d-1 if d%2==0 else d+1

def move():
	return move_to_make

def step(computer, steps, x, y, direction, seen):
	global move_to_make, part_1, oxygen
	x_move,y_move = directions[direction]
	new_x = x + x_move
	new_y = y + y_move
	if (new_x, new_y) in seen:
		return
	move_to_make = direction
	status = computer.execute(move)
	steps += 1
	if status == 2:
		print(4230979038290849038)
		part_1 = min(part_1, steps)
		oxygen = (new_x, new_y)
	seen[(new_x, new_y)] = status
	if status == 0:
		return 0
	else:
		x, y = new_x, new_y
		for i in range(1,5):
			if i == reverse_move(direction):
				continue
			step(copy.deepcopy(computer), steps, x, y, i, seen)
	return 1

for i in range(1,5):
	step(copy.deepcopy(computer), 0, x, y, i, seen)

x_coords = set([x for x,y in seen])
y_coords = set([y for x,y in seen])
row_size, col_size = len(x_coords), len(y_coords)
oxygen = (oxygen[0] + abs(min(x_coords)), oxygen[1] + abs(min(y_coords)))
filled = [oxygen]
mapping = []
for i in range(min(y_coords), max(y_coords)+1):
	line = ''
	row = []
	for j in range(min(x_coords), max(x_coords)+1):
		line += str(seen.get((i,j), 0))
		row += [seen.get((i,j), 0)]
	mapping.append(row)
	print(line)

part_2 = 0
while filled:
	new_filled = []
	for location in filled:
		for direction in directions[1:]:
			x, y = tuple([sum(z) for z in zip(location, direction)])
			if 0 <= x < row_size and 0 <= y < col_size:
				if mapping[x][y] == 1:
					mapping[x][y] = 0
					new_filled.append((x,y))
	filled = new_filled
	part_2 += 1
part_2 -= 1

print("Part 1:", part_1)
print("Part 2:", part_2)