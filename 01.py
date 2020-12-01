with open("01.txt", "r") as f:
	fuels = [x // 3 - 2 for x in list(map(int, f.readlines()))]
	fuel_sum = 0
	for fuel in fuels:
		while fuel > 0:
			fuel_sum += fuel
			fuel = fuel // 3 - 2

	print("Part 1:", sum(fuels))
	print("Part 2:", fuel_sum)