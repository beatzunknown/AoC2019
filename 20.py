from collections import deque

with open("20.txt", "r") as f:
	mapping = [[c for c in line.rstrip("\r\n")] for line in f.readlines()]

d = [(-1,0), (0,-1), (1,0), (0,1)]

# outer portals will have index 0, and inner portals index 1
portals = {}
points = {}

def add_portal(portal, coord, inner):
	global portals
	if portal not in portals:
		portals[portal] = [coord]
	else:
		portals[portal] += [coord]
	points[coord] = (portal, inner)

# determine bounds for inner region
reg_started = False
reg_r = []
for r in range(2, len(mapping)-2):
	if mapping[r].count(' ') > 4 and not reg_started:
		reg_r += [r]
		reg_started = True
	if mapping[r].count(' ') <= 4 and reg_started:
		reg_r += [r-1]
		break

reg_started = False
reg_c = []
for c in range(2, len(mapping[2])-2):
	col = [row[c] for row in mapping]
	if col.count(' ') > 4 and not reg_started:
		reg_c += [c]
		reg_started = True
	if col.count(' ') <= 4 and reg_started:
		reg_c += [c-1]
		break

# outer vertical portals
for c in range(len(mapping[2])):
	if mapping[0][c].isupper():
		p = mapping[0][c] + mapping[1][c]
		add_portal(p, (2,c), 0)
	if mapping[-2][c].isupper():
		p = mapping[-2][c] + mapping[-1][c]
		add_portal(p, (len(mapping)-3,c), 0)

# outer horizontal portals
for r in range(len(mapping)):
	if mapping[r][0].isupper():
		p = mapping[r][0] + mapping[r][1]
		add_portal(p, (r,2), 0)
	if mapping[r][-2].isupper():
		p = mapping[r][-2] + mapping[r][-1]
		add_portal(p, (r,len(mapping[2])-3), 0)

# inner vertical portals
for c in range(reg_c[0], reg_c[1]+1):
	if mapping[reg_r[0]][c].isupper():
		p = mapping[reg_r[0]][c] + mapping[reg_r[0]+1][c]
		add_portal(p, (reg_r[0]-1,c), 1)
	if mapping[reg_r[1]-1][c].isupper():
		p = mapping[reg_r[1]-1][c] + mapping[reg_r[1]][c]
		add_portal(p, (reg_r[1]+1,c), 1)

# inner horizontal portals
for r in range(reg_r[0], reg_r[1]+1):
	if mapping[r][reg_c[0]].isupper():
		p = mapping[r][reg_c[0]] + mapping[r][reg_c[0]+1]
		add_portal(p, (r,reg_c[0]-1), 1)
	if mapping[r][reg_c[1]-1].isupper():
		p = mapping[r][reg_c[1]-1] + mapping[r][reg_c[1]]
		add_portal(p, (r,reg_c[1]+1), 1)

def no(level):
	return True

def yes(level):
	return (level==0)

def neighbours(src):
	return [tuple(sum(pos) for pos in zip(src,mov)) for mov in d]

def bfs(g, src, dest, check_recursion):
	q = deque()
	q.append((src, 0, 0))
	seen = [(src, 0)]
	while len(q):
		src, dist, level = q.popleft()
		for c in neighbours(src):
			if g[c[0]][c[1]] == '.' and (c, level) not in seen:
				if c in points:
					if points[c][0] == 'AA':
						continue
					if points[c][0] == 'ZZ':
						if check_recursion(level) or check_recursion==no:
							return dist+1
						else:
							continue
					is_inner = points[c][1]
					warp = portals[points[c][0]][not is_inner]
					if is_inner:
						if level > len(portals.keys()):
							continue
						q.append((warp, dist+2, level+1))
						seen.append((warp, level+1))
					else:
						if level == 0 and check_recursion==yes:
							continue
						q.append((warp, dist+2, level-1))
						seen.append((warp, level-1))
				else:
					q.append((c, dist+1, level))
				seen.append((c, level))
	return 1000000

def remove_deadends(mapping):
	deadends = deque()
	for r in range(2,len(mapping)-2):
		for c in range(2, len(mapping[0])-2):
			n = neighbours((r,c))
			if mapping[r][c]=='.' and sum([mapping[x[0]][x[1]]=='#' for x in n]) == 3:
				deadends.append((r,c))

	while len(deadends):
		r,c = deadends.pop()
		mapping[r][c] = '#'
		for nr,nc in neighbours((r,c)):
			if mapping[nr][nc]=='.' and sum([mapping[x[0]][x[1]]=='#' for x in neighbours((nr,nc))]) == 3:
				deadends.append((nr,nc))

remove_deadends(mapping)

print("Part 1:", bfs(mapping, portals['AA'][0], portals['ZZ'][0], check_recursion=no))
print("Part 2:", bfs(mapping, portals['AA'][0], portals['ZZ'][0], check_recursion=yes))