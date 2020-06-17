# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        curNode = head
        while curNode != None:
            temp = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = temp
            
        return preNode

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        subHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return subHead


b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(4)
b.next.next.next.next = ListNode(5)

a = Solution2()
c = a.reverseList(b)

while c != None:
    print(c.val, end=' ')
    c = c.next