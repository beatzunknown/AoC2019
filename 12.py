import copy
import math

moon_pos = []
with open("12.txt", "r") as f:
	for line in f.readlines():
		moon_pos.append([int(pos[2:]) for pos in line.strip()[1:-1].split(', ')])

moon_vel = [[0,0,0] for p in moon_pos]

steps = 1000
step = 0

part_1 = x = y = z = 0

# note that the step function is not surjective meaning that no 2 inputs
# produce the same output. Thus if there is a cycle, the first repeated
# state must be the initial state so this is all we have to check.

# Additionally orbits on each axis are independent of each other
memory_x = ([pos[0] for pos in moon_pos], [vel[0] for vel in moon_vel])
memory_y = ([pos[1] for pos in moon_pos], [vel[1] for vel in moon_vel])
memory_z = ([pos[2] for pos in moon_pos], [vel[2] for vel in moon_vel])

while True:
	for i in range(len(moon_pos)):
		for j in range(len(moon_pos)):
			if i != j:
				for k in range(3):
					if moon_pos[i][k] > moon_pos[j][k]:
						moon_vel[i][k] -= 1
					elif moon_pos[i][k] < moon_pos[j][k]:
						moon_vel[i][k] += 1
	for i in range(len(moon_pos)):
		for k in range(3):
			moon_pos[i][k] += moon_vel[i][k]

	step += 1
	if step == steps:
		part_1 = sum([sum(abs(p) for p in moon_pos[i]) * sum(abs(v) for v in moon_vel[i]) for i in range(len(moon_pos))])

	x_tup = ([pos[0] for pos in moon_pos], [vel[0] for vel in moon_vel])
	y_tup = ([pos[1] for pos in moon_pos], [vel[1] for vel in moon_vel])
	z_tup = ([pos[2] for pos in moon_pos], [vel[2] for vel in moon_vel])

	if not x and x_tup == memory_x:
		x = step
	if not y and y_tup == memory_y:
		y = step
	if not z and z_tup == memory_z:
		z = step

	if part_1 != 0 and x != 0 and y != 0 and z != 0:
		break

gcd_xy = x * y // math.gcd(x, y)
part_2 = z * gcd_xy // math.gcd(z, gcd_xy)

print("Part 1:", part_1)
print("Part 2:", part_2)