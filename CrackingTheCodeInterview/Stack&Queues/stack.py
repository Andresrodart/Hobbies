class setOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.setOfStacks = [[]]
		self.actualStack = 0
	def push(self, data):
		if self.capacity == len(self.setOfStacks[self.actualStack]):
			self.actualStack += 1
			self.setOfStacks.append([data])
		else: self.setOfStacks[self.actualStack].append(data)
	def pop(self):
		if self.actualStack == 0 and len(self.setOfStacks[0]) == 0: raise Exception('No elements in stack')
		elif len(self.setOfStacks[self.actualStack]) == 0:	self.actualStack -= 1
		return self.setOfStacks[self.actualStack].pop()
	def peek(self):
		if self.actualStack == 0 and len(self.setOfStacks[0]) == 0: raise Exception('No elements in stack')
		elif len(self.setOfStacks[self.actualStack]) == 0:	self.actualStack -= 1
		return self.setOfStacks[self.actualStack][-1]
	def popFrom(self, index):
		if index > self.actualStack or index < 0: raise Exception('index out of bounds')
		elif len(self.setOfStacks[index]) == 0: raise Exception('No elements in stack')
		else: return self.setOfStacks[index].pop()

if __name__ == '__main__':
	stkset = setOfStacks(2)
	for i in range(30): stkset.push(i)
	stkset.popFrom(2)
	for i in range(30): print(stkset.pop(), end=', ')
	