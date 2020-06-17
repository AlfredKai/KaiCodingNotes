class LRUCache:

    def __init__(self, capacity: int):
        self.list = [-1] * capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            index = self.list.index(key)
            val = self.list[index]
            for i in range(index, 0, -1):
                self.list[i] = self.list[i-1]
            self.list[0] = val
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if self.list[-1] != -1:
                del self.dict[self.list[-1]]
            for i in range(len(self.list)-1, 0, -1):
                self.list[i] = self.list[i-1]
            self.list[0] = key
        else:
            index = self.list.index(key)
            val = self.list[index]
            for i in range(index, 0, -1):
                self.list[i] = self.list[i-1]
            self.list[0] = val
        self.dict[key] = value
        # print(self.list)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print(self):
        node = self.head
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print()
            
    def printReverse(self):
        node = self.tail
        while node is not None:
            print(node.val, end=' ')
            node = node.prev
        print()

    def add(self, x):
        if self.head == None:
            self.head = ListNode(x)
            self.tail = self.head
        else:
            node = ListNode(x)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def addNode(self, x):
        if self.head == None:
            self.head = x
            self.tail = self.head
        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = x

    def addNodeToHead(self, x):
        if self.head == None:
            self.head = x
            self.tail = self.head
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x

# double link list
class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.list = DoubleLinkedList()
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            if key != self.list.head.val[0]:
                prevNode = node.prev
                node.prev.next = node.next
                if node.next != None:
                    node.next.prev = prevNode
                if key == self.list.tail.val[0]:
                    self.list.tail = node.prev
                self.list.head.prev = node
                node.next = self.list.head
                node.prev = None
                self.list.head = node
            return self.dict[key].val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            node = ListNode((key, value))
            self.dict[key] = node
            self.list.addNodeToHead(node)
            if self.length < self.capacity:
                self.length += 1
            else:
                del self.dict[self.list.tail.val[0]]
                self.list.tail.prev.next = None
                self.list.tail = self.list.tail.prev
        else:
            node = self.dict[key]
            if key != self.list.head.val[0]:
                prevNode = node.prev
                node.prev = node.next
                if node.next != None:
                    node.next.prev = prevNode
                self.list.head.prev = node
                node.next = self.list.head
                node.prev = None
                self.list.head = node
            node.val = (key, value)
        # print(self.list)

# using OrderedDict
from collections import OrderedDict

class LRUCache3:

    def __init__(self, capacity: int):
        self.ordict = OrderedDict()
        self.count = capacity

    def get(self, key: int) -> int:
        if key in self.ordict:
            self.ordict.move_to_end(key)
        else:
            return -1
        return self.ordict[key]

    def put(self, key: int, value: int) -> None:
        self.ordict[key] = value
        if key in self.ordict:
            self.ordict.move_to_end(key)
        if len(self.ordict) > self.count:
            self.ordict.popitem(False)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache2(2)
obj.put(1, 1)
obj.put(2, 2)
obj.list.print()
obj.list.printReverse()
print(obj.get(1))
obj.list.print()
obj.list.printReverse()
obj.put(3, 3)
obj.list.print()
obj.list.printReverse()
print(obj.get(2))
# obj.list.print()
# obj.list.printReverse()
obj.put(4, 4)
print(obj.get(1))
obj.list.print()
print(obj.get(3))
print(obj.get(4))

obj = LRUCache2(2)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))

