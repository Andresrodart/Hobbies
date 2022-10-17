# Problem: We have a dictionary [string - value] and we will need to perform 3 operations
#   1: PUT - Here we will add a key value to the dict and increment the version
#               RES - PUT(#1) KEY = value
#   2: GET - Here we receive a key and we will send the value or NULL
#               RES - GET KEY = value
#   3: GET_VERSION - Here we receive a key and the version of the value we want, if not exist in the version we look the value from prev versions
#               RES - GET KEY(#VER) = value

# Solution proporsal: We will use double linked list to add a node with, key, value and version
class Node:
	def __init__(self, value, version) -> None:
		self.value = value
		self.version = version
		self.prev = self.next =  self
  
class CircularList:
	def __init__(self, head = None) -> None:
		self.head = head

	def append(self, node):
		if self.head is None:
			self.head = node
		else:
			node.prev = rear = self.head.prev
			rear.next = self.head.prev = node
			node.next = self.head

	def getFrom(self, version):
		node = self.head
		lastSeen = None
		while node.next != self.head and version != node.version:
			if version < node.version: return node.prev
			node = node.next
		return node

	def __repr__(self):
		node = self.head
		res = '--value: ' + str(node.value) + ' version: ' + str(node.version)
		while node.next != self.head:
			node = node.next
			res += '--value: ' + str(node.value) + ' version: ' + str(node.version)
		return res

class KeyValueStore:
	def __init__(self) -> None:
		self.versions = {}
		self.version = 0
	
	def put(self, key, value):
		self.version += 1
		newNode = Node(value, self.version)
		list = self.versions.setdefault(key, CircularList(newNode))
		if list.head != newNode:
			list.append(newNode)
		return 'PUT(#'+ str(newNode.version) +')' + ' ' + key + ' = ' + str(newNode.value)
	
	def get(self, key, version = None):
		if key not in self.versions:
			return self.__getReturn__(key, version)
		return self.__getReturn__(key, version, self.versions[key].getFrom(version if version is not None else self.version))
			
	
	def __getReturn__(self, key, version, node = None):
		value = node.value if node is not None else 'NULL'
		if version is None:
			return 'GET ' + key + ' = ' + str(value)
		return 'GET ' + key + '(#'+ str(version) +') = ' + str(value)

store = KeyValueStore()
# print(store.put('one', 1))
# print(store.put('two', 10))
# print(store.put('one', 100))
# print(store.get('one'))
# print(store.get('one', 3))
# print(store.get('one', 1)) 
# print(store.get('one', 2)) 
# print(store.get('one', 4)) 
# print(store.versions)
filename = 'input.txt'
with open(filename, 'r') as f:
	for line in f:
		inputTokens = line.strip().split(' ')
		if len(inputTokens) == 3:
			[command, key, value] = inputTokens
			if command == 'GET':
				print(store.get(key, int(value)))

			elif command == 'PUT':
				print(store.put(key, int(value)))
		else:
			[command, key] = inputTokens
			if command == 'GET':
				print(store.get(key))
