# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None

        curNode = head
        nthFromEnd = head
        count = 0
        while curNode.next != None:
            count += 1
            curNode = curNode.next
            if n < count:
                nthFromEnd = nthFromEnd.next
        else:
            if n == 1 and nthFromEnd == head:
                if nthFromEnd.next == None:
                    return None

            if n == count + 1:
                return nthFromEnd.next

            nthFromEnd.next = nthFromEnd.next.next
        return head

class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listLen = 1
        curNode = head
        while curNode.next != None:
            listLen += 1
            curNode = curNode.next

        if n == listLen:
            return head.next

        count = 1
        curNode = head
        nth = listLen - n
        while curNode.next != None:
            if count == nth:
                curNode.next = curNode.next.next
                break
            count += 1
            curNode = curNode.next
        
        return head
        

a = Solution2()
 
listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
listNode.next.next.next.next = ListNode(5)

b = a.removeNthFromEnd(listNode, 2)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: 1 2 3 5')

listNode = ListNode(1)
listNode.next = ListNode(2)

b = a.removeNthFromEnd(listNode, 2)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: 2')

listNode = ListNode(1)
listNode.next = ListNode(2)

b = a.removeNthFromEnd(listNode, 1)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: 1')

listNode = ListNode(1)

b = a.removeNthFromEnd(listNode, 1)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: []')

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)

b = a.removeNthFromEnd(listNode, 1)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: 1 2')

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)

b = a.removeNthFromEnd(listNode, 2)

while b != None:
    print(b.val, end=' ')
    b = b.next
print('expect: 1 3')