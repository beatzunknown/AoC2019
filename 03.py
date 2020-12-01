
def process_data(cmds, coords, steps):
	D = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
	x = 0
	y = 0
	step = 0
	for cmd in cmds:
		direction = cmd[0]
		dist = int(cmd[1:])
		x_delta, y_delta = D[direction]
		while dist > 0:
			dist -= 1
			step += 1
			x += x_delta
			y += y_delta
			coords.append((x,y))
			steps.setdefault((x,y), []).append(step)

coords = []
cmd_list = []
steps = []

with open("03.txt", "r") as f:
	i = 0
	for line in f.readlines():
		cmds = line.strip().split(",")
		cmd_list.append(cmds)
		steps.append({})
		coords.append([])
		process_data(cmds, coords[i], steps[i])
		i += 1

dups = set(coords[0]).intersection(coords[1])

dists = [abs(d[0]) + abs(d[1]) for d in set(dups)]

print(dups)
steps_combined = [min(steps[0][c]) + min(steps[1][c]) for c in dups]

print("Part 1:", min(dists))
print("Part 2:", min(steps_combined))