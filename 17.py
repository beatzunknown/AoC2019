from intcode import IntCode

with open("17.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

d = [(-1,0), (0,-1), (1,0), (0,1)]

inputs = []
input_i = 0

def part1_input():
	pass

def part2_input():
	global inputs, input_i
	input_i += 1
	return inputs[input_i-1]

def get_neighbours(row, col):
	global d
	return [tuple(sum(pos) for pos in zip((row,col),d[i])) for i in range(len(d))]

def in_range(view, row, col):
	return 0 <= row < len(view) and 0 <= col < len(view[0])

def list_join(l, sep):
	new_list = []
	for i in l:
		new_list += [i, sep]
	return new_list[:-1]

# map generation
view = []
line = []
start = None
computer = IntCode(state, [])
while not computer.is_completed():
	try:
		out = computer.execute(part1_input)
		if out == 10:
			view.append(line)
			line = []
		else:
			line.append(chr(out))
		if chr(out) in "^<v>":
			direction = ['^', '<', 'v', '>'].index(chr(out))
			start = (len(view), len(line)-1)
	except IndexError:
		pass
view.pop() #accounts for extra newline at end

for row in view:
	print(''.join(row))

# alignment parameters
align_param = 0
direction = 0

for r in range(1, len(view)-1):
	for c in range(1, len(view[0])-1):
		if view[r][c] == "#":
			adj_pos = get_neighbours(r,c)
			adj_scaffold = sum([view[y][x]=='#' for (y,x) in adj_pos])
			if adj_scaffold > 2:
				align_param += c*r
		elif view[r][c] in "^<v>":
			direction = ['^', '<', 'v', '>'].index(view[r][c])
			start = (r,c)

# map traversing
moves = []
r,c = start
while True:
	new_direction = None
	opp_direction = (direction + 2) % len(d)
	adj_pos = get_neighbours(r,c)
	adj_pos.pop(opp_direction)
	for i in range(len(d)):
		new_r, new_c = tuple(sum(pos) for pos in zip((r,c),d[i]))
		if in_range(view, new_r, new_c) and view[new_r][new_c] == '#' and i%2 != direction%2:
			new_direction = i
			r,c = new_r,new_c
			break
	if new_direction == None:
		break
	elif new_direction - direction == 1 or new_direction - direction == -3:
		moves.append('L')
	else:
		moves.append('R')

	steps = 1
	while view[r][c] == '#':
		new_r, new_c = tuple(sum(pos) for pos in zip((r,c),d[new_direction]))
		if in_range(view, new_r, new_c) and view[new_r][new_c] == '#':
			r,c = new_r,new_c
			steps += 1
		else:
			break
	moves += [str(steps)]
	direction = new_direction

# movement sequence compression
# kudos to @OverjoyedBanana
# https://www.reddit.com/r/adventofcode/comments/ebr7dg/2019_day_17_solutions/fb8se1o/
compressions = []
compression_sums = []
seq = ' '.join(moves)
for a_e in range(2, 9):
    for b_s in range(a_e+1, len(moves)-3):
        for b_e in range(b_s+2, b_s+2+9):
            a = " ".join(moves[0:a_e*2])
            b = " ".join(moves[b_s*2:b_e*2])
            rem = seq.replace(a, '|').replace(b, '|')
            _,min_c = min((len(c.strip()),c.strip()) for c in rem.split('|') if len(c.strip()) > 0)
            rem = rem.replace(min_c, '').replace(' ', '').replace('|', '')
            if len(rem) == 0:
                #print("FOUND A=%s, B=%s, C=%s" % (a,b,min_c))
                compression = []
                for pattern in [a,b,min_c]:
                	compression.append(pattern.split())
                compressions.append(compression)
                compression_sums.append(sum(len(pat) for pat in compression))

pattern = compressions[compression_sums.index(min(compression_sums))]
#print(pattern)

i = 0
routine = []
while i < len(moves)-1:
	for p in pattern:
		if moves[i:i+len(p)] == p:
			routine += [['A', 'B', 'C'][pattern.index(p)]]
			i += len(p)
			break

routine = list(map(ord, ','.join(routine))) + [ord('\n')]
pattern = [list(map(ord, ','.join(p)))+[ord('\n')] for p in pattern]
inputs = routine
for p in pattern:
	inputs += p
inputs += [ord('n'), ord('\n')]

state[0] = 2
computer = IntCode(state, [])
dust = 0
while not computer.is_completed():
	try:
		dust = computer.execute(part2_input)
	except IndexError:
		break

print("Part 1:", align_param)
print("Part 2:", dust)