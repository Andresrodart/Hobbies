class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def replace(self, data): self.data = data

class LinkedList:
	def __init__(self, arry = None):
		self.head = None
		self.length = 0
		if arry: 
			for element in arry: self.append(element)
	def append(self, data):
		if self.head is None: 
			self.head = Node(data)
			self.length = 1
		else:
			end = self.last()
			end.next = Node(data)
			self.length += 1
	def push(self, data):
		new_head = Node(data)
		new_head.next = self.head
		self.head = new_head
		self.length += 1
	def last(self):
		iterator = self.head
		while iterator.next is not None: iterator = iterator.next
		return iterator
	def findIth(self, index):
		if index < 0 or index >= self.length: raise Exception('{} out of list bounds'.format(index))
		iterator = self.head
		for i in range(index): iterator = iterator.next
		return iterator
	def decapitate(self):
		self.head = self.head.next
		self.length -= 1
	def dequeue(self):
		prev_end = self.findIth(self.length - 2)
		prev_end.next = None
		self.length -= 1
	def deleteNext(self, node):
		node.next = node.next.next
		self.length -= 1
		return True
	def deleteByIndex(self, index):
		if index == 0: self.decapitate()
		elif index == self.length - 1: self.dequeue()
		else: self.deleteNext(self.findIth(index - 1))
	def stringtify(self):
		iterator = self.head
		res = []
		while iterator is not None:
			res.append(str(iterator.data))
			iterator = iterator.next
		return '[' + ', '.join(res) + ']'
	#############	Problems	###############
	def removeDuplicates(self):
		iterator, prev = self.head.next, self.head
		# Fast
		seen = set([prev.data])
		while iterator is not None: 
			if iterator.data in seen: self.deleteNext(prev)
			else: 
				seen.add(iterator.data)
				prev = prev.next
			iterator = iterator.next
		# Less Memory
		# iterator = self.head
		# while iterator is not None:
		# 	prev = iterator
		# 	iterator_2 = iterator.next
		# 	while iterator_2 is not None:
		# 		if iterator.data == iterator_2.data: self.deleteNext(prev)
		# 		else: prev = prev.next
		# 		iterator_2 = iterator_2.next
		# 	iterator = iterator.next
	def kthToLast(self, k):
		return self.findIth(self.length - 1 - k)
	def delete(self, node):
		if node is None: return False 
		elif node.next is None: self.dequeue()
		else: 
			node.data = node.next.data
			node.next = node.next.next
			self.length -= 1
	def partition(self, value):
		new_list = LinkedList()
		iterator = self.head
		while iterator is not None:
			if iterator.data < value: new_list.push(iterator.data)
			else: new_list.append(iterator.data)
			iterator = iterator.next
		self.head = new_list.head
	def isPalindrome(self):
		if self.head is None or self.head.next is None: return True
		if self.head.next.next is None: return True if self.head.next.data == self.head.data else False
		i, j, count, stack = self.head, self.head, 0, []
		while j.next is not None:
			j = j.next
			if count % 2 == 0: 
				stack.append(i.data)
				i = i.next
			count += 1
		if (count + 1) // 2 != 0: i = i.next
		# j, queue = self.head, []
		while i is not None:
			if i.data != stack.pop(): return False
			i = i.next
			# stack.insert(0, i.data)
			# queue.append(j.data)
			# i, j = i.next, j.next
		# if queue == stack: return True
		# return False
		return True
	def doesIntersec(self, LinkedList):
		i = self.head if LinkedList.length < self.length else LinkedList.head
		j = self.head if LinkedList.length > self.length else LinkedList.head
		for _ in range(abs(LinkedList.length - self.length)): i = i.next
		while i is not None and i is not j and i != j: i, j = i.next, j.next
		if i is None: return False
		else: return True
		# resI, ResJ = i, j
		# while i is not None:
		# 	if i.data != j.data: return False
		# 	i, j = i.next, j.next
		# return resI if resI is ResJ else False
	def hasLoop(self):
		hashTable, iterator = set(), self.head
		while iterator is not None:
			if id(iterator) in hashTable: return iterator
			else: hashTable.add(id(iterator))
			iterator = iterator.next
		return None
	def re_length(self):
		self.length = 0
		iterator = self.head
		while(iterator is not None):
			self.length +=1
			iterator = iterator.next
	def reverse(self):
		tail = self.head
		prev =  self._reverse(self.head.next)
		prev.next, tail.next = tail, None
	def _reverse(self, next_):
		if next_.next is None:
			self.head = next_
			return self.head
		prev = self._reverse(next_.next)
		prev.next = next_
		return next_
