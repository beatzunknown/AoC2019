lower = 125730
upper = 579381

multi_digits = double_digits = 0

for num in range(lower, upper+1):
	pword = str(num)
	if pword[5]>=pword[4]>=pword[3]>=pword[2]>=pword[1]>=pword[0]:
		# if there is a multiple count there are adjacent digits
		# since digits in increasing order
		counts = [pword.count(c) for c in pword]
		double_digits += (2 in counts)
		multi_digits += any(c >= 2 for c in counts)

print("Part 1:", multi_digits)
print("Part 2", double_digits)