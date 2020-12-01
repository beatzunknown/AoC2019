import math

mapping = {}

with open("14.txt", "r") as f:
	for line in f.readlines():
		solvents,solution = line.strip().split(" => ")
		solvents = [(int(x.split()[0]), x.split()[1]) for x in solvents.split(", ")]
		mapping[solution.split()[1]] = (int(solution.split()[0]), solvents)

remnants = {key:0 for key in mapping.keys()}
remnants["ORE"] = 0

ores = part_1 = part_2 = 0
max_ores = 1000000000000

def calc_required_ores(product):
	global remnants
	ores = 0
	qty = product[0]
	prod = product[1]
	surplus = remnants.get(prod, 0)
	needed = qty-surplus
	multiple = math.ceil(max([needed, 0]) / mapping[prod][0])
	remnants[prod] = mapping[prod][0] * multiple - needed
	for solvent in mapping[prod][1]:
		if solvent[1] == 'ORE':
			ores += multiple * solvent[0]
		else:
			ores += calc_required_ores((multiple * solvent[0], solvent[1]))
	return ores

part_1 = calc_required_ores((1, 'FUEL'))

max_ores = 1000000000000
ores_used = 0
fuels = 0
mode = 10
while ores_used < max_ores or mode > -1:
	remnants = {key:0 for key in mapping.keys()}
	ores_used = calc_required_ores((fuels + 10**mode, 'FUEL'))
	if ores_used < max_ores:
		fuels += 10**mode
	else:
		mode -= 1

print("Part 1:", part_1)
print("Part 2:", fuels)