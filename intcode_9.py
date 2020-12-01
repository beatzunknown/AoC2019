instruction_size = {
	99: 1,
	1: 4,
	2: 4,
	3: 2,
	4: 2,
	5: 3,
	6: 3,
	7: 4,
	8: 4,
	9: 2
}

class IntCode:
	def __init__(self, state, inputs):
		for i in range(10000):
			state.append(0)
		self.memory_initial = state
		self.memory = [x for x in state]
		self.pc = 0
		self.ic = 0 #input counter
		self.inputs = inputs
		self.outputs = []
		self.halted = False
		self.completed = False
		self.rb = 0

	def execute(self, inputs):
		self.inputs += inputs
		while self.pc < len(self.memory) and not self.halted:
			i = self.pc
			data = str(self.memory[i])
			op = int(data[-2:])
			p = [0,0,0]
			for j in range(len(data[:-2])):
				p[j] = int(data[:-2][len(data[:-2])-1-j])

			if instruction_size[op] > 1:
				if p[0] == 1:
					r1 = i+1
				else:
					r1 = self.memory[i+1] + (0 if p[0] == 0 else self.rb)
				if instruction_size[op] > 2:	
					if p[1] == 1:
						r2 = i+2
					else:
						r2 = self.memory[i+2] + (0 if p[1] == 0 else self.rb)
					if instruction_size[op] > 3:
						if p[2] == 1:
							r3 = i+3
						else:
							r3 = self.memory[i+3] + (0 if p[2] == 0 else self.rb)
			#print(data, r1, r2, r3, i, p)
			#print(type(self.memory[r3]), type(self.memory[r1]), type(self.memory[r2]))
			if op == 99:# or r1>l or r2>l or r3>l:
				self.halted = True
				self.completed = True
				break
			elif op == 1:
				self.memory[r3] = self.memory[r1] + self.memory[r2]
			elif op == 2:
				self.memory[r3] = self.memory[r1] * self.memory[r2]
			elif op == 3:
				try:
					self.memory[r1] = self.inputs[self.ic]
					self.ic += 1
				except IndexError:
					#print("run")
					self.halted = True
					break
			elif op == 4:
				print(self.memory[r1])
				self.outputs.append(self.memory[r1])
				#return self.memory[r1]
			elif op == 5:
				if self.memory[r1] != 0:
					self.pc = self.memory[r2]
					continue
			elif op == 6:
				if self.memory[r1] == 0:
					self.pc = self.memory[r2]
					continue
			elif op == 7:
				self.memory[r3] = self.memory[r1] < self.memory[r2]
			elif op == 8:
				self.memory[r3] = self.memory[r1] == self.memory[r2]
			elif op == 9:
				self.rb += self.memory[r1]

			self.pc += instruction_size[op]

		self.halted = False
		return self.outputs.pop(len(self.outputs) - 1)

	def is_halted(self):
		return self.halted

	def is_completed(self):
		return self.completed