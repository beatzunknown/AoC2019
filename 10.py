import math

asteroids = []
with open("10.txt", "r") as f:
	for y, row in enumerate(f.readlines()):
		for x, val in enumerate(row.strip()):
			if val == "#":
				asteroids.append((x,y))

max_ast = 0
station = (0, 0)
for x, y in asteroids:
	detected = set()
	for x2, y2 in asteroids:
		if (x, y) != (x2, y2):
			dist_x = x2 - x
			dist_y = y2 - y
			detected.add(math.atan2(dist_x, dist_y))
	if len(detected) > max_ast:
		max_ast = len(detected)
		station = (x, y)

vaporization_data = {}
for x, y in asteroids:
	if (x, y) != station:
		dist_x = x - station[0]
		dist_y = -(y - station[1]) # to account for y axis going down
		dist = abs(dist_x) + abs(dist_y)
		angle = math.atan2(dist_x, dist_y)
		vaporization_data.setdefault(angle, []).append((dist, x, y))
		vaporization_data[angle].sort(key=lambda x:x[0], reverse=True)

positive = sorted(x for x in vaporization_data.keys() if x >= 0)
negative = sorted(x for x in vaporization_data.keys() if x < 0)
angles = positive + negative

vaporized = [station]
while len(vaporized) < len(asteroids):
	for angle in angles:
		if vaporization_data[angle]:
			vaporized.append(vaporization_data[angle].pop())

print(vaporized[50], vaporized[100], vaporized[199], vaporized[200])
part_2 = vaporized[200][1] * 100 + vaporized[200][2]
print("Part 1:", max_ast)
print("Part 2:", part_2)
