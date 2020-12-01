with open("06.txt", "r") as f:
	data = [line.strip().split(")") for line in f.readlines()]

mapping = {}
for entry in data:
	if entry[0] in mapping:
		mapping[entry[0]] += [entry[1]]
	else:
		mapping[entry[0]] = [entry[1]]

for i in range(6):
	for key in mapping:
		new_vals = []
		for val in mapping[key]:
			new_vals += mapping.get(val, [])
		mapping[key] += new_vals
		mapping[key] = list(set(mapping[key]))

num_orbits = sum(len(mapping[key]) for key in mapping)

mapping = {}
for entry in data:
	if entry[0] in mapping:
		mapping[entry[0]] += [entry[1]]
	else:
		mapping[entry[0]] = [entry[1]]
	if entry[1] in mapping:
		mapping[entry[1]] += [entry[0]]
	else:
		mapping[entry[1]] = [entry[0]]

seen = set()
distances = []

def dfs_path_find(src, dest, curr_dist, seen):
	seen.add(src)
	global distances
	for node in mapping[src]:
		if node == dest:
			distances.append(curr_dist-1)
			return
		elif not node in seen:
			dfs_path_find(node, dest, curr_dist+1, seen)
	return

dfs_path_find("YOU", "SAN", 0, seen)

print("Part 1:", num_orbits)
print("Part 2:", distances[0])