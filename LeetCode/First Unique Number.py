from typing import List

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.rec = {}
        self.deleted = set()
        self.head = None
        self.tail = None
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if self.head == None:
            return -1
        return self.head.val

    def add(self, value: int) -> None:
        if value in self.deleted:
            return
        if value in self.rec:
            node = self.rec[value]
            
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            if self.head == node:
                self.head = node.next
            self.deleted.add(value)
            return
        newNode = Node(value)
        self.rec[value] = newNode
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique([2,3,5])
# print(obj.showFirstUnique())
# obj.add(5)
# print(obj.showFirstUnique())
# obj.add(2)
# print(obj.showFirstUnique())
# obj.add(3)
# print(obj.showFirstUnique())