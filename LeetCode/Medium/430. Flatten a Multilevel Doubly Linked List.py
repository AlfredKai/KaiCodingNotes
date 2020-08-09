# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        new_head = Node(None, None, None, None)
        r = new_head
        while stack:
            node = stack.pop()
            print(node.val)
            new_head.next = Node(node.val, new_head, None, None)
            new_head = new_head.next
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        r.next.prev = None
        return r.next

b = Node(1, None, None, None)
b.child = Node(3, b, None, None)
b.next = Node(2, b, None, None)
a = Solution()
c = a.flatten(b)
print()