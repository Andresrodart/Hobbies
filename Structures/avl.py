class node:
	def __init__(self, key):
		self.value = key
		self.height = 1
		self.right = None
		self.left = None

class AVL:
	"""
		AVL of unique elements
	"""
	def __init__(self):
		self.root = None
	def add(self, key):
		# if self.root is None: self.root = node(key)
		location = self.find(key)
		location = node(key)
		location.height = 1
		self.balance()

	def find(self, value):
		iterator = self.root
		while iterator.value != value or iterator is not None:
			if iterator.left or iterator.right: iterator.height = 1 + max(iterator.left.height, iterator.right.height)
			if value > iterator.value: iterator = iterator.right
			else: iterator = iterator.left
		return iterator
