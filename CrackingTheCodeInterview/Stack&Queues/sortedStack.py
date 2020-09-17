def sortStack(stack):
	SortedStack = [stack.pop()]
	while stack:
		temp = stack.pop()
		while SortedStack and temp > SortedStack[-1]: stack.append(SortedStack.pop())
		SortedStack.append(temp)
		while stack and SortedStack[-1] > stack[-1]: SortedStack.append(stack.pop())
	return SortedStack

if __name__ == '__main__':
	stack = [5, 2, 0, 3, 4, 1]
	stack = sortStack(stack)
	print(stack)