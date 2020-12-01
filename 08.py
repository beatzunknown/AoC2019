w = 25
h = 6

with open("08.txt", "r") as f:
	data = f.readline().strip()
	layers = [data[x:x+w*h] for x in range(0, len(data), w*h)]

zero_counts = {x:x.count("0") for x in layers}
least_zeros = min(layers, key=zero_counts.get)
part_1 = least_zeros.count("1") * least_zeros.count("2")

final_img = ""
for i in range(w*h):
	new = "2"
	for j in range(len(layers)):
		if not layers[j][i] == "2":
			new = layers[j][i]
			break
	final_img += ('*' if new=='1' else ' ')

print("Part 1:", part_1)
print("Part 2 Image:")
for i in range(h):
	print(final_img[i*w:(i+1)*w])