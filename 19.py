from intcode import IntCode
from queue import Queue

with open("19.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

q = Queue()

def execute():
	return IntCode(state, []).execute(input_func)

def add_input(data):
	global q
	for elem in data:
		q.put(elem)

def input_func():
	global q
	return q.get()

mapping = [['.' for i in range(50)] for j in range(50)]
affected = 0
start_x = 0
for y in range(50):
	add_input([start_x, y])
	while execute() == 0 and start_x < 49:
		start_x += 1
		add_input([start_x, y])
	if start_x == 49:
		start_x = 0
	for x in range(start_x, 50):
		add_input([x, y])
		out = execute()
		affected += out
		if out == 1:
			mapping[y][x] = '#'
		else:
			break

for row in mapping:
	print(''.join(row))

y = x = 50
complete = False
while not complete:
	add_input([start_x, y])
	while execute() == 0:
		start_x += 1
		add_input([start_x, y])
	x = start_x
	while True:
		add_input([x, y])
		if execute():
			add_input([x+99, y])
			if execute():
				add_input([x, y+99, x+99, y+99, x, y+49, x+99, y+49])
				if sum([execute() for i in range(4)]) == 4:
					complete = True
					break
			else:
				break
		else:
			break
		x += 1
	y += 1
y -= 1

part_2 = x*10000 + y

print("Part 1:", affected)
print("Part 2:", part_2)
