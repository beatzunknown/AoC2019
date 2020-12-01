with open("22.txt", "r") as f:
	shuffles = [line.strip().split() for line in f.readlines()]

def execute(func, args):
	if args[1].isalpha():
		return func(args[0])
	else:
		return func(args[0], int(args[1]))

def new_stack(deck):
	return deck[::-1]

def cut(deck, n):
	n = n % len(deck)
	return deck[n:] + deck[:n]

def increment(deck, n):
	size = len(deck)
	deck = new_stack(deck)
	table = [-1 for i in deck]
	i = 0
	while len(deck) > 0:
		if table[i] == -1:
			table[i] = deck.pop()
		i = (i+n) % size
	return table

funcs = {'new': new_stack,
		 'cut': cut,
		 'increment': increment}

def shuffle(deck_size, num_shuffles):
	deck = list(range(deck_size))
	for i in range(num_shuffles):
		for s in shuffles:
			deck = execute(funcs[s[-2]], (deck, s[-1]))
	return deck

print("Part 1:", shuffle(10007, 1).index(2019))
#print("Part 2:", shuffle(119315717514047, 1).index(2020))
