import itertools
from intcode_7 import IntCode

with open("07.txt", "r") as f:
	state = list(map(int, f.readline().strip().split(",")))

max_signal = 0

for perm in list(itertools.permutations([0, 1, 2, 3, 4])):
	prev_amp = 0
	for i in range(5):
		computer = IntCode([x for x in state], [])
		prev_amp = computer.execute([perm[i], prev_amp])
	max_signal = max(max_signal, prev_amp)

part_1 = max_signal

max_signal = 0

for perm in list(itertools.permutations([5,6,7,8,9])):
	states = [[x for x in state] for y in range(5)]
	computers = [IntCode(states[i], [perm[i]]) for i in range(5)]
	prev_amp = 0
	completed_computers = 0
	while completed_computers < 5:
		for i in range(5):
			if not computers[i].is_completed():
				#state = [x for x in state_old]
				prev_amp = computers[i].execute([prev_amp])
			else:
				completed_computers += 1
	max_signal = max(max_signal, prev_amp)
	print("Curr max signal: " + str(max_signal))

print("Part 1:", part_1)
print("Part 2:", str(max_signal))