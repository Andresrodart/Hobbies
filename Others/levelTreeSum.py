# Given a binary tree with no repeted id, staring the root with cero I want to know the
# sum of each level eg:
#	 		0					-> 0
#	 	2			3			-> 5
#	1		3 	2		4		-> 10
# As a result i want an array with does values [0, 5, 10]
#First we have to see that in worst case the length of the tre will be n =  number of nodes 
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def PrintTree(self, level):
		if level:
			for i in range(level):
				print('', end = '\t')
		print( self.data)
		if self.left:
			self.left.PrintTree(level + 1)
		if self.right:
			self.right.PrintTree(level + 1)

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

def sumLevelsAux(node, res, level):
	if len(res) <= level:				#So we check if the level existe as index in the res list
		res.insert(level, node.data)	
	else:
		res[level] += node.data			#If the index exist we just sum the new value
	if node.left:						#And we trasverse in pre-order style checking first that the nodes exist
		sumLevelsAux(node.left, res, level + 1)
	if node.right:
		sumLevelsAux(node.right, res, level + 1)

def sumTreeLevels(root):
	res = [0]							#First element will always be zero, we could make an array of n node lements but I prefer not to
	sumLevelsAux(root.left, res, 1)
	sumLevelsAux(root.right, res, 1)
	return res


root = Node(0)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
res = sumTreeLevels(root)
print(res)
#root.PrintTree(0)