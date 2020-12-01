import copy

with open("24.txt", "r") as f:
	board = [[c for c in line.strip()] for line in f.readlines()]
	size = len(board)

board_orig = copy.deepcopy(board)

d = [(-1,0), (0,-1), (1,0), (0,1)]
boards = []

def empty_board():
	new = [['.' for i in range(size)] for j in range(size)]
	new[size//2][size//2] = '?'
	return new

def neighbours(b, i, j):
	num = 0
	for x,y in d:
		if 0 <= i+x < size and 0 <= j+y < size:
			if boards[b][i+x][j+y] == '#':
				num += 1
			elif boards[b][i+x][j+y] == '?' and b < len(boards)-1:
				inner = boards[b+1]
				if i == size//2 - 1:
					num += sum([1 if inner[0][k] == '#' else 0 for k in range(size)])
				elif i == size//2 + 1:
					num += sum([1 if inner[size-1][k] == '#' else 0 for k in range(size)])
				elif j == size//2 - 1:
					num += sum([1 if inner[k][0] == '#' else 0 for k in range(size)])
				elif j == size//2 + 1:
					num += sum([1 if inner[k][size-1] == '#' else 0 for k in range(size)])
	if b > 0:
		outer = boards[b-1]
		if j == 0:
			num += outer[size//2][size//2 - 1] == '#'
		elif j == size-1:
			num += outer[size//2][size//2 + 1] == '#'
		if i == 0:
			num += outer[size//2 - 1][size//2] == '#'
		elif i == size-1:
			num += outer[size//2 + 1][size//2] == '#'
	return num

def new_state(b, i, j):
	adj = neighbours(b, i, j)
	if boards[b][i][j] == '#':
		return '#' if adj == 1 else '.'
	elif boards[b][i][j] == '.':
		return '#' if 1 <= adj <= 2 else '.'
	else:
		return '?'

def compare(board_a, board_b):
	for i in range(size):
		for j in range(size):
			if board_a[i][j] != board_b[i][j]:
				return False
	return True

def run(b):
	new_board = [[new_state(b, i, j) for j in range(size)] for i in range(size)]
	return copy.deepcopy(new_board)

history = [board]

part_1 = None

boards = [board]
while not part_1:
	boards[0] = run(0)
	if any([compare(boards[0], b) for b in history]):
		part_1 = sum([2**i for i in range(size**2) if boards[0][i//size][i%size] == '#'])
	else:
		history.append(boards[0])

board = copy.deepcopy(board_orig)
board[size//2][size//2] = '?'
boards = [empty_board(), board, empty_board()]

for _ in range(200):
	new_boards = [run(b) for b in range(len(boards))]
	boards = copy.deepcopy(new_boards)
	if not compare(boards[0], empty_board()):
		boards = [empty_board()] + boards
	if not compare(boards[-1], empty_board()):
		boards += [empty_board()]

part_2 = 0
for b in boards:
	for row in b:
		part_2 += row.count('#')

print("Part 1:", part_1)
print("Part 2:", part_2)