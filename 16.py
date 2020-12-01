with open("16.txt", "r") as f:
	seq_orig = [int(c) for c in f.readline().strip()]

def gen_pattern(pos, size, pattern_base):
	pattern = []
	pattern_len = -1
	while size > pattern_len:
		for i in range(len(pattern_base)):
			pattern += [pattern_base[i]] * pos
			pattern_len += pos
	return pattern[1:size+1]

def fft(nums, patterns):
	output = []
	for i in range(len(nums)):
		num = 0
		for j in range(len(nums)):
			num += nums[j]*patterns[i][j]
		output.append(int(str(num)[-1]))
	return output

seq = [x for x in seq_orig]
pattern_base = [0,1,0,-1]
phases = 100
patterns = [gen_pattern(i+1, len(seq), pattern_base) for i in range(len(seq))]

for i in range(phases):
	seq = fft(seq, patterns)

part_1 = ''.join([str(x) for x in seq[:8]])

seq = [x for x in seq_orig] * 10000
offset = int(''.join(str(c) for c in seq[:7]))
seq = seq[offset:]

for phase in range(100):
	for i in range(len(seq)-1, 0, -1):
		seq[i-1] = (seq[i] + seq[i-1]) % 10

part_2 = ''.join([str(x) for x in seq[:8]])

print("Part 1:", part_1)
print("Part 2:", part_2)