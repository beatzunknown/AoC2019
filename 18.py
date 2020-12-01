from collections import deque

part2_data = ['@#@', '###', '@#@']

with open("18.txt", "r") as f:
	mapping = [[c for c in line.strip()] for line in f.readlines()]

def neighbours(src):
	r,c = src
	yield r+1,c
	yield r-1,c
	yield r,c+1
	yield r,c-1

def neighbours2(src):
	for i in range(src):
		r,c = src[i]
		yield src[:i] + [(r+1,c)] + src[i+1:]
		yield src[:i] + [(r-1,c)] + src[i+1:]
		yield src[:i] + [(r,c+1)] + src[i+1:]
		yield src[:i] + [(r,c-1)] + src[i+1:]

def bfs_dist(g, src, dest):
	if src == dest:
		return 0
	state = {}
	keys = frozenset()
	seen = set((src, keys))
	q = deque()
	q.append((src, 1, keys))
	found = False
	while len(q) and not found:
		curr, dist, keys = q.popleft()
		print(set(keys), dist, curr)
		dat = (curr, keys)
		if dat in state:
			if dist > state[dat]:
				continue
		state[dat] = dist
		if len(keys) == dest:
			return dist-1
		for c in neighbours(curr):
			cell = g[c[0]][c[1]]
			if (c, keys) not in seen and (cell == '.' or cell.lower() in keys or cell.islower()):
				if cell.islower() and cell not in keys:
					#print(g[c[0]][c[1]],'\n')
					q.append((c, dist+1, keys|{cell}))
					seen.add((c, keys|{cell}))
				else:
					q.append((c, dist+1, keys))
				seen.add((c, keys))
		#print(curr)
	return 1000000

def bfs_dist2(g, src, dest):
	if src == dest:
		return 0
	state = {}
	keys = frozenset()
	seen = [(src, keys)]
	q = deque()
	q.append((src, 1, keys))
	found = False
	while len(q) and not found:
		curr, dist, keys = q.popleft()
		print(set(keys), dist, curr)
		dat = (tuple(curr), keys)
		if dat in state:
			if dist > state[dat]:
				continue
		state[dat] = dist
		if len(keys) == dest:
			return dist-1
		for b in range(len(curr)):
			bot = curr[b]
			for c in neighbours(bot):
				cell = g[c[0]][c[1]]
				new_curr = curr[:b] + [c] + curr[b+1:]
				if (new_curr, keys) not in seen and (cell == '.' or cell.lower() in keys or cell.islower()):
					if cell.islower() and cell not in keys:
						#print(g[c[0]][c[1]],'\n')
						q.append((new_curr, dist+1, keys|{cell}))
						seen.append((new_curr, keys|{cell}))
					else:
						q.append((new_curr, dist+1, keys))
					seen.append((new_curr, keys))
		#print(curr)
	return 1000000

def remove_deadends(mapping):
	deadends = deque()
	for r in range(1, len(mapping)-1):
		for c in range(1, len(mapping[0])-1):
			if mapping[r][c]=='.' and sum([mapping[x[0]][x[1]]=='#' for x in neighbours((r,c))]) == 3:
				deadends.append((r,c))

	while len(deadends):
		r,c = deadends.pop()
		mapping[r][c] = '#'
		for nr,nc in neighbours((r,c)):
			if mapping[nr][nc]=='.' and sum([mapping[x[0]][x[1]]=='#' for x in neighbours((nr,nc))]) == 3:
				deadends.append((nr,nc))

remove_deadends(mapping)

pos = {}
start = None
for r in range(len(mapping)):
	for c in range(len(mapping[0])):
		if mapping[r][c].islower():
			pos[mapping[r][c]] = (r,c)
		elif mapping[r][c] == '@':
			start = (r, c)
			mapping[r][c] = '.'

mapping2 = [[cell for cell in row] for row in mapping]
start2 = []
for r in range(len(part2_data)):
	for c in range(len(part2_data[0])):
		if part2_data[r][c] == '@':
			start2.append((start[0]-1+r, start[1]-1+c))
		else:
			mapping2[start[0]-1+r][start[1]-1+c] = '#'

print('\n'.join([''.join(l) for l in mapping]))
print('\n'.join([''.join(l) for l in mapping]))

m = ord(min(pos.keys()))
size = ord(max(pos.keys())) - m
print(m, size)
t = 1000000
#print(mapping)
print(pos)
print(m, size, len(pos))
print("Part 1", bfs_dist(mapping, start, len(pos)))
#print("Part 2", bfs_dist2(mapping2, start2, len(pos)))

