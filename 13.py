from intcode import IntCode

with open("13.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

computer = IntCode(state, [])

x = y = tile = 0
mapping = {}

while not computer.is_completed():
	try:
		x = computer.execute([])
		y = computer.execute([])
		tile = computer.execute([])
		mapping[(x,y)] = tile
	except IndexError:
		break

state[0] = 2
computer = IntCode(state, [])

ball_x = paddle_x = points = 0

def joystick():
	if ball_x < paddle_x:
		return -1
	elif ball_x > paddle_x:
		return 1
	else:
		return 0

while not computer.is_completed():
	try:
		x = computer.execute(joystick)
		y = computer.execute(joystick)
		tile = computer.execute(joystick)
		if tile == 3:
			paddle_x = x
		elif tile == 4:
			ball_x = x
		if (x,y) == (-1,0):
			points = tile
	except IndexError:
		break

print("Part 1:", sum(1 if mapping[k]==2 else 0 for k in mapping.keys()))
print("Part 2:", points)