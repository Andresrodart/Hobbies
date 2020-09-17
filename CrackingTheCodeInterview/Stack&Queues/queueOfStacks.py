class queueOfstacks:
	def __init__(self):
		self._in_ = [] 
		self._out_ = []
	def add(self, data):
		if len(self._in_) == 0: self.move2in()
		self._in_.append(data)
	def remove(self):
		if len(self._out_) == 0: self.move2out() 
		if len(self._out_) == 0: raise Exception('Empty queue')
		return self._out_.pop()
	def move2in(self):
		while self._out_: self._in_.append(self._out_.pop())
	def move2out(self):
		while self._in_: self._out_.append(self._in_.pop())

if __name__ == '__main__':
	que = queueOfstacks()
	for i in range(30): que.add(i)
	for i in range(30): print(que.remove(), end=', ')
	#que.remove()