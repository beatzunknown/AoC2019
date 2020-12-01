import itertools
from intcode import IntCode

with open("09.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

def input_1():
	return 1

def input_2():
	return 2

part_1 = IntCode(state, []).execute(input_1)
part_2 = IntCode(state, []).execute(input_2)

print("Part 1:", part_1)
print("Part 2:", part_2)