def reverseSum(numA, numB):
	res = LinkedList()
	iA, iB, carry = numA.head, numB.head, False
	while iA is not None and iB is not None:
		parSum = iA.data + iB.data + (1 if carry else 0)
		if parSum >= 10: 
			res.append(parSum - 10)
			carry = True
		else:
			res.append(parSum)
			carry = False
		iA, iB = iA.next, iB.next
	if iA is not None or iB is not None:
		iA = iA if iB is None else iB
		parSum = iA.data + (1 if carry else 0)
		if parSum >= 10: 
			res.append(parSum - 10)
			carry = True
		else:
			res.append(parSum)
			carry = False
		iA = iA.next
		while iA is not None:
			res.append(iA.data + (1 if carry else 0))
			carry = False
			iA = iA.next
	if carry: res.append(1)
	return res
def LinkedSum(numA, numB):
	if numB.length > numA.length: numA, numB = numB, numA
	for i in range(numA.length - numB.length): numB.push(0)
	
	iA, iB = numA.head, numB.head
	if iA.data + iB.data > 10: res = LinkedList([1, iA.data + iB.data - 10])
	else: res = LinkedList([iA.data + iB.data])
	
	iA, iB, prev = iA.next, iB.next, res.head
	while iA is not None and iB is not None:
		if iA.data + iB.data >= 10: 
			res.append(iA.data + iB.data - 10)
			prev.data += 1
		else: res.append(iA.data + iB.data)
		iA, iB, prev = iA.next, iB.next, prev.next
	return res
def isPalindrome(node, index, length, stack):
	if index > length: return True
	if index > length // 2:
		if length % 2 != 0 and index == length // 2 + 1: return True and isPalindrome(node.next, index + 1, length, stack)
		return node.data == stack.pop() and isPalindrome(node.next, index + 1, length, stack)
	else:
		stack.append(node.data)
		return isPalindrome(node.next, index + 1, length, stack)
if __name__ == "__main__":
	LL = LinkedList()
	LL.push(10)
	LL.append(0)
	print(LL.stringtify())
	LL = LinkedList(arry = [1, 8, 6, 79])
	LL.deleteByIndex(2)
	LL.decapitate()
	LL.dequeue()
	print(LL.stringtify())
	LL = LinkedList(arry = [8, 1, 8, 8, 7, 8, 7])
	LL.removeDuplicates()
	print(LL.stringtify())
	LL = LinkedList(arry = [8, 8, 2, 3, 4, 8])
	LL.delete(LL.findIth(2))
	print(LL.stringtify())
	print(reverseSum(LinkedList([7, 1, 7]), LinkedList([5, 9, 2, 9, 1, 2, 3])).stringtify())
	print(LinkedSum(LinkedList([1, 1, 6, 1, 7]), LinkedList([2, 9 ,5])).stringtify())
	LL = LinkedList(arry = [3, 5, 8, 5, 10, 2, 1])
	LL.partition(5)
	print(LL.stringtify())
	LL = LinkedList(arry = [1, 0, 0, 2, 0, 0, 1])
	print(LL.isPalindrome())
	print(isPalindrome(LL.head, 1, LL.length, []))
	LL = LinkedList(arry = list('xbbxxbba'))
	print(LL.isPalindrome())
	print(isPalindrome(LL.head, 1, LL.length, []))
	print(LL.doesIntersec(LinkedList(arry = list('xbba'))))
	LL2 = LinkedList(arry = list('717'))
	ref = LL.head
	for i in range(LL.length - LL2.length): ref = ref.next
	LL2.head.next.next = ref
	LL2.re_length()
	print(LL.doesIntersec(LL2))
	LL = LinkedList(arry = [3, 5, 8, 5, 10, 2, 1])
	print(LL.hasLoop())
	LL.last().next = LL.findIth(3)
	print(LL.hasLoop().data)
	LL = LinkedList(arry = list('xbbxxbba'))
	print(LL.stringtify())
	LL.reverse()
	print(LL.stringtify())
	