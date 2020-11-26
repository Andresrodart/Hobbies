class skipList:
    def __init__(self):
        pass
    def search(self, value):
        node = self.head
        while node.below:
            node = node.below
            while vale >= node.value:
                node = node.next
        return node
    def inster(self, value)
        node, q, i, coin = self.search(value), None, True
        while coin:
            i += 1
            if i >= h: 
                h += 1
                self.createNewLevel()
            while p.above is None:
